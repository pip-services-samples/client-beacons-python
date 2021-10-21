# -*- coding: utf-8 -*-

from pip_services3_commons.data import DataPage
from pip_services3_rpc.clients import CommandableHttpClient

from .IBeaconsClientV1 import IBeaconsClientV1
from .BeaconV1 import BeaconV1


class BeaconsHttpClientV1(CommandableHttpClient, IBeaconsClientV1):
    def __init__(self):
        super(BeaconsHttpClientV1, self).__init__("v1/beacons")

    def get_beacons_by_filter(self, correlation_id, filter, paging):
        response = self.call_command(
            'get_beacons',
            correlation_id,
            {
                'filter': filter,
                'paging': paging
            }
        )
        page = DataPage(
            data=[BeaconV1(**item) for item in response['data']],
            total=response['total']
        )
        return page

    def get_beacon_by_id(self, correlation_id, id):
        response = self.call_command(
            'get_beacon_by_id',
            correlation_id,
            {
                'id': id
            }
        )
        if response:
            return BeaconV1(**response)

    def get_beacon_by_udi(self, correlation_id, udi):
        response = self.call_command(
            'get_beacon_by_udi',
            correlation_id,
            {
                'udi': udi
            }
        )
        if response:
            return BeaconV1(**response)

    def calculate_position(self, correlation_id, site_id, udis):
        return self.call_command(
            'calculate_position',
            correlation_id,
            {
                'site_id': site_id,
                'udis': udis
            }
        )

    def create_beacon(self, correlation_id, entity):
        response = self.call_command(
            'create_beacon',
            correlation_id,
            {
                'beacon': entity
            }
        )
        if response:
            return BeaconV1(**response)

    def update_beacon(self, correlation_id, entity):
        response = self.call_command(
            'update_beacon',
            correlation_id,
            {
                'beacon': entity
            }
        )
        if response:
            return BeaconV1(**response)

    def delete_beacon_by_id(self, correlation_id, id):
        response = self.call_command(
            'delete_beacon_by_id',
            correlation_id,
            {
                'id': id
            }
        )
        if response:
            return BeaconV1(**response)
