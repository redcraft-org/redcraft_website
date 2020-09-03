from datetime import datetime

from donations import models


class CouponService:
    def setCoupon(self, data):
        if 'name' not in data:
            return {'err': 'name is not define'}
        if 'is_public' not in data:
            return {'err': 'is_public is not define'}
        if 'start_date' not in data:
            return {'err': 'start_date is not define'}
        if 'stop_date' not in data:
            return {'err': 'stop_date is not define'}
        if 'min_amount' not in data:
            return {'err': 'min_amount is not define'}
        if 'max_amount' not in data:
            return {'err': 'max_amount is not define'}
        if 'modifier' not in data:
            return {'err': 'modifier is not define'}
        if 'source' not in data:
            return {'err': 'source is not define'}

        coupon = models.Coupon(**data)

    def createAccesCodeCoupon(self, data_coupon, data_acces_code):


    def getCoupons(self):
        return [ coupon.toArray() for coupon in models.Coupon.objects.all() ]

    def getFuturCoupon(self):
        return [ coupon.toArray() for coupon in models.Coupon.objects.filter(start_date__gt=datetime.now()) ]

    def getPassedCoupon(self):
        return [ coupon.toArray() for coupon in models.Coupon.objects.filter(stop_date__lt=datetime.now()) ]

    def getCurrentCoupon(self):
        return [ coupon.toArray() for coupon in models.Coupon.objects.filter(start_date__lt=datetime.now(), stop_date__gt=datetime.now()) ]

    def getCouponByName(self, name):
        try:
            return models.Coupon.objects.get(name=name).toArray()
        except models.Coupon.DoesNotExist:
            return {'err': f'{name} not existe'}

    def getCouponById(self, id):
        try:
            return models.Coupon.objects.get(id=id).toArray()
        except models.Coupon.DoesNotExist:
            return {'err': f'{id} not existe'}
