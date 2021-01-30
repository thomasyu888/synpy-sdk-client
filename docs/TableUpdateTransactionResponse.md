# TableUpdateTransactionResponse

An AsynchronousResponseBody returned from a table update transaction.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_type** | **str** | Concrete Type | [optional] 
**results** | [**list[TableUpdateResponse]**](TableUpdateResponse.md) | List of responses. There will be one response for each request in the transaction. | [optional] 
**snapshot_version_number** | **float** | The version number of the snapshot. Returned only, if a new snapshot was requested. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


