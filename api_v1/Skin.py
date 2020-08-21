import io
import base64
import requests
import json
import numpy as np
from PIL import Image


class Skin:

    OUTER_CHOISE = {
        'true': True,
        'false': False}

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

        self.image = Image.open(image_bytes).convert("RGBA")
        self.size = 0
        self.outer = True

    def renderTemplate(self):
        img = self.image
        if self.size > 0: img = img.resize((self.size, self.size), Image.NEAREST)
        return self.__toPng(img)

    def renderHead(self):
        img_head = self.image.crop((8, 8, 16, 16))
        if self.outer:
            img_outer = self.image.crop((40, 8, 48, 16))
            img_head.paste(img_outer, (0, 0), img_outer)
        img = img_head
        if self.size > 0: img = img.resize((self.size, self.size), Image.NEAREST)
        return self.__toPng(img)
        
    def renderBody(self):
        # TODO #
        img = self.image
        if self.size > 0: img = img.resize((self.size, self.size), Image.NEAREST)
        return self.__toPng(img)

    def loadRequest(self, request):
        self.size = request.GET.get('size', 0)
        try:
            self.size = int(self.size)
        except ValueError:
            return 'size must be int'

        self.outer = request.GET.get('outer', 'true')
        if self.outer in self.OUTER_CHOISE: 
            self.outer = self.OUTER_CHOISE[self.outer]
        else:
            return 'outer must be bool' 

        return False

    def __toPng(self, img):
        b = io.BytesIO()
        img.save(b, 'GIF')
        return b.getvalue()
