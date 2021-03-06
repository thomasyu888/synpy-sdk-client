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
from synclient.models.entity_bundle_v2 import EntityBundleV2  # noqa: E501
from synclient.rest import ApiException

class TestEntityBundleV2(unittest.TestCase):
    """EntityBundleV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EntityBundleV2
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = synclient.models.entity_bundle_v2.EntityBundleV2()  # noqa: E501
        if include_optional :
            return EntityBundleV2(
                access_control_list = {"createdBy":"...","creationDate":"12345","etag":"...","id":"...","modifiedBy":"...","modifiedOn":"12345","resourceAccess":[{"accessType":["UPDATE_SUBMISSION","CHANGE_PERMISSIONS"],"principalId":12345},{"accessType":["UPDATE","SEND_MESSAGE"],"principalId":12345}]}, 
                annotations = {"annotations":{"property1":{"type":"STRING","value":["...","..."]},"property2":{"type":"STRING","value":["...","..."]}},"etag":"...","id":"..."}, 
                benefactor_acl = {"createdBy":"...","creationDate":"12345","etag":"...","id":"...","modifiedBy":"...","modifiedOn":"12345","resourceAccess":[{"accessType":["UPDATE_SUBMISSION","CHANGE_PERMISSIONS"],"principalId":12345},{"accessType":["UPDATE","SEND_MESSAGE"],"principalId":12345}]}, 
                doi_association = {"associatedBy":"...","associatedOn":"...","associationId":"...","doiUri":"...","doiUrl":"...","etag":"...","objectId":"...","objectType":"WIKI","objectVersion":12345,"updatedBy":"...","updatedOn":"..."}, 
                entity = {"concreteType":"...","createdBy":"...","createdOn":"...","description":"...","etag":"...","id":"...","modifiedBy":"...","modifiedOn":"...","name":"Trial ' + (_) . 09","parentId":"..."}, 
                entity_type = 'project', 
                file_handles = [
                    {"concreteType":"...","contentMd5":"...","contentSize":12345,"contentType":"...","createdBy":"...","createdOn":"...","etag":"...","fileName":"...","id":"...","storageLocationId":12345}
                    ], 
                file_name = '0', 
                has_children = True, 
                path = {"path":[{"benefactorId":12345,"createdBy":"...","createdOn":"...","id":"...","modifiedBy":"...","modifiedOn":"...","name":"...","type":"...","versionLabel":"...","versionNumber":12345},{"benefactorId":12345,"createdBy":"...","createdOn":"...","id":"...","modifiedBy":"...","modifiedOn":"...","name":"...","type":"...","versionLabel":"...","versionNumber":12345}]}, 
                permissions = {"canAddChild":true,"canCertifiedUserAddChild":true,"canCertifiedUserEdit":true,"canChangePermissions":true,"canChangeSettings":true,"canDelete":true,"canDownload":true,"canEdit":true,"canEnableInheritance":true,"canModerate":true,"canPublicRead":true,"canUpload":true,"canView":true,"isCertificationRequired":true,"isCertifiedUser":true,"ownerPrincipalId":12345}, 
                restriction_information = {"hasUnmetAccessRequirement":true,"restrictionLevel":"CONTROLLED_BY_ACT"}, 
                root_wiki_id = '0', 
                table_bundle = {"columnModels":[{"columnType":"EVALUATIONID","defaultValue":"...","enumValues":["...","..."],"facetType":"enumeration","id":"...","maximumListLength":100,"maximumSize":12345,"name":"..."},{"columnType":"STRING","defaultValue":"...","enumValues":["...","..."],"facetType":"range","id":"...","maximumListLength":100,"maximumSize":12345,"name":"..."}],"maxRowsPerPage":12345}, 
                thread_count = 1.337
            )
        else :
            return EntityBundleV2(
        )

    def testEntityBundleV2(self):
        """Test EntityBundleV2"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
