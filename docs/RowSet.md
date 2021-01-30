# RowSet

Represents a set of row of a TableEntity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_type** | **str** | Concrete Type | [optional] 
**etag** | **str** | Any RowSet returned from Synapse will contain the current etag of the change set. To update any rows from a RowSet the etag must be provided with the POST. | [optional] 
**headers** | [**[SelectColumn]**](SelectColumn.md) | The list of SelectColumns that describes the rows of this set. | [optional] 
**rows** | [**[RowTable]**](RowTable.md) | The Rows of this set. The index of each row value aligns with the index of each header. | [optional] 
**table_id** | **str** | The ID of the TableEntity than owns these rows | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


