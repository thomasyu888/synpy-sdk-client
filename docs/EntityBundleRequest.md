# EntityBundleRequest

Specifies what fields to include in an EntityBundle
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_access_control_list** | **bool** | Include the AccessControlList for this Entity | [optional] 
**include_annotations** | **bool** | Include Annotations associated with the Entity in the response. | [optional] 
**include_benefactor_acl** | **bool** | Include the ACL of the Entity from which this Entity inherits its AccessControlList | [optional] 
**include_doi_association** | **bool** | Include DOIs associated with this Entity | [optional] 
**include_entity** | **bool** | Include the Entity in the response. | [optional] 
**include_entity_path** | **bool** | Include EntityHeaders for all Entities in this Entity&#39;s path  | [optional] 
**include_file_handles** | **bool** | Include all FileHandles associated with this Entity. | [optional] 
**include_file_name** | **bool** | If this Entity is a FileEntity, include its filename | [optional] 
**include_has_children** | **bool** | Include boolean indicating whether this Entity has children | [optional] 
**include_permissions** | **bool** | Include permissions of the current user on the entity. | [optional] 
**include_restriction_information** | **bool** | Include the RestrictionLevel of this Entity | [optional] 
**include_root_wiki_id** | **bool** | Include the id of the root Wiki associated with this Entity | [optional] 
**include_table_bundle** | **bool** | If the Entity is a TableEntity, include Table specific metadata. | [optional] 
**include_thread_count** | **bool** | Include the number of discussion threads that mention this Entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


