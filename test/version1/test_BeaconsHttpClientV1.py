# -*- coding: utf-8 -*-

from pip_services3_commons.config import ConfigParams
from pip_services3_commons.refer import References, Descriptor


from service_beacons_python.logic import BeaconsController
from service_beacons_python.persistence import BeaconsMemoryPersistence
from service_beacons_python.services import BeaconsHttpServiceV1

from src.version1 import BeaconsHttpClientV1
from .BeaconsClientV1Fixture import BeaconsClientV1Fixture

http_config = ConfigParams.from_tuples(
    'connection.protocol', 'http',
    'connection.port', 3000,
    'connection.host', 'localhost')


class TestBeaconsHttpClientV1:
    persistence: BeaconsMemoryPersistence
    controller: BeaconsController
    service: BeaconsHttpServiceV1
    client: BeaconsHttpClientV1
    fixture: BeaconsClientV1Fixture

    @classmethod
    def setup_class(cls):
        cls.controller = BeaconsController()
        cls.persistence = BeaconsMemoryPersistence()

        cls.service = BeaconsHttpServiceV1()
        cls.service.configure(http_config)

        cls.client = BeaconsHttpClientV1()
        cls.client.configure(http_config)

        cls.references = References.from_tuples(
            Descriptor('beacons', 'persistence', 'memory', 'default', '1.0'), cls.persistence,
            Descriptor('beacons', 'controller', 'default', 'default', '1.0'), cls.controller,
            Descriptor('beacons', 'service', 'http', 'default', '1.0'), cls.service,
            Descriptor('beacons', 'client', 'http', 'default', '1.0'), cls.client
        )
        cls.controller.set_references(cls.references)
        cls.client.set_references(cls.references)
        cls.service.set_references(cls.references)

        cls.fixture = BeaconsClientV1Fixture(cls.client)

        cls.persistence.open(None)
        cls.service.open(None)
        cls.client.open(None)

    @classmethod
    def teardown_class(cls):
        cls.client.close(None)
        cls.service.close(None)
        cls.persistence.close(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()

    def test_calculate_position(self):
        self.fixture.test_calculate_position()
