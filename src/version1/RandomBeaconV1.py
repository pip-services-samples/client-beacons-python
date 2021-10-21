# -*- coding: utf-8 -*-

from typing import Any

from pip_services3_commons.random import RandomArray, RandomInteger

from src.version1 import BeaconTypeV1, BeaconV1


class RandomBeaconV1:
    @staticmethod
    def next_beacon_type() -> str:
        return RandomArray.pick(
            [
                BeaconTypeV1.AltBeacon, BeaconTypeV1.EddyStoneUdi,
                BeaconTypeV1.Unknown, BeaconTypeV1.iBeacon
            ]
        )

    @staticmethod
    def next_beacon_center() -> Any:
        return {
            'type': 'Point',
            'center': {
                'coordinates': [RandomInteger.next_integer(1, 1000), RandomInteger.next_integer(1, 1000)]
            }
        }

    @staticmethod
    def next_beacon() -> BeaconV1:
        return BeaconV1(
            id=None,
            site_id=None,
            type=RandomBeaconV1.next_beacon_type(),
            udi=RandomArray.pick(['00001', '00002', '00003', '00004']),
            label=None,
            center=RandomBeaconV1.next_beacon_center(),
            radius=RandomInteger.next_integer(1, 1000)
        )
