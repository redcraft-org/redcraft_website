import io
import base64
import requests
import json
import numpy as np
from PIL import Image


class SkinService:

    OUTER_CHOISE = {
        'true': True,
        'false': False,
    }

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
        profile_data = json.loads(profile_data)
        url_texture = profile_data['textures']['SKIN']['url']

        self.slim = 'metadata' in profile_data['textures']['SKIN']

        # Get image template
        response = requests.get(url_texture)
        image_bytes = io.BytesIO(response.content)

        self.image = Image.open(image_bytes)
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
        if self.size > 8: img = img.resize((self.size, self.size), Image.NEAREST)
        return self.__toPng(img)
        
    def renderBody(self):
        img_skin = self.__getBody()

        if self.outer:
            img_outer = self.__getOuter()
            img_skin.paste(img_outer, (0, 0), img_outer)

        if self.size > 16: img_skin = img_skin.resize((self.size, self.size * 2), Image.NEAREST)
        return self.__toPng(img_skin)

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

    def __getBody(self):
        img_head = self.image.crop((8, 8, 16, 16))
        img_body = self.image.crop((20, 20, 28, 33))
        img_arm_left = self.image.crop((44, 20, 48 - int(self.slim), 32))
        img_arm_right = self.image.crop((36, 52, 40 - int(self.slim), 64))
        img_leg_left = self.image.crop((4, 20, 8, 33))
        img_leg_right = self.image.crop((20, 52, 24, 64))

        img_skin = Image.new('RGBA', (16, 32), color=(0, 0, 0, 0))
        img_skin.paste(img_head, (4, 0))
        img_skin.paste(img_body, (4, 8))
        img_skin.paste(img_arm_left, (int(self.slim), 8))
        img_skin.paste(img_arm_right, (12, 8))
        img_skin.paste(img_leg_left, (4, 20))
        img_skin.paste(img_leg_right, (8, 20))

        return img_skin

    def __getOuter(self):
        img_outer_head = self.image.crop((40, 8, 48, 16))
        img_outer_body = self.image.crop((20, 36, 28, 48))
        img_outer_arm_left = self.image.crop((44, 36, 48 - int(self.slim), 48))
        img_outer_arm_right =self.image.crop((52, 52, 56 - int(self.slim), 64)) 
        img_outer_leg_left = self.image.crop((4, 36, 8, 48))
        img_outer_leg_right = self.image.crop((4, 52, 8, 64))

        img_outer = Image.new('RGBA', (16, 32), color=(0, 0, 0, 0))
        img_outer.paste(img_outer_head, (4, 0))
        img_outer.paste(img_outer_body, (4, 8))
        img_outer.paste(img_outer_arm_left, (int(self.slim), 8))
        img_outer.paste(img_outer_arm_right, (12, 8))
        img_outer.paste(img_outer_leg_left, (4, 20))
        img_outer.paste(img_outer_leg_right, (8, 20))

        return img_outer

    def __toPng(self, img):
        b = io.BytesIO()
        img.save(b, 'PNG')
        return b.getvalue()
