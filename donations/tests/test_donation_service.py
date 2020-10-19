from datetime import datetime
from django.test import TestCase
from donations.service import DonationsService
from donations import models

from donations.test import scenarios_donations as scenarios


class DonationsServiceTest(TestCase):
    def setUp(self):
        now = datetime.now()
        self.coupon_set_test = scenarios.COUPON_TEST

        for coupon_data in self.coupon_set_test:
            # create coupon with coupon_data
            coupon_data['coupon'] = models.Coupon.objects.create(**coupon_data['coupon_data']) if coupon_data['coupon_data'] else None
            # create and add public access code at public coupon
            if coupon_data['coupon_data']['public']:
                code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                access_code_coupon = models.AccessCodeCoupon.objects.create(
                    access_code=code,
                    unlimited=True,
                    coupon=coupon_data['coupon']
                )
                coupon_data['code'] = code

    def test_scenarios(self):
        donation_service = DonationsService()

        for scenario in scenarios.SCENARIO_TEST:
            coupon_used = self.coupon_set_test[scenario['coupon_scenario_use']]

            # Create access code coupon if need
            if coupon_used['create_limited_code']:
                code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
                access_code_coupon = models.AccessCodeCoupon.objects.create(
                    access_code=code,
                    unlimited=True,
                    coupon=coupon_used['coupon']
                )
                coupon_data['code'] = code

            # Create data params for new donations
            data = scenario['data'].copy()
            if scenario['add_code']: data['code'] = coupon_data['code']

            # Call service to add donations
            res = donation_service.newDonation(**data)

            # Add id to res if need it
            if scenario['add_id_to_res']: scenario['res']['response']['id'] = res.id

            # Check return
            self.assertEqual(scenario['res']['response'], res['response'],
                f"{scenario['name']} {coupon_used['name']} - the response does not match\
                {res['response']}\nIs not equal at:\n{scenario['res']['response']}"
            )

            # if refunded
            if scenario['refunded']:
                donations_object = models.Donations.objects.get(id=res.id)
                donations_object.refunded = True
                donations_object.save()

            # check models
            if 'models_to_test' in scenario:
                self.check_donation(coupon_used)
                self.check_access_code()
                self.check_coupon()

    def check_donation(self, coupon_used):
        # Check donations row in database
        if 'donations' in scenario['models_to_test']:
            donations_object = models.Donations.objects.get(id=res.id)

            if 'amount' in scenario['models_to_test']['donations']:
                self.assertEqual(donations_object.amount, scenario['data']['amount'],
                    f"{scenario['name']} {coupon_used['name']} - amount don't match\
                    {donations_object.amount}\nIs not equal at:\n{scenario['data']['amount']}"
                )

            # TODO #
            # if 'create_at' in scenario['models_to_test']['donations']:
            #     self.assertEqual()

            if 'source' in scenario['models_to_test']['donations']:
                self.assertEqual(donations_object.source, scenario['data']['source'],
                    f"{scenario['name']} {coupon_used['name']} - source don't match\
                    {donations_object.source}\nIs not equal at:\n{scenario['data']['source']}"
                )

            if 'message' in scenario['models_to_test']['donations']:
                self.assertEqual(donations_object.message, scenario['data']['message'],
                    f"{scenario['name']} {coupon_used['name']} - message don't match\
                    {donations_object.message}\nIs not equal at:\n{scenario['data']['message']}"
                )

            if 'refunded' in scenario['models_to_test']['donations']:
                self.assertEqual(donations_object.refunded, scenario['refunded'],
                    f"{scenario['name']} {coupon_used['name']} - coupon don't match\
                    {donations_object.coupon}\nIs not equal at:\n{scenario['refunded']}"
                )

            if 'anonym' in scenario['models_to_test']['donations']:
                self.assertEqual(donations_object.anonym, scenario['anonym'],
                    f"{scenario['name']} {coupon_used['name']} - anonym don't match\
                    {donations_object.anonym}\nIs not equal at:\n{scenario['anonym']}"
                )

            if 'coupon' in scenario['models_to_test']['donations']:
                self.assertEqual(donations_object.coupon, coupon_used['coupon'],
                    f"{scenario['name']} {coupon_used['name']} - coupon don't match\
                    {donations_object.coupon}\nIs not equal at:\n{coupon_used['coupon']}"
                )

            if 'player' in scenario['models_to_test']['donations']:
                try:
                    player = models.PlayerDonation.objects.get(name=scenario['data']['player'])
                except models.PlayerDonation.DoesNotExist:
                    self.assertTrue(False, 
                        f"{scenario['name']} {coupon_used['name']} - don't find player\
                        {scenario['data']['player']}"
                    )
                else:
                    self.assertEqual(donations_object.player, player,
                        f"{scenario['name']} {coupon_used['name']} - player don't match\
                        {donations_object.player}\nIs not equal at:\n{player}"
                    )

            if 'gift_player' in scenario['models_to_test']['donations']:
                try:
                    player = models.PlayerDonation.objects.get(name=scenario['data']['gift_player'])
                except models.PlayerDonation.DoesNotExist:
                    self.assertTrue(False, 
                        f"{scenario['name']} {coupon_used['name']} - don't find gift_player\
                        {scenario['data']['gift_player']}"
                    )
                else:
                    self.assertEqual(donations_object.gift_player, player,
                        f"{scenario['name']} {coupon_used['name']} - gift_player don't match\
                        {donations_object.gift_player}\nIs not equal at:\n{player}"
                    )

    def check_access_code(self):
        if 'access_code' in scenario['models_to_test']:
            if 'access_code' in scenario['models_to_test']['access_code']:
                self.assertEqual(donations_object.coupon, coupon_used['coupon'])
                
            if 'unlimited' in scenario['models_to_test']['access_code']:
                self.assertEqual(donations_object.coupon, coupon_used['coupon'])
                
            if 'used' in scenario['models_to_test']['access_code']:
                self.assertEqual(donations_object.coupon, coupon_used['coupon'])
                
            if 'coupon' in scenario['models_to_test']['access_code']:
                self.assertEqual(donations_object.coupon, coupon_used['coupon'])


    def check_coupon(self):
        if 'coupon' in scenario['models_to_test']:
            pass
