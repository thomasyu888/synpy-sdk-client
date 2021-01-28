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
from synclient.models.trashed_entity import TrashedEntity  # noqa: E501
from synclient.rest import ApiException

class TestTrashedEntity(unittest.TestCase):
    """TrashedEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TrashedEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.trashed_entity.TrashedEntity()  # noqa: E501
        if include_optional :
            return TrashedEntity(
                deleted_by_principal_id = '0', 
                deleted_on = '0', 
                entity_id = '0', 
                entity_name = '0', 
                original_parent_id = '0'
            )
        else :
            return TrashedEntity(
        )

    def testTrashedEntity(self):
        """Test TrashedEntity"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
