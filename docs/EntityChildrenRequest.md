# EntityChildrenRequest

Request for EntityHeaders of the children of a given parent Entity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_sum_file_sizes** | **bool** | When true, the sum of the files sizes (bytes) with the given parentId and types will be included. False by default | [optional] [default to False]
**include_total_child_count** | **bool** | When true, the total number of children with the givenparentId and types will be included. False by default | [optional] [default to False]
**include_types** | [**list[EntityType]**](EntityType.md) | The types of children to be include. Must include at least one type. | [optional] 
**next_page_token** | **str** | Optional parameter used to fetch the next page of results. When NULL, the first page will be returned. The nextPageToken is provided with the results if there is another page of results. | [optional] 
**parent_id** | **str** | The ID of the parent. Set to null to list projects. | [optional] 
**sort_by** | [**SortBy**](SortBy.md) |  | [optional] 
**sort_direction** | [**SortDirection**](SortDirection.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


