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
from synclient.models.doi_response import DoiResponse  # noqa: E501
from synclient.rest import ApiException

class TestDoiResponse(unittest.TestCase):
    """DoiResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DoiResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.doi_response.DoiResponse()  # noqa: E501
        if include_optional :
            return DoiResponse(
                concrete_type = '0', 
                doi = null
            )
        else :
            return DoiResponse(
        )

    def testDoiResponse(self):
        """Test DoiResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
