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
from synclient.models.question import Question  # noqa: E501
from synclient.rest import ApiException

class TestQuestion(unittest.TestCase):
    """Question unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Question
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.question.Question()  # noqa: E501
        if include_optional :
            return Question(
                concrete_type = '0', 
                doc_link = '0', 
                help_text = '0', 
                prompt = '0', 
                question_index = 56, 
                reference = {"ownerObjectId":"...","ownerObjectType":"ORGANIZATION","wikiPageId":"..."}
            )
        else :
            return Question(
        )

    def testQuestion(self):
        """Test Question"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
