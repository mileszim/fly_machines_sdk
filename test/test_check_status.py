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

from fly_machines_sdk.models.check_status import CheckStatus  # noqa: E501

class TestCheckStatus(unittest.TestCase):
    """CheckStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CheckStatus:
        """Test CheckStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CheckStatus`
        """
        model = CheckStatus()  # noqa: E501
        if include_optional:
            return CheckStatus(
                name = '',
                output = '',
                status = '',
                updated_at = ''
            )
        else:
            return CheckStatus(
        )
        """

    def testCheckStatus(self):
        """Test CheckStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()