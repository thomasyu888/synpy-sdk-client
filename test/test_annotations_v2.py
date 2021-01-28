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
from synclient.models.annotations_v2 import AnnotationsV2  # noqa: E501
from synclient.rest import ApiException

class TestAnnotationsV2(unittest.TestCase):
    """AnnotationsV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AnnotationsV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.annotations_v2.AnnotationsV2()  # noqa: E501
        if include_optional :
            return AnnotationsV2(
                annotations = {
                    'key' : {"type":"DOUBLE","value":["...","..."]}
                    }, 
                etag = '0', 
                id = '0'
            )
        else :
            return AnnotationsV2(
        )

    def testAnnotationsV2(self):
        """Test AnnotationsV2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
