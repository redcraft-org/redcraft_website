import requests
from network_data import models
from django.conf import settings

class NetworkDescriptionService:
    def createNetworkDescription(self, title, text, overview, path_img, active):
        network_description = models.NetworkDescription(title=title, text=text, overview=overview, path_img=path_img, active=active)

    def getAll(self):
        return list(models.NetworkDescription.objects.all())

    def getAllActive(self):
        return list(models.NetworkDescription.objects.filter(active=True))

    def getMinecraftVersions(self):
        url_proxy = settings.PROXY_REDCRAFT['versions']
        response = requests.get(url_proxy)
        return response.json()

    def getMinecraftPlayers(self):
        url_proxy = settings.PROXY_REDCRAFT['players']
        response = requests.get(url_proxy)
        return response.json()

    def getMinecraftVersionsMinMax(self):
        minecraft_versions = self.getMinecraftVersions()
        return (
            minecraft_versions["supportedVersions"][0],
            minecraft_versions["supportedVersions"][-1],
        )

    def countPlayers(self):
        minecraft_players = self.getMinecraftPlayers()
        count_players = 0
        for _, server_data in minecraft_players['players'].items():
            count_players += len(server_data)
        return count_players
