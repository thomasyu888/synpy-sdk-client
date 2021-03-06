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
from synclient.models.paginated_results_of_submission_status import PaginatedResultsOfSubmissionStatus  # noqa: E501
from synclient.rest import ApiException

class TestPaginatedResultsOfSubmissionStatus(unittest.TestCase):
    """PaginatedResultsOfSubmissionStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedResultsOfSubmissionStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.paginated_results_of_submission_status.PaginatedResultsOfSubmissionStatus()  # noqa: E501
        if include_optional :
            return PaginatedResultsOfSubmissionStatus(
                results = [
                    {"annotations":{"doubleAnnos":[{"isPrivate":true,"key":"...","value":12345},{"isPrivate":true,"key":"...","value":12345}],"longAnnos":[{"isPrivate":true,"key":"...","value":12345},{"isPrivate":true,"key":"...","value":12345}],"objectId":"...","scopeId":"...","stringAnnos":[{"isPrivate":true,"key":"...","value":"..."},{"isPrivate":true,"key":"...","value":"..."}],"version":12345},"canCancel":true,"cancelRequested":true,"entityId":"...","etag":"...","id":"...","modifiedOn":"12345","status":"ACCEPTED","statusVersion":12345,"submissionAnnotations":{"annotations":{"property1":{"type":"TIMESTAMP_MS","value":["...","..."]},"property2":{"type":"TIMESTAMP_MS","value":["...","..."]}},"etag":"...","id":"..."},"versionNumber":12345}
                    ], 
                total_number_of_results = 56
            )
        else :
            return PaginatedResultsOfSubmissionStatus(
        )

    def testPaginatedResultsOfSubmissionStatus(self):
        """Test PaginatedResultsOfSubmissionStatus"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
