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
from synclient.models.paginated_results_of_access_requirement import PaginatedResultsOfAccessRequirement  # noqa: E501
from synclient.rest import ApiException

class TestPaginatedResultsOfAccessRequirement(unittest.TestCase):
    """PaginatedResultsOfAccessRequirement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatedResultsOfAccessRequirement
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.paginated_results_of_access_requirement.PaginatedResultsOfAccessRequirement()  # noqa: E501
        if include_optional :
            return PaginatedResultsOfAccessRequirement(
                results = [
                    {"accessType":"SUBMIT","concreteType":"...","createdBy":"...","createdOn":"...","description":"...","etag":"...","id":12345,"modifiedBy":"...","modifiedOn":"...","subjectIds":[{"id":"...","type":"EVALUATION"},{"id":"...","type":"TEAM"}],"versionNumber":12345}
                    ], 
                total_number_of_results = 56
            )
        else :
            return PaginatedResultsOfAccessRequirement(
        )

    def testPaginatedResultsOfAccessRequirement(self):
        """Test PaginatedResultsOfAccessRequirement"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
