# -*- coding: utf-8 -*-

from pip_services3_commons.validate.ObjectSchema import ObjectSchema


class BeaconV1Schema(ObjectSchema):
    def __init__(self):
        super().__init__()
        self.with_optional_property("id", "String")
        self.with_required_property("site_id", "String")
        self.with_optional_property("type", "String")
        self.with_required_property("udi", "String")
        self.with_optional_property("label", "String")
        self.with_optional_property("center", "Object")
        self.with_optional_property("radius", "float")
