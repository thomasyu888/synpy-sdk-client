# TeamMembershipStatus

JSON schema for the possible status of a User with respect to Team membership.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_join** | **bool** | true if and only if the user requesting this status information can join the user to the team | [optional] 
**can_send_email** | **bool** | true if and only if the user can send an email to the team | [optional] 
**has_open_invitation** | **bool** | true if and only if the user has an open invitation to join the team | [optional] 
**has_open_request** | **bool** | true if and only if the user has an open request to join the team | [optional] 
**has_unmet_access_requirement** | **bool** | true if and only if there is at least one unmet access requirement for the user on the team | [optional] 
**is_member** | **bool** | true if and only if the user is a member of the team | [optional] 
**membership_approval_required** | **bool** | true if and only if team admin approval is required for the user to join the team | [optional] 
**team_id** | **str** | The id of the Team. | [optional] 
**user_id** | **str** | The principal id of the user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


