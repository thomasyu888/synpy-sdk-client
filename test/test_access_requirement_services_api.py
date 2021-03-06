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

import synclient
from synclient.api.access_requirement_services_api import AccessRequirementServicesApi  # noqa: E501
from synclient.rest import ApiException


class TestAccessRequirementServicesApi(unittest.TestCase):
    """AccessRequirementServicesApi unit test stubs"""

    def setUp(self):
        self.api = synclient.api.access_requirement_services_api.AccessRequirementServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_team_access_requirements(self):
        """Test case for get_team_access_requirements

        Retrieve paginated list of ALL Access Requirements associated with a Team.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
