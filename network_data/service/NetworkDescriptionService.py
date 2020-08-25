from network_data import models

class NetworkDescriptionService:
    def createNetworkDescription(self, title, text, overview, path_img, active):
        network_description = models.NetworkDescription(title=title, text=text, overview=overview, path_img=path_img, active=active)

    def getAll(self):
        return list(models.NetworkDescription.objects.all())

    def getAllActive(self):
        return list(models.NetworkDescription.objects.filter(active=True))
