from django.db import models


class Donation(models.Model):
    '''
    single donation made by a player

    amount: donation value
    create_at: date of donation
    source: 
    message: message transmitted at the time of the donation
    refunded: true if the donation has been refunded
    coupon: coupon applied to the donation
    player: player who makes the gift, in the case of a gift then it is the player who gives the gift.
    gift_player: player who is offered a gift, if null then the gift is not a gift
    '''
    amount = models.DecimalField(editable=False, max_digits=8, decimal_places=2)
    create_at = models.DateTimeField(editable=False, auto_now=False, auto_now_add=True)
    source = models.CharField(max_length=128)
    message = models.CharField(max_length=280)
    refunded = models.BooleanField(default=False)
    coupon = models.ForeignKey(
        'Coupon',
        on_delete=models.PROTECT,
    )
    player = models.ForeignKey(
        'PlayerDonation',
        on_delete=models.PROTECT,
        null=True
    )
    gift_player = models.ForeignKey(
        'PlayerDonation',
        on_delete=models.PROTECT,
        null=True
    )



class AccesCodeCoupon(models.Model):
    '''
    The code associated with a coupon

    access_code: The coupon access code
    unlimited: If false then can only be used once.
    used: if unlimited is true, then used becomes true once the code is used.
    coupon: The coupon associated with the access code
    '''
    access_code = models.CharField(max_length=32)
    unlimited = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    coupon = models.ForeignKey(
        'Coupon',
        on_delete=models.PROTECT,
        null=True
    )


class Coupon(models.Model):
    '''
    Discount coupon

    name: 
    start_date, stop_date:
    min_amount, max_amount:
    modifier: 
    source: 
    public: 
    players: 
    '''
    name = models.CharField(max_length=128)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    stop_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    min_amount = models.DecimalField(max_digits=5 ,decimal_places=2)
    max_amount = models.DecimalField(max_digits=5 ,decimal_places=2)
    modifier = models.DecimalField(max_digits=5, decimal_places=2)
    source = models.CharField(max_length=128)
    public = models.BooleanField(default=True)
    players = models.ManyToManyField(PlayerDonation)

    def isNeedCode(self):
        return len(self.accesscodecoupon_set.all()) > 0

    def valideCode(self, code):
        try:
            accescode_object = self.accesscodecoupon_set.get(access_code=code)
        except self.DoesNotExist:
            return False
        else:
            # accescode_object.
            return True
            

    def toArray(self):
        return {
            'id': self.id,
            'name': self.name,
            'is_public': self.is_public,
            'start_date': self.start_date,
            'stop_date': self.stop_date,
            'min_amount': self.min_amount,
            'max_amount': self.max_amount,
            'modifier': self.modifier,
            'source': self.source,
            'code': [
                {
                    'code': code.access_code,
                    'player': code.player,
                } for code in self.accescodecoupon_set.all()
            ]
        }


class PlayerDonation(models.Model):
    '''
    A player who made a donation

    uuid: 
    name: 
    total_amount: 
    real_amount: 
    '''
    uuid = models.UUIDField(editable=False)
    name = modes.CharField(max_length=64)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    real_amount = models.DecimalField(max_digits=10, decimal_places=2)
