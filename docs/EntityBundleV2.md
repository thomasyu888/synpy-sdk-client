# EntityBundleV2

Bundle to transport an Entity and related data objects
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_control_list** | [**AccessControlList**](AccessControlList.md) |  | [optional] 
**annotations** | [**AnnotationsV2**](AnnotationsV2.md) |  | [optional] 
**benefactor_acl** | [**AccessControlList**](AccessControlList.md) |  | [optional] 
**doi_association** | [**DoiAssociation**](DoiAssociation.md) |  | [optional] 
**entity** | [**Entity**](Entity.md) |  | [optional] 
**entity_type** | [**EntityType**](EntityType.md) |  | [optional] 
**file_handles** | [**[FileHandle]**](FileHandle.md) | FileHandles associated with this Entity | [optional] 
**file_name** | **str** | If this Entity is a FileEntity, this is its filename | [optional] 
**has_children** | **bool** | Whether or not this Entity has children | [optional] 
**path** | [**EntityPath**](EntityPath.md) |  | [optional] 
**permissions** | [**UserEntityPermissions**](UserEntityPermissions.md) |  | [optional] 
**restriction_information** | [**RestrictionInformationResponse**](RestrictionInformationResponse.md) |  | [optional] 
**root_wiki_id** | **str** | Id of the root Wiki associated with this Entity | [optional] 
**table_bundle** | [**TableBundle**](TableBundle.md) |  | [optional] 
**thread_count** | **float** | Number of disucssion threads that reference this Entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


