from django.urls import path, re_path

from donations import views


urlpatterns = [
    path('coupon/check/code/<str:code>', views.createCoupon, name='check_code_coupon'),
]
