"""
    Platform Repository Service

    Platform Repository Service - Sage Bionetworks Platform   # noqa: E501

    The version of the OpenAPI document: develop-SNAPSHOT
    Contact: thomas.yu@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import synclient
from synclient.model.accessor_change import AccessorChange
from synclient.model.research_project import ResearchProject
from synclient.model.restrictable_object_type import RestrictableObjectType
from synclient.model.submission_state import SubmissionState
globals()['AccessorChange'] = AccessorChange
globals()['ResearchProject'] = ResearchProject
globals()['RestrictableObjectType'] = RestrictableObjectType
globals()['SubmissionState'] = SubmissionState
from synclient.model.submission import Submission


class TestSubmission(unittest.TestCase):
    """Submission unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSubmission(self):
        """Test Submission"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Submission()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
