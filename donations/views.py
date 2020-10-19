from datetime import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect

from donations.service.CouponService import CouponService


def createCoupon(request):
    return JsonResponse(CouponService().createCoupon(
        {
            'name': 'test',
            'is_public': True,
            'start_date': datetime(2020, 1, 1),
            'stop_date': datetime(2021, 1, 1),
            'min_amount': 1,
            'max_amount': 2,
            'modifier': 1,
            'source': 'test',
        }, 3
    ))

def getCoupons(request):
    return JsonResponse(CouponService().getCoupons())

def getFutureCoupon(request):
    return JsonResponse(CouponService().getFutureCoupon())

def getPassedCoupon(request):
    return JsonResponse(CouponService().getPassedCoupon())

def getCurrentCoupon(request):
    return JsonResponse(CouponService().getCurrentCoupon())

def getCouponById(request):
    return JsonResponse(CouponService().getCouponById(1))
