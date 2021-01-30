# QueryBundleRequest

Query Bundle Request
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_type** | **str** | Concrete Type | [optional] 
**entity_id** | **str** | Entity Id | [optional] 
**part_mask** | **int** | Optional, default all. The &#39;partsMask&#39; is an integer mask that can be combined into to request any desired part. The mask is defined as follows: * Query Results (queryResults) &#x3D; 0x1 * Query Count (queryCount) &#x3D; 0x2 * Select Columns (selectColumns) &#x3D; 0x4 * Max Rows Per Page (maxRowsPerPage) &#x3D; 0x8 * The Table Columns (columnModels) &#x3D; 0x10 * Facet statistics for each faceted column (facetStatistics) &#x3D; 0x20 * The sum of the file sizes (sumFileSizesBytes) &#x3D; 0x40  | [optional] 
**query** | [**Query**](Query.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


