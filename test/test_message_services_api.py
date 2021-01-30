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
from synclient.api.message_services_api import MessageServicesApi  # noqa: E501
from synclient.rest import ApiException


class TestMessageServicesApi(unittest.TestCase):
    """MessageServicesApi unit test stubs"""

    def setUp(self):
        self.api = synclient.api.message_services_api.MessageServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_send_message_to_entity_owner(self):
        """Test case for send_message_to_entity_owner

        Adds the owner of the given entity as an additional recipient of the message.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()