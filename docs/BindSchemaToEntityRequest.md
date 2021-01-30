# BindSchemaToEntityRequest

Request to bind an Entity to a JSON schema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** | The ID of the the entity. | [optional] 
**schemaid** | **str** | The $id of the JSON schema to bind to the entity. Note: If the $id includes a semantic version then entity will be bound to that specific version. If the $id excludes the semantic version then the entity will be bound to the latest version of that schema.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


