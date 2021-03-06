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
from synclient.models.paginated_results_of_evaluation_all_of import PaginatedResultsOfEvaluationAllOf  # noqa: E501
from synclient.rest import ApiException

class TestPaginatedResultsOfEvaluationAllOf(unittest.TestCase):
    """PaginatedResultsOfEvaluationAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedResultsOfEvaluationAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.paginated_results_of_evaluation_all_of.PaginatedResultsOfEvaluationAllOf()  # noqa: E501
        if include_optional :
            return PaginatedResultsOfEvaluationAllOf(
                access_type = '0', 
                active_only = '0', 
                evaluation_ids = '0', 
                results = [
                    {"contentSource":"syn234444","createdOn":"12345","description":"Evaluation Queue","etag":"aaaaa","id":"12345","name":"Test Evaluation","ownerId":"22222","quota":{"firstRoundStart":"12345","numberOfRounds":12345,"roundDurationMillis":12345,"submissionLimit":12345},"status":"PLANNED","submissionInstructionsMessage":"Instructions","submissionReceiptMessage":"Received"}
                    ], 
                total_number_of_results = 56
            )
        else :
            return PaginatedResultsOfEvaluationAllOf(
        )

    def testPaginatedResultsOfEvaluationAllOf(self):
        """Test PaginatedResultsOfEvaluationAllOf"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
