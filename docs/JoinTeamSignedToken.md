# JoinTeamSignedToken

Signed token containing the information needed to join a new user to a team.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concrete_type** | **str** | Concrete Type | [optional] 
**created_on** | **str** | The date-time the token was generated. | [optional] 
**expires_on** | **str** | The date-time when this token expires. | [optional] 
**hmac** | **str** | The hash message authentication code for the message. | [optional] 
**member_id** | **str** | The ID of the new team member. | [optional] 
**team_id** | **str** | The ID of the team which the user was invited to join. | [optional] 
**user_id** | **str** | The ID of the user who is acting to add the new member to the Team. The HMAC in the token authenticates that the request is being made by this user.&#39;  | [optional] 
**version** | **int** | The version of the key used to generate the HMAC. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


