# PaginatedResultsOfMembershipInvitation

Retrieve the open invitations from a Team, optionally filtering by the invitee. An invitation is only open if it has not expired and if the user has not joined the Team. Note: certain fields may be omitted when returned if the field value is null 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**list[MembershipInvitation]**](MembershipInvitation.md) | The the id of the entity to which this reference refers | [optional] 
**total_number_of_results** | **int** | Calculating the actual totalNumberOfResults is not longer supported. Therefore, for each page, the totalNumberOfResults is estimated using the current page, limit, and offset. When the page size equals the limit, the totalNumberOfResults will be offset+pageSize+ 1. Otherwise, the totalNumberOfResults will be offset+pageSize.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


