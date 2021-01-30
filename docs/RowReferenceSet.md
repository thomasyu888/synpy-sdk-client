# RowReferenceSet

Represents a set of RowReferences of a TableEntity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **str** | When a RowReferenceSet is returned from a table update, this will be set to the current etag of the table. | [optional] 
**headers** | [**list[SelectColumn]**](SelectColumn.md) | The list of ColumnModels ID that describes the rows of this set. | [optional] 
**rows** | [**list[RowReference]**](RowReference.md) | Each RowReference of this list refers to a single version of a single row of a TableEntity. | [optional] 
**table_id** | **str** | The ID of the TableEntity than owns these rows | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


