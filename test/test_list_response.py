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
from synclient.models.list_response import ListResponse  # noqa: E501
from synclient.rest import ApiException

class TestListResponse(unittest.TestCase):
    """ListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.list_response.ListResponse()  # noqa: E501
        if include_optional :
            return ListResponse(
                next_page_token = '0', 
                page = [
                    {"createdBy":"...","createdOn":"...","dataFileHandleId":"...","etag":"...","formDataId":"...","groupId":"...","modifiedOn":"...","name":"...","submissionStatus":{"rejectionMessage":"...","reviewedBy":"...","reviewedOn":"...","state":"REJECTED","submittedOn":"..."}}
                    ]
            )
        else :
            return ListResponse(
        )

    def testListResponse(self):
        """Test ListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
