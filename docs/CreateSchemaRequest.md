# CreateSchemaRequest

An AsynchronousRequestBody to define a new JsonSchema.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_type** | **str** | Concrete Type | [optional] 
**dry_run** | **bool** | When true, an attempt will be made to create the schema normally, but the resulting schema will not be retained. This can be used to validate a schema without actually registering it. The default value is false.  | [optional] 
**schema** | [**JsonSchema**](JsonSchema.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


