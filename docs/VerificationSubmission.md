# VerificationSubmission

User info submitted for verification by Synapse ACT
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attachments** | [**list[AttachmentMetadata]**](AttachmentMetadata.md) | Metadata of Files attached to the submission. The list will be emptied after the state is APPROVED or REJECTED.  | [optional] 
**company** | **str** | This person&#39;s current affiliation  | [optional] 
**created_by** | **str** | The principal ID of the user requesting verification | [optional] 
**created_on** | **str** | The date and time this object was created | [optional] 
**emails** | **list[str]** | The list of user email addresses registered to this user. | [optional] 
**first_name** | **str** | This person&#39;s given name (forename)  | [optional] 
**id** | **str** | The ID of this object | [optional] 
**last_name** | **str** | This person&#39;s family name (surname)  | [optional] 
**location** | **str** | This person&#39;s location  | [optional] 
**notification_email** | **str** | The primary (notification) email address registered to this user. | [optional] 
**orcid** | **str** | The user&#39;s ORCID URI  | [optional] 
**state_history** | [**list[VerificationState]**](VerificationState.md) | List of state changes the submission has passed through, ordered by time. The last in the list contains the current state of the submission.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


