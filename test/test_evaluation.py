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
from synclient.models.evaluation import Evaluation  # noqa: E501
from synclient.rest import ApiException

class TestEvaluation(unittest.TestCase):
    """Evaluation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Evaluation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.evaluation.Evaluation()  # noqa: E501
        if include_optional :
            return Evaluation(
                content_source = '0', 
                created_on = '0', 
                description = '0', 
                etag = '0', 
                id = '0', 
                name = '0', 
                owner_id = '0', 
                quota = {"firstRoundStart":"33333333","numberOfRounds":1,"roundDurationMillis":12345,"submissionLimit":2}, 
                status = 'PLANNED', 
                submission_instructions_message = '0', 
                submission_receipt_message = '0'
            )
        else :
            return Evaluation(
        )

    def testEvaluation(self):
        """Test Evaluation"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
