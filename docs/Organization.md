# Organization

The first step in creating new type schema in Synapse is to setup and configure an organization. The name of the organization serves as the root for each schema's $id managed by that organization. The organization name 'org.sagebionetworks' is reserved for the core Synapse model objects. Each organization also has an Access Control List (ACL) that controls who can add schemas to an organization. All schemas created under an Organization will be considered publicly readable and reference-able. Organizations are immutable 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The ID of the user that created this Organization. | [optional] 
**created_on** | **str** | The date this Organization was created. | [optional] 
**id** | **str** | The Synapse identifier issued to the Organization. | [optional] 
**name** | **str** | The name of the organization servers as the root for each schema&#39;s $id managed under an organization, and each name must be unique.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


