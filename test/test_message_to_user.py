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
from synclient.models.message_to_user import MessageToUser  # noqa: E501
from synclient.rest import ApiException

class TestMessageToUser(unittest.TestCase):
    """MessageToUser unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MessageToUser
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.message_to_user.MessageToUser()  # noqa: E501
        if include_optional :
            return MessageToUser(
                bcc = '0', 
                cc = '0', 
                created_by = '0', 
                created_on = '0', 
                file_handle_id = '0', 
                id = '0', 
                in_reply_to = '0', 
                in_reply_to_root = '0', 
                is_notification_message = True, 
                notification_unsubscribe_endpoint = '0', 
                recipients = [
                    '0'
                    ], 
                subject = '0', 
                to = '0', 
                user_profile_setting_endpoint = '0', 
                with_profile_setting_link = True, 
                with_unsubscribe_link = True
            )
        else :
            return MessageToUser(
        )

    def testMessageToUser(self):
        """Test MessageToUser"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()