# TeamSubmissionEligibility

Describes the eligibility of a Challenge Team to submit to an Evalution queue, reflecting the queue's submission quotas and current submissions. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eligibility_state_hash** | **int** | A hash of this object, used for optimistic concurrency. | [optional] 
**evaluation_id** | **str** | The ID of the Evaluation of interest | [optional] 
**members_eligibility** | [**list[MemberSubmissionEligibility]**](MemberSubmissionEligibility.md) | Describes the submission eligibility of the contributors to the Submission. | [optional] 
**team_eligibility** | [**SubmissionEligibility**](SubmissionEligibility.md) |  | [optional] 
**team_id** | **str** | The ID of the Team of interest | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


