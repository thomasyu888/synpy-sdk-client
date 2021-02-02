"""
    Platform Repository Service

    Platform Repository Service - Sage Bionetworks Platform   # noqa: E501

    The version of the OpenAPI document: develop-SNAPSHOT
    Contact: thomas.yu@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import synclient
from synclient.api.asynchronous_job_services_api import AsynchronousJobServicesApi  # noqa: E501


class TestAsynchronousJobServicesApi(unittest.TestCase):
    """AsynchronousJobServicesApi unit test stubs"""

    def setUp(self):
        self.api = AsynchronousJobServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_job_status(self):
        """Test case for get_job_status

        Get Asynchronous Job.  # noqa: E501
        """
        pass

    def test_launch_new_job(self):
        """Test case for launch_new_job

        Launch new Asynchronous jobs.  # noqa: E501
        """
        pass

    def test_stop_job(self):
        """Test case for stop_job

        Stop a Asynchronous Job.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()