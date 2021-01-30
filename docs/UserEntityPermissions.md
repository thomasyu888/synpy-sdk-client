# UserEntityPermissions

The permission a User has for a given Entity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_add_child** | **bool** | Can the user add a child entity to this entity? | [optional] 
**can_certified_user_add_child** | **bool** | Can the user add a child entity to this entity once they become a Certified User? | [optional] 
**can_certified_user_edit** | **bool** | Can the user edit this entity once they become a Certified User? | [optional] 
**can_change_permissions** | **bool** | Can the user change the permissions of this entity? | [optional] 
**can_change_settings** | **bool** | Can the user change the settings of this entity? | [optional] 
**can_delete** | **bool** | Can the user delete this entity? | [optional] 
**can_download** | **bool** | Are there any access requirements precluding the user from downloading this entity? | [optional] 
**can_edit** | **bool** | Can the user edit this entity? | [optional] 
**can_enable_inheritance** | **bool** | Can the user delete the entity&#39;s access control list (so it inherits settings from an ancestor)?&#39;  | [optional] 
**can_moderate** | **bool** | Can the user moderate the forum associated with this entity? Note that only project entity has forum. | [optional] 
**can_public_read** | **bool** | Is this entity considered public? | [optional] 
**can_upload** | **bool** | Are there any access requirements precluding the user from uploading into this entity (folder or project)? | [optional] 
**can_view** | **bool** | Can the user view this entity? | [optional] 
**is_certification_required** | **bool** | Is the certification requirement enabled for the project of the entity? | [optional] 
**is_certified_user** | **bool** | Is this user certified? | [optional] 
**owner_principal_id** | **float** | The principal ID of the entity&#39;s owner (i.e. the entity&#39;s &#39;createdBy&#39;)&#39;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


