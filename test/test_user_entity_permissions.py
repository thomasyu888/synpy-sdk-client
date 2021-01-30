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
from synclient.models.user_entity_permissions import UserEntityPermissions  # noqa: E501
from synclient.rest import ApiException

class TestUserEntityPermissions(unittest.TestCase):
    """UserEntityPermissions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserEntityPermissions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.user_entity_permissions.UserEntityPermissions()  # noqa: E501
        if include_optional :
            return UserEntityPermissions(
                can_add_child = True, 
                can_certified_user_add_child = True, 
                can_certified_user_edit = True, 
                can_change_permissions = True, 
                can_change_settings = True, 
                can_delete = True, 
                can_download = True, 
                can_edit = True, 
                can_enable_inheritance = True, 
                can_moderate = True, 
                can_public_read = True, 
                can_upload = True, 
                can_view = True, 
                is_certification_required = True, 
                is_certified_user = True, 
                owner_principal_id = 1.337
            )
        else :
            return UserEntityPermissions(
        )

    def testUserEntityPermissions(self):
        """Test UserEntityPermissions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
