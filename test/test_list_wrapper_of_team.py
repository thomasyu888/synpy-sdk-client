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
from synclient.models.list_wrapper_of_team import ListWrapperOfTeam  # noqa: E501
from synclient.rest import ApiException

class TestListWrapperOfTeam(unittest.TestCase):
    """ListWrapperOfTeam unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ListWrapperOfTeam
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.list_wrapper_of_team.ListWrapperOfTeam()  # noqa: E501
        if include_optional :
            return ListWrapperOfTeam(
                list = [
                    {"canPublicJoin":true,"createdBy":"...","createdOn":"...","description":"...","etag":"...","icon":"...","id":"...","modifiedBy":"...","modifiedOn":"...","name":"..."}
                    ]
            )
        else :
            return ListWrapperOfTeam(
        )

    def testListWrapperOfTeam(self):
        """Test ListWrapperOfTeam"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
