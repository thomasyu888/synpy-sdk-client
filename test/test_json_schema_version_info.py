# coding: utf-8

"""
    Platform Repository Service

    Platform Repository Service - Sage Bionetworks Platform   # noqa: E501

    The version of the OpenAPI document: develop-SNAPSHOT
    Contact: thomas.yu@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import synclient
from synclient.models.json_schema_version_info import JsonSchemaVersionInfo  # noqa: E501
from synclient.rest import ApiException

class TestJsonSchemaVersionInfo(unittest.TestCase):
    """JsonSchemaVersionInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JsonSchemaVersionInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.json_schema_version_info.JsonSchemaVersionInfo()  # noqa: E501
        if include_optional :
            return JsonSchemaVersionInfo(
                id = '0', 
                created_by = '0', 
                created_on = '0', 
                json_sha256_hex = '0', 
                organization_id = '0', 
                organization_name = '0', 
                schema_id = '0', 
                schema_name = '0', 
                semantic_version = '0', 
                version_id = '0'
            )
        else :
            return JsonSchemaVersionInfo(
        )

    def testJsonSchemaVersionInfo(self):
        """Test JsonSchemaVersionInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
