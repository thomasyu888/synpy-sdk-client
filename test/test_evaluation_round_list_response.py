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
from synclient.models.evaluation_round_list_response import EvaluationRoundListResponse  # noqa: E501
from synclient.rest import ApiException

class TestEvaluationRoundListResponse(unittest.TestCase):
    """EvaluationRoundListResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EvaluationRoundListResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.evaluation_round_list_response.EvaluationRoundListResponse()  # noqa: E501
        if include_optional :
            return EvaluationRoundListResponse(
                next_page_token = '0', 
                page = [
                    {"etag":"...","evaluationId":"...","id":"...","limits":[{"limitType":"TOTAL","maximumSubmissions":12345},{"limitType":"WEEKLY","maximumSubmissions":12345}],"roundEnd":"12345","roundStart":"12345"}
                    ]
            )
        else :
            return EvaluationRoundListResponse(
        )

    def testEvaluationRoundListResponse(self):
        """Test EvaluationRoundListResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
