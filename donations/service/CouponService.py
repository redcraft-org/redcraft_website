from datetime import datetime
import random
import string
from donations import models


class CouponService:
    def createCoupon(self, data_coupon, nb_access_code=None):
        try:
            if data_coupon['start_date'] >= data_coupon['stop_date']:
                return {'err': 'start_date can\'t before stop_date'}
            if data_coupon['min_amount'] >= data_coupon['max_amount']:
                return {'err': 'min_amount can\'t smaller max_amount'}
        except KeyError as e:
            return {'err': f'need {str(e)}'}

        if 'name' not in data_coupon:
            return {'err': 'need name'}
        if 'modifier' not in data_coupon:
            return {'err': 'need modifier'}
        if 'source' not in data_coupon:
            return {'err': 'need source'}

        coupon_object = models.Coupon(**data_coupon)
        coupon_object.save()

        if nb_access_code > 0:
            for i in range(nb_access_code):
                access_code = models.AccesCodeCoupon(
                    access_code=''.join(random.choices(string.ascii_letters + string.digits, k=6)),
                    coupon=coupon_object
                )
                access_code.save()

        return {'response': True, 'id': coupon_object.id}

    def getCoupons(self):
        return  {coupon.id: coupon.toArray() for coupon in models.Coupon.objects.all()}

    def getFutureCoupon(self):
        return {coupon.id: coupon.toArray() for coupon in models.Coupon.objects.filter(start_date__gt=datetime.now())}

    def getPassedCoupon(self):
        return {coupon.id: coupon.toArray() for coupon in models.Coupon.objects.filter(stop_date__lt=datetime.now())}

    def getCurrentCoupon(self):
        return {coupon.id: coupon.toArray() for coupon in models.Coupon.objects.filter(start_date__lt=datetime.now(), stop_date__gt=datetime.now())}

    def getCouponByName(self, name):
        try:
            coupon = models.Coupon.objects.get(name=name)
        except models.Coupon.DoesNotExist:
            return {'err': f'{name} not exist'}
        else:
            coupon_data = coupon.toArray()
            coupon_data['id'] = coupon.id
            return coupon_data

    def getCouponById(self, id):
        try:
            coupon = models.Coupon.objects.get(id=id)
        except models.Coupon.DoesNotExist:
            return {'err': f'{id} not exist'}
        else:
            coupon_data = coupon.toArray()
            coupon_data['id'] = coupon.id
            return coupon_data
