from datetime import datetime


now = datetime.now()

COUPON_TEST = {
    'without_coupon': {
        'name': 'without coupon',
        'create_limited_code': True,
        'coupon_data': None
    },
    'with_public_coupon': {
        'name': 'with public coupon',
        'create_limited_code': True,
        'coupon_data': {
            'name': 'test-public',
            'start_date': now,
            'end_date': now.remplace(year=now.year+10),
            'min_amount': 0,
            'max_amount': 100,
            'modifier': 0.25,
            'source': 'noel',
            'public': False
        },
    },
    'with_limited_coupon': {
        'name': 'with limited coupon',
        'create_limited_code': True,
        'coupon_data': {
            'name': 'test-limited',
            'start_date': now,
            'end_date': now.remplace(year=now.year+10),
            'min_amount': 0,
            'max_amount': 100,
            'modifier': 0.5,
            'source': 'event',
            'public': True
        },
    },
}

SCENARIO_TEST = [
    {
        'name': 'success simple donation',
        'data': {
            'player_name': 'Likyaz',
            'is_anonymous': False,
            'amount': 10,
            'is_gift': False,
            'gift_player': None,
            'message': 'I love redcraft!',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'without_coupon',
        'add_code': False,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player']
        }
    },
    {
        'name': 'success simple donation',
        'data': {
            'player_name': 'Likyaz',
            'is_anonymous': False,
            'amount': 10,
            'is_gift': False,
            'gift_player': None,
            'message': 'I love redcraft!',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'with_public_coupon',
        'add_code': True,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
            'access_code': ['access_code', 'unlimited', 'used', 'coupon'],
            'coupon': ['name', 'start_date', 'stop_date', 'min_amount', 'max_amount', 'modifier', 'source', 'public', 'players'],
        }
    },
    {
        'name': 'success simple donation',
        'data': {
            'player_name': 'Likyaz',
            'is_anonymous': False,
            'amount': 10,
            'is_gift': False,
            'gift_player': None,
            'message': 'I love redcraft!',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'with_limited_coupon',
        'add_code': True,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
            'access_code': ['access_code', 'unlimited', 'used', 'coupon'],
            'coupon': ['name', 'start_date', 'stop_date', 'min_amount', 'max_amount', 'modifier', 'source', 'public', 'players'],
        }
    },
    {
        'name': 'success anonym donations',
        'data': {
            'player_name': None,
            'is_anonymous': True,
            'amount': 100,
            'is_gift': False,
            'gift_player': None,
            'message': 'RC <3',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'without_coupon',
        'add_code': False,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player']
        }
    },
    {
        'name': 'success anonym donations',
        'data': {
            'player_name': None,
            'is_anonymous': True,
            'amount': 100,
            'is_gift': False,
            'gift_player': None,
            'message': 'RC <3',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'with_public_coupon',
        'add_code': True,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
            'access_code': ['access_code', 'unlimited', 'used', 'coupon'],
            'coupon': ['name', 'start_date', 'stop_date', 'min_amount', 'max_amount', 'modifier', 'source', 'public', 'players'],
        }
    },
    {
        'name': 'success anonym donations',
        'data': {
            'player_name': None,
            'is_anonymous': True,
            'amount': 100,
            'is_gift': False,
            'gift_player': None,
            'message': 'RC <3',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'with_limited_coupon',
        'add_code': True,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
            'access_code': ['access_code', 'unlimited', 'used', 'coupon'],
            'coupon': ['name', 'start_date', 'stop_date', 'min_amount', 'max_amount', 'modifier', 'source', 'public', 'players'],
        }
    },
    {
        'name': 'success simple gift donations',
        'data': {
            'player_name': 'lululombard',
            'is_anonymous': False,
            'amount': 10,
            'is_gift': True,
            'gift_player': 'Likyaz',
            'message': 'Little Likyaz',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'without_coupon',
        'add_code': False,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
        }
    },
    {
        'name': 'success simple gift donations',
        'data': {
            'player_name': 'lululombard',
            'is_anonymous': False,
            'amount': 10,
            'is_gift': True,
            'gift_player': 'Likyaz',
            'message': 'Little Likyaz',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'with_public_coupon',
        'add_code': True,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
            'access_code': ['access_code', 'unlimited', 'used', 'coupon'],
            'coupon': ['name', 'start_date', 'stop_date', 'min_amount', 'max_amount', 'modifier', 'source', 'public', 'players'],
        }
    },
    {
        'name': 'success simple gift donations',
        'data': {
            'player_name': 'lululombard',
            'is_anonymous': False,
            'amount': 10,
            'is_gift': True,
            'gift_player': 'Likyaz',
            'message': 'Little Likyaz',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'with_limited_coupon',
        'add_code': True,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
            'access_code': ['access_code', 'unlimited', 'used', 'coupon'],
            'coupon': ['name', 'start_date', 'stop_date', 'min_amount', 'max_amount', 'modifier', 'source', 'public', 'players'],
        }
    },
    {
        'name': 'success anonym gift donations',
        'data': {
            'player_name': None,
            'is_anonymous': True,
            'amount': 10,
            'is_gift': True,
            'gift_player': 'Redvax',
            'message': 'Just for you!!',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'without_coupon',
        'add_code': False,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
        }
    },
    {
        'name': 'success anonym gift donations',
        'data': {
            'player_name': None,
            'is_anonymous': True,
            'amount': 10,
            'is_gift': True,
            'gift_player': 'Redvax',
            'message': 'Just for you!!',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'with_public_coupon',
        'add_code': True,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
            'access_code': ['access_code', 'unlimited', 'used', 'coupon'],
            'coupon': ['name', 'start_date', 'stop_date', 'min_amount', 'max_amount', 'modifier', 'source', 'public', 'players'],
        }
    },
    {
        'name': 'success anonym gift donations',
        'data': {
            'player_name': None,
            'is_anonymous': True,
            'amount': 10,
            'is_gift': True,
            'gift_player': 'Redvax',
            'message': 'Just for you!!',
            'source': 'paypal',
        },
        'coupon_scenario_use': 'with_limited_coupon',
        'add_code': True,
        'res': {'response': True},
        'add_id_to_res': True,
        'refunded': False,
        'models_to_test': {
            'donations': ['amount', 'create_at', 'source', 'message', 'refunded', 'coupon', 'player', 'gift_player'],
            'access_code': ['access_code', 'unlimited', 'used', 'coupon'],
            'coupon': ['name', 'start_date', 'stop_date', 'min_amount', 'max_amount', 'modifier', 'source', 'public', 'players'],
        }
    }
]

