# coding: utf-8

"""
    Fly Machines API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from fly_machines_sdk.models.api_machine_config import ApiMachineConfig
from fly_machines_sdk.models.check_status import CheckStatus
from fly_machines_sdk.models.image_ref import ImageRef
from fly_machines_sdk.models.machine_event import MachineEvent

class Machine(BaseModel):
    """
    Machine
    """
    checks: Optional[conlist(CheckStatus)] = None
    config: Optional[ApiMachineConfig] = None
    created_at: Optional[StrictStr] = None
    events: Optional[conlist(MachineEvent)] = None
    id: Optional[StrictStr] = None
    image_ref: Optional[ImageRef] = None
    instance_id: Optional[StrictStr] = Field(None, description="InstanceID is unique for each version of the machine")
    name: Optional[StrictStr] = None
    nonce: Optional[StrictStr] = Field(None, description="Nonce is only every returned on machine creation if a lease_duration was provided.")
    private_ip: Optional[StrictStr] = Field(None, description="PrivateIP is the internal 6PN address of the machine.")
    region: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    updated_at: Optional[StrictStr] = None
    __properties = ["checks", "config", "created_at", "events", "id", "image_ref", "instance_id", "name", "nonce", "private_ip", "region", "state", "updated_at"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Machine:
        """Create an instance of Machine from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in checks (list)
        _items = []
        if self.checks:
            for _item in self.checks:
                if _item:
                    _items.append(_item.to_dict())
            _dict['checks'] = _items
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in events (list)
        _items = []
        if self.events:
            for _item in self.events:
                if _item:
                    _items.append(_item.to_dict())
            _dict['events'] = _items
        # override the default output from pydantic by calling `to_dict()` of image_ref
        if self.image_ref:
            _dict['image_ref'] = self.image_ref.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Machine:
        """Create an instance of Machine from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Machine.parse_obj(obj)

        _obj = Machine.parse_obj({
            "checks": [CheckStatus.from_dict(_item) for _item in obj.get("checks")] if obj.get("checks") is not None else None,
            "config": ApiMachineConfig.from_dict(obj.get("config")) if obj.get("config") is not None else None,
            "created_at": obj.get("created_at"),
            "events": [MachineEvent.from_dict(_item) for _item in obj.get("events")] if obj.get("events") is not None else None,
            "id": obj.get("id"),
            "image_ref": ImageRef.from_dict(obj.get("image_ref")) if obj.get("image_ref") is not None else None,
            "instance_id": obj.get("instance_id"),
            "name": obj.get("name"),
            "nonce": obj.get("nonce"),
            "private_ip": obj.get("private_ip"),
            "region": obj.get("region"),
            "state": obj.get("state"),
            "updated_at": obj.get("updated_at")
        })
        return _obj


