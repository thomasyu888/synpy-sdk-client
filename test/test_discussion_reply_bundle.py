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
from synclient.models.discussion_reply_bundle import DiscussionReplyBundle  # noqa: E501
from synclient.rest import ApiException

class TestDiscussionReplyBundle(unittest.TestCase):
    """DiscussionReplyBundle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DiscussionReplyBundle
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.discussion_reply_bundle.DiscussionReplyBundle()  # noqa: E501
        if include_optional :
            return DiscussionReplyBundle(
                created_by = '0', 
                created_on = '0', 
                etag = '0', 
                forum_id = '0', 
                id = '0', 
                is_deleted = True, 
                is_edited = True, 
                message_key = '0', 
                modified_on = '0', 
                project_id = '0', 
                thread_id = '0'
            )
        else :
            return DiscussionReplyBundle(
        )

    def testDiscussionReplyBundle(self):
        """Test DiscussionReplyBundle"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
