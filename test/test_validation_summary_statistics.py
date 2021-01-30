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
from synclient.models.validation_summary_statistics import ValidationSummaryStatistics  # noqa: E501
from synclient.rest import ApiException

class TestValidationSummaryStatistics(unittest.TestCase):
    """ValidationSummaryStatistics unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ValidationSummaryStatistics
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.validation_summary_statistics.ValidationSummaryStatistics()  # noqa: E501
        if include_optional :
            return ValidationSummaryStatistics(
                container_id = '0', 
                generated_on = '0', 
                number_of_invalid_children = 56, 
                number_of_unknown_children = 56, 
                number_of_valid_children = 56, 
                total_number_of_children = 56
            )
        else :
            return ValidationSummaryStatistics(
        )

    def testValidationSummaryStatistics(self):
        """Test ValidationSummaryStatistics"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()