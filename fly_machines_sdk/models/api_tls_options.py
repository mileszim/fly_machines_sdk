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
from pydantic import BaseModel, StrictBool, StrictStr, conlist

class ApiTLSOptions(BaseModel):
    """
    ApiTLSOptions
    """
    alpn: Optional[conlist(StrictStr)] = None
    default_self_signed: Optional[StrictBool] = None
    versions: Optional[conlist(StrictStr)] = None
    __properties = ["alpn", "default_self_signed", "versions"]

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
    def from_json(cls, json_str: str) -> ApiTLSOptions:
        """Create an instance of ApiTLSOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiTLSOptions:
        """Create an instance of ApiTLSOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ApiTLSOptions.parse_obj(obj)

        _obj = ApiTLSOptions.parse_obj({
            "alpn": obj.get("alpn"),
            "default_self_signed": obj.get("default_self_signed"),
            "versions": obj.get("versions")
        })
        return _obj


