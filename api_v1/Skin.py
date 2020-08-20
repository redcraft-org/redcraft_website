import io
import base64
import requests
import json
import numpy as np
from PIL import Image


class Skin:
    def __init__(self, ref):

        if len(ref) <= 16:
            # Get player id
            url = 'https://api.mojang.com/users/profiles/minecraft/' + ref
            response = requests.get(url)
            ref = response.json()['id']
        
        # Get player profile
        url = 'https://sessionserver.mojang.com/session/minecraft/profile/' + ref
        response = requests.get(url)
        profile_data = response.json()['properties'][0]['value']

        # Get url skin
        profile_data = base64.b64decode(profile_data)
        url_texture = json.loads(profile_data)['textures']['SKIN']['url']

        # Get image template
        response = requests.get(url_texture)
        image_bytes = io.BytesIO(response.content)
        self.image = Image.open(image_bytes)

    def renderTemplate(self, size=None):
        self.__scale(size)
        return self.__toPng()

    def renderHead(self, size=None):
        self.__crop(8, 8, 16, 16)
        self.__scale(size)
        return self.__toPng()
        
    def renderBody(self, size=None):
        # TODO #
        return self.__toPng()

    def __toPng(self):
        b = io.BytesIO()
        self.image.save(b, 'GIF')
        return b.getvalue()

    def __crop(self, x, y, w, h):
        self.image = self.image.crop((x, y, w, h))

    def __scale(self, size):
        if size is not None: self.image = self.image.resize((size, size), Image.NEAREST)