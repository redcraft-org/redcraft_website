from network_data import models

class NetworkDescriptionService:
    def createNetworkDescription(self, title, text, overview, path_img, active):
        network_description = models.NetworkDescription(title=title, text=text, overview=overview, path_img=path_img, active=active)

    def getAll(self):
        return list(models.NetworkDescription.objects.all())

    def getAllActive(self):
        return list(models.NetworkDescription.objects.filter(active=True))

    def getMinecraftVersions(self):
        # TODO : Call the API instead of hard-coded dict
        return {
            "serverSoftware": "RedCraft",
            "mainVersion": "1.16.2",
            "supportedVersions": [
                "1.8.x", "1.9", "1.9.1", "1.9.2", "1.9.3/4", 
                "1.10", "1.11", "1.11.1", "1.12", "1.12.1", 
                "1.12.2", "1.13", "1.13.1", "1.13.2", "1.14", 
                "1.14.1", "1.14.2", "1.14.3", "1.14.4", "1.15", 
                "1.15.1", "1.15.2", "1.16", "1.16.1", "1.16.2"
            ]
        }
