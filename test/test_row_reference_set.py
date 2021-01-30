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
from synclient.models.row_reference_set import RowReferenceSet  # noqa: E501
from synclient.rest import ApiException

class TestRowReferenceSet(unittest.TestCase):
    """RowReferenceSet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RowReferenceSet
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.row_reference_set.RowReferenceSet()  # noqa: E501
        if include_optional :
            return RowReferenceSet(
                etag = '0', 
                headers = [
                    {"columnType":"BOOLEAN","id":"...","name":"..."}
                    ], 
                rows = [
                    {"rowId":12345,"versionNumber":12345}
                    ], 
                table_id = '0'
            )
        else :
            return RowReferenceSet(
        )

    def testRowReferenceSet(self):
        """Test RowReferenceSet"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()