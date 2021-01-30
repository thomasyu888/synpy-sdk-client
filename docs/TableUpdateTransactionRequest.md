# TableUpdateTransactionRequest

An AsynchronousRequestBody to used make multiple changes to a table as a single 'transaction'. All changes will either succeed or fail as a unit. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**[TableUpdateRequest]**](TableUpdateRequest.md) | List of changes that describes schema and/or row changes to a table. | [optional] 
**concrete_type** | **str** | Concrete Type | [optional] 
**create_snapshot** | **bool** | When set to &#39;true&#39;, a snapshot of the table will be created after the change from this transaction request are applied to the table.  | [optional] 
**entity_id** | **str** | Entity Id | [optional] 
**snapshot_options** | [**SnapshotRequest**](SnapshotRequest.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


