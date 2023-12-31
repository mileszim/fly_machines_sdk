# coding: utf-8

"""
    Fly Machines API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from fly_machines_sdk.models.extend_volume_response import ExtendVolumeResponse  # noqa: E501

class TestExtendVolumeResponse(unittest.TestCase):
    """ExtendVolumeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExtendVolumeResponse:
        """Test ExtendVolumeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExtendVolumeResponse`
        """
        model = ExtendVolumeResponse()  # noqa: E501
        if include_optional:
            return ExtendVolumeResponse(
                needs_restart = True,
                volume = fly_machines_sdk.models.volume.Volume(
                    attached_alloc_id = '', 
                    attached_machine_id = '', 
                    block_size = 56, 
                    blocks = 56, 
                    blocks_avail = 56, 
                    blocks_free = 56, 
                    created_at = '', 
                    encrypted = True, 
                    fstype = '', 
                    id = '', 
                    name = '', 
                    region = '', 
                    size_gb = 56, 
                    snapshot_retention = 56, 
                    state = '', 
                    zone = '', )
            )
        else:
            return ExtendVolumeResponse(
        )
        """

    def testExtendVolumeResponse(self):
        """Test ExtendVolumeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
