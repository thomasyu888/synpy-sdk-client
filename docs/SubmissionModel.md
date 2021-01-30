# SubmissionModel

A Submission to a Synapse Evaluation is a pointer to a versioned Entity. Submissions are immutable, so we archive a copy of the EntityBundle at the time of submission. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributors** | [**[SubmissionContributor]**](SubmissionContributor.md) | User ids of the submitter and (if a team submission) the team members involved in creating the submission.  | [optional] 
**created_on** | **str** | The date on which Submission was created. | [optional] 
**docker_digest** | **str** | For Docker repositories, the digest from the commit. Null for other entity types. | [optional] 
**docker_repository_name** | **str** | For Docker repositories, the name of the submitted repository. Null for other entity types. | [optional] 
**entity_bundle_json** | **str** | The Bundled Entity and Annotations JSON at the time of submission. | [optional] 
**entity_id** | **str** | The Synapse ID of the Entity in this Submission. | [optional] 
**evaluation_id** | **str** | The Synapse ID of the Evaluation this Submission is for. | [optional] 
**evaluation_round_id** | **str** | The Synapse ID of the EvaluationRound to which this was submitted. DO NOT specify a value for this. It will be filled in automatically upon creation of the Submission if the Evaluation is configured with an EvaluationRound. | [optional] 
**id** | **str** | The unique, immutable Synapse ID of this Submission. | [optional] 
**name** | **str** | The title of this Submission. | [optional] 
**submitter_alias** | **str** | The alias for the user or team creating the submission. | [optional] 
**team_id** | **str** | optional Team which collaborated on the submission | [optional] 
**user_id** | **str** | The Synapse ID of the user who created this Submission. | [optional] 
**version_number** | **int** | The submitted version number of the Entity. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


