# JsonSchemaVersionInfo

Information about a single version of a JSON schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The full &#39;$id&#39; of this schema version  | [optional] 
**created_by** | **str** | The ID of the user that created this JSON schema version. | [optional] 
**created_on** | **str** | The date this JSON schema version was created. | [optional] 
**json_sha256_hex** | **str** | The SHA-256 hexadecimal hash of the UTF-8 encoded JSON schema. | [optional] 
**organization_id** | **str** | The Synapse issued numeric identifier for the organization. | [optional] 
**organization_name** | **str** | The name of the organization to which this schema belongs. | [optional] 
**schema_id** | **str** | The Synapse issued numeric identifier for the schema. | [optional] 
**schema_name** | **str** | The name of the this schema. | [optional] 
**semantic_version** | **str** | The semantic version label provided when this version was created. Can be null if a semantic version was not provided when this version was created.  | [optional] 
**version_id** | **str** | The Synapse issued numeric identifier for this version. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


