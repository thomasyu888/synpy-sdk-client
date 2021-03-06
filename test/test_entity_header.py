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
from synclient.models.entity_header import EntityHeader  # noqa: E501
from synclient.rest import ApiException

class TestEntityHeader(unittest.TestCase):
    """EntityHeader unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EntityHeader
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.entity_header.EntityHeader()  # noqa: E501
        if include_optional :
            return EntityHeader(
                benefactor_id = 1.337, 
                created_by = '0', 
                created_on = '0', 
                id = '0', 
                modified_by = '0', 
                modified_on = '0', 
                name = '0', 
                type = '0', 
                version_label = '0', 
                version_number = 1.337
            )
        else :
            return EntityHeader(
        )

    def testEntityHeader(self):
        """Test EntityHeader"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
