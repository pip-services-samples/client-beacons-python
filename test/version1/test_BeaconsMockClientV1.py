# -*- coding: utf-8 -*-
from src.version1.BeaconsMockClientV1 import BeaconsMockClientV1

from test.version1.BeaconsClientV1Fixture import BeaconsClientV1Fixture


class TestBeaconsMockClientV1:
    @classmethod
    def setup_class(cls):
        cls.client = BeaconsMockClientV1()
        cls.fixture = BeaconsClientV1Fixture(cls.client)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_calculate_position(self):
        self.fixture.test_calculate_position()
