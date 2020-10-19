from donations import models


class DonationsService:
    def newDonation(self, amount, player_uuid, data={}):
        try:
            coupon = models.Coupon.objects.get(id=data['id_coupon'])
        except KeyError as e:
            return {'err': f'need {str(e)}'}
        except models.coupon.DoesNotExist:
            return {'err': 'coupon not exist'}
        else:
            if 'code_coupon' in data and coupon.needCode():
                coupon.check

        donations_object = models.Donations.object.create()
        data = {
            'amount': amount,
        }

        return {'response': True, 'id': donations_object.id}

    def getDonations(self):
        pass

    def getDonation(self):
        pass

    def getPlayerDonations(self):
        pass
