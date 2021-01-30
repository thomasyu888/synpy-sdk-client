# ListRequest

Request for a list of FormData matching the provided filters.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_by_state** | [**[StateEnum]**](StateEnum.md) | Only return results with a state that matches elements from this set. Required. Must include at least one element.  | [optional] 
**group_id** | **str** | The group identifier. Required. | [optional] 
**next_page_token** | **str** | The results are automatically paginated. To get the next page, forward the nextPageToken returned from the last request.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


