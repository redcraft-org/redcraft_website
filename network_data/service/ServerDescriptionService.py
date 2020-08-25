from network_data import models

class ServerDescriptionService:
    def createServerDescription(self, title, text, overview, path_img, active):
        network_description = models.ServerDescription(title=title, text=text, overview=overview, path_img=path_img, active=active)

    def getAll(self):
        return list(models.ServerDescription.objects.all())

    def getAllActive(self):
        return list(models.ServerDescription.objects.filter(active=True))