player_test = {
    'anonymous': {
        'total_amount': 0,
        'real_amount': 0
    }
}

for scenario in SCENARIO_TEST:
    player_name = scenario['data']['player_name']
    gift_player = scenario['data']['gift_player']
    amount = scenario['data']['amount']
    real_amount = scenario['data']['amount']

    if player_name is not None and player_name not in player_test:
        player_test[player_name] = {
            'total_amount': 0,
            'real_amount': 0
        }
    if gift_player is not None and gift_player not in player_test:
        player_test[gift_player] = {
            'total_amount': 0,
            'real_amount': 0
        }

    if scenario['data']['is_gift']:
        # Is a Gift
        total_value = scenario['data']['amount'] + scenario['data']['amount'] * COUPON_TEST[scenario['coupon_scenario_use']]['coupon_data']['modifier']
        if gift_player is not None:
            player_test[gift_player]['total_amount'] = player_test[gift_player]['total_amount'] + total_value
        if player_name is not None:
            player_test[player_name]['real_amount'] = player_test[player_name]['real_amount'] + scenario['data']['amount']
    else:
        # Is not a gift
        total_value = scenario['data']['amount'] + scenario['data']['amount'] * COUPON_TEST[scenario['coupon_scenario_use']]['coupon_data']['modifier']
        if player_name is not None:
            player_test[player_name]['total_amount'] = player_test[player_name]['total_amount'] + total_value
            player_test[player_name]['real_amount'] = player_test[player_name]['real_amount'] + scenario['data']['amount']
        else:
            player_test['anonymous']['total_amount'] = player_test['anonymous']['total_amount'] + total_value
            player_test['anonymous']['real_amount'] = player_test['anonymous']['real_amount'] + scenario['data']['amount']
