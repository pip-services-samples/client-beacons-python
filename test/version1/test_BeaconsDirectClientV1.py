# -*- coding: utf-8 -*-

from pip_services3_commons.refer import References, Descriptor

from service_beacons_python.logic import BeaconsController
from service_beacons_python.persistence import BeaconsMemoryPersistence

from src.version1.BeaconsDirectClientV1 import BeaconsDirectClientV1
from .BeaconsClientV1Fixture import BeaconsClientV1Fixture


class TestBeaconsDirectClientV1():
    @classmethod
    def setup_class(cls):
        cls.controller = BeaconsController()
        cls.persistence = BeaconsMemoryPersistence()

        cls.client = BeaconsDirectClientV1()

        cls.references = References.from_tuples(
            Descriptor('beacons', 'persistence', 'memory', 'default', '1.0'), cls.persistence,
            Descriptor('beacons', 'controller', 'default', 'default', '1.0'), cls.controller,
            Descriptor('beacons', 'client', 'http', 'default', '1.0'), cls.client
        )
        cls.controller.set_references(cls.references)
        cls.client.set_references(cls.references)

        cls.fixture = BeaconsClientV1Fixture(cls.client)

        cls.persistence.open(None)

    def teardown_method(self, method):
        self.persistence.close(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_calculate_position(self):
        self.fixture.test_calculate_position()
