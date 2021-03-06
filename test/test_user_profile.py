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
from synclient.models.user_profile import UserProfile  # noqa: E501
from synclient.rest import ApiException

class TestUserProfile(unittest.TestCase):
    """UserProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.user_profile.UserProfile()  # noqa: E501
        if include_optional :
            return UserProfile(
                r_studio_url = '0', 
                company = '0', 
                created_on = '0', 
                display_name = '0', 
                email = '0', 
                emails = [
                    '0'
                    ], 
                etag = '0', 
                first_name = '0', 
                industry = '0', 
                last_name = '0', 
                location = '0', 
                notification_settings = {"markEmailedMessagesAsRead":true,"sendEmailNotifications":true}, 
                open_ids = [
                    '0'
                    ], 
                owner_id = '0', 
                position = '0', 
                preferences = [
                    {"concreteType":"...","name":"..."}
                    ], 
                profile_picure_file_handle_id = '0', 
                summary = '0', 
                team_name = '0', 
                url = '0', 
                user_name = '0'
            )
        else :
            return UserProfile(
        )

    def testUserProfile(self):
        """Test UserProfile"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
