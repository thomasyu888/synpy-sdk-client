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
from synclient.models.entity_children_response import EntityChildrenResponse  # noqa: E501
from synclient.rest import ApiException

class TestEntityChildrenResponse(unittest.TestCase):
    """EntityChildrenResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EntityChildrenResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.entity_children_response.EntityChildrenResponse()  # noqa: E501
        if include_optional :
            return EntityChildrenResponse(
                next_page_token = '0', 
                page = [
                    {"benefactorId":12345,"createdBy":"...","createdOn":"...","id":"...","modifiedBy":"...","modifiedOn":"...","name":"...","type":"...","versionLabel":"...","versionNumber":12345}
                    ], 
                sum_file_sizes_bytes = 56, 
                total_child_count = 56
            )
        else :
            return EntityChildrenResponse(
        )

    def testEntityChildrenResponse(self):
        """Test EntityChildrenResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
