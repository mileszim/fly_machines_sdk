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

from fly_machines_sdk.models.signal_request import SignalRequest  # noqa: E501

class TestSignalRequest(unittest.TestCase):
    """SignalRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SignalRequest:
        """Test SignalRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SignalRequest`
        """
        model = SignalRequest()  # noqa: E501
        if include_optional:
            return SignalRequest(
                signal = 'SIGABRT'
            )
        else:
            return SignalRequest(
        )
        """

    def testSignalRequest(self):
        """Test SignalRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
