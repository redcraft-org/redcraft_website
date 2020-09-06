from django.contrib import admin

from donations import models


admin.site.register(models.PlayerDonation)
admin.site.register(models.Coupon)
admin.site.register(models.Donation)
admin.site.register(models.AccesCodeCoupon)
