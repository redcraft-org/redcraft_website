from django.db import models


class Donation(models.Model):
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



class AccesCodeCoupon(models.Model):
    access_code = models.CharField(max_length=32)
    coupon = models.ForeignKey(
        'Coupon',
        on_delete=models.PROTECT,
        null=True
    )
    player = models.ForeignKey(
        'PlayerDonation',
        on_delete=models.PROTECT,
        null=True
    )


class Coupon(models.Model):
    name = models.CharField(max_length=128)
    is_public = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    stop_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    min_amount = models.DecimalField(max_digits=5 ,decimal_places=2)
    max_amount = models.DecimalField(max_digits=5 ,decimal_places=2)
    modifier = models.DecimalField(max_digits=5, decimal_places=2)
    source = models.CharField(max_length=128)

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
        }


class PlayerDonation(models.Model):
    player_uuid = models.UUIDField(editable=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    real_amount = models.DecimalField(max_digits=10, decimal_places=2)
