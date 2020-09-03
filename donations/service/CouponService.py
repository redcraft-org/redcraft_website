from datetime import datetime

from donations import models


class CouponService:
    def createAccesCodeCoupon(self, data_coupon, list_acces_code):
        pass

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
