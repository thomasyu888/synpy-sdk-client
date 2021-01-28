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
from synclient.models.submission_status_enum import SubmissionStatusEnum  # noqa: E501
from synclient.rest import ApiException

class TestSubmissionStatusEnum(unittest.TestCase):
    """SubmissionStatusEnum unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubmissionStatusEnum
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.submission_status_enum.SubmissionStatusEnum()  # noqa: E501
        if include_optional :
            return SubmissionStatusEnum(
            )
        else :
            return SubmissionStatusEnum(
        )

    def testSubmissionStatusEnum(self):
        """Test SubmissionStatusEnum"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
