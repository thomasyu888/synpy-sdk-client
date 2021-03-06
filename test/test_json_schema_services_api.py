"""
    Platform Repository Service

    Platform Repository Service - Sage Bionetworks Platform   # noqa: E501

    The version of the OpenAPI document: develop-SNAPSHOT
    Contact: thomas.yu@sagebionetworks.org
    Generated by: https://openapi-generator.tech
"""


import unittest

import synclient
from synclient.api.json_schema_services_api import JsonSchemaServicesApi  # noqa: E501


class TestJsonSchemaServicesApi(unittest.TestCase):
    """JsonSchemaServicesApi unit test stubs"""

    def setUp(self):
        self.api = JsonSchemaServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_organziation(self):
        """Test case for create_organziation

        Create a new Organization.  # noqa: E501
        """
        pass

    def test_create_schema_async_get(self):
        """Test case for create_schema_async_get

        Get the results of an asynchronous job that was started to create a new JSON schema.   # noqa: E501
        """
        pass

    def test_create_schema_async_start(self):
        """Test case for create_schema_async_start

        Start an asynchronous job to create a new JSON schema.  # noqa: E501
        """
        pass

    def test_delete_json_schema(self):
        """Test case for delete_json_schema

        """
        pass

    def test_delete_organization(self):
        """Test case for delete_organization

        Delete the identified Organization.  # noqa: E501
        """
        pass

    def test_get_json_schema(self):
        """Test case for get_json_schema

        Get a registered JSON schema using its $id.  # noqa: E501
        """
        pass

    def test_get_organization_acl(self):
        """Test case for get_organization_acl

        Get the ACL associated of an Organization.  # noqa: E501
        """
        pass

    def test_get_organization_by_name(self):
        """Test case for get_organization_by_name

        Lookup an Organization by name.  # noqa: E501
        """
        pass

    def test_get_validation_schema_results(self):
        """Test case for get_validation_schema_results

        Get the results of an asynchronous job that was started to compile a 'validation' schema for a JSON schema.   # noqa: E501
        """
        pass

    def test_list_json_schemas(self):
        """Test case for list_json_schemas

        List all JSON schemas for an Organization.  # noqa: E501
        """
        pass

    def test_list_json_schemas_versions(self):
        """Test case for list_json_schemas_versions

        List the version information for each version of a given schema.  # noqa: E501
        """
        pass

    def test_list_organizations(self):
        """Test case for list_organizations

        List all organizations.  # noqa: E501
        """
        pass

    def test_start_get_validation_schema(self):
        """Test case for start_get_validation_schema

        Start validating JSON schema   # noqa: E501
        """
        pass

    def test_update_organization_acl(self):
        """Test case for update_organization_acl

        Update the AccessControlList (ACL) for the identified Organization.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
