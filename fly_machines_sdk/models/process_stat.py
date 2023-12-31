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
from pydantic import BaseModel, StrictInt, StrictStr, conlist
from fly_machines_sdk.models.listen_socket import ListenSocket

class ProcessStat(BaseModel):
    """
    ProcessStat
    """
    command: Optional[StrictStr] = None
    cpu: Optional[StrictInt] = None
    directory: Optional[StrictStr] = None
    listen_sockets: Optional[conlist(ListenSocket)] = None
    pid: Optional[StrictInt] = None
    rss: Optional[StrictInt] = None
    rtime: Optional[StrictInt] = None
    stime: Optional[StrictInt] = None
    __properties = ["command", "cpu", "directory", "listen_sockets", "pid", "rss", "rtime", "stime"]

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
    def from_json(cls, json_str: str) -> ProcessStat:
        """Create an instance of ProcessStat from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in listen_sockets (list)
        _items = []
        if self.listen_sockets:
            for _item in self.listen_sockets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['listen_sockets'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ProcessStat:
        """Create an instance of ProcessStat from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ProcessStat.parse_obj(obj)

        _obj = ProcessStat.parse_obj({
            "command": obj.get("command"),
            "cpu": obj.get("cpu"),
            "directory": obj.get("directory"),
            "listen_sockets": [ListenSocket.from_dict(_item) for _item in obj.get("listen_sockets")] if obj.get("listen_sockets") is not None else None,
            "pid": obj.get("pid"),
            "rss": obj.get("rss"),
            "rtime": obj.get("rtime"),
            "stime": obj.get("stime")
        })
        return _obj


