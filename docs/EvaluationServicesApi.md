# synclient.EvaluationServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_evaluation**](EvaluationServicesApi.md#create_evaluation) | **POST** /evaluation | Creates a new Evaluation.
[**create_evaluation_round**](EvaluationServicesApi.md#create_evaluation_round) | **POST** /evaluation/{evalId}/round | Create Evaluation Round
[**create_submission**](EvaluationServicesApi.md#create_submission) | **POST** /evaluation/submission | Creates a Submission and sends a submission notification email to the submitter&#39;s team members. 
[**delete_acl**](EvaluationServicesApi.md#delete_acl) | **DELETE** /evaluation/{evalId}/acl | This method is deprecated and should be removed from future versions of the API.
[**delete_evaluation**](EvaluationServicesApi.md#delete_evaluation) | **DELETE** /evaluation/{evalId} | Deletes an Evaluation.
[**delete_evaluation_round**](EvaluationServicesApi.md#delete_evaluation_round) | **DELETE** /evaluation/{evalId}/round/{roundId} | Delete Evaluation Round
[**delete_submission**](EvaluationServicesApi.md#delete_submission) | **DELETE** /evaluation/submission/{subId} | Deletes a Submission and its accompanying SubmissionStatus.
[**find_evaluation**](EvaluationServicesApi.md#find_evaluation) | **GET** /evaluation/name/{name} | Finds an Evaluation by name.
[**get_acl**](EvaluationServicesApi.md#get_acl) | **GET** /evaluation/{evalId}/acl | Gets the access control list (ACL) governing the given evaluation.
[**get_all_evaluation_rounds**](EvaluationServicesApi.md#get_all_evaluation_rounds) | **POST** /evaluation/{evalId}/round/list | Get all rounds of an Evaluation
[**get_all_submission_bundles**](EvaluationServicesApi.md#get_all_submission_bundles) | **GET** /evaluation/{evalId}/submission/bundle/all | Gets a collection of bundled Submissions and SubmissionStatuses to a given Evaluation.
[**get_all_submission_statuses**](EvaluationServicesApi.md#get_all_submission_statuses) | **GET** /evaluation/{evalId}/submission/status/all | Gets a collection of SubmissionStatuses to a specified Evaluation.
[**get_all_submissions**](EvaluationServicesApi.md#get_all_submissions) | **GET** /evaluation/{evalId}/submission/all | Gets a collection of Submissions to a specified Evaluation.
[**get_available_evaluations_paginated**](EvaluationServicesApi.md#get_available_evaluations_paginated) | **GET** /evaluation/available | Gets a collection of Evaluations in which the user has SUBMIT permission, within a given range. 
[**get_evaluation**](EvaluationServicesApi.md#get_evaluation) | **GET** /evaluation/{evalId} | Gets an Evaluation.
[**get_evaluation_round**](EvaluationServicesApi.md#get_evaluation_round) | **GET** /evaluation/{evalId}/round/{roundId} | Get Evaluation Round
[**get_evaluations_by_content_source_paginated**](EvaluationServicesApi.md#get_evaluations_by_content_source_paginated) | **GET** /entity/{id}/evaluation | Gets Evaluations tied to a project.
[**get_evaluations_paginated**](EvaluationServicesApi.md#get_evaluations_paginated) | **GET** /evaluation | Gets a collection of Evaluations, within a given range.
[**get_my_submission_bundles**](EvaluationServicesApi.md#get_my_submission_bundles) | **GET** /evaluation/{evalId}/submission/bundle | Gets the requesting users bundled Submissions and SubmissionStatuses to a specified Evaluation.&#39; 
[**get_my_submissions**](EvaluationServicesApi.md#get_my_submissions) | **GET** /evaluation/{evalId}/submission | Gets the requesting user&#39;s Submissions to a specified Evaluation.
[**get_submission**](EvaluationServicesApi.md#get_submission) | **GET** /evaluation/submission/{subId} | Gets a Submission.
[**get_submission_count**](EvaluationServicesApi.md#get_submission_count) | **GET** /evaluation/{evalId}/submission/count | Gets the number of Submissions to a specified Evaluation.
[**get_submission_status**](EvaluationServicesApi.md#get_submission_status) | **GET** /evaluation/submission/{subId}/status | Gets the SubmissionStatus object associated with a specified Submission.
[**get_team_submission_eligibility**](EvaluationServicesApi.md#get_team_submission_eligibility) | **GET** /evaluation/{evalId}/team/{id}/SubmissionEligibility | Find out whether a Team and its members are eligible to submit to a given Evaluation queue (at the current time).&#39; 
[**has_access2**](EvaluationServicesApi.md#has_access2) | **GET** /evaluation/{evalId}/access | Determines whether a specified Synapse user has a certain access type on evaluation.
[**redirect_url_for_file_handle**](EvaluationServicesApi.md#redirect_url_for_file_handle) | **GET** /evaluation/submission/{subId}/file/{fileHandleId} | Gets a pre-signed URL to access a requested File contained within a specified Submission. 
[**request_to_cancel_submission**](EvaluationServicesApi.md#request_to_cancel_submission) | **PUT** /evaluation/submission/{subId}/cancellation | User requests to cancel their submission.
[**update_acl**](EvaluationServicesApi.md#update_acl) | **PUT** /evaluation/acl | Updates the supplied access control list (ACL) for an evaluation.
[**update_evaluation**](EvaluationServicesApi.md#update_evaluation) | **PUT** /evaluation/{evalId} | Updates an Evaluation.
[**update_evaluation_round**](EvaluationServicesApi.md#update_evaluation_round) | **PUT** /evaluation/{evalId}/round/{roundId} | Update Evaluation Round
[**update_submission_status**](EvaluationServicesApi.md#update_submission_status) | **PUT** /evaluation/submission/{subId}/status | Updates a SubmissionStatus object.
[**update_submission_status_batch**](EvaluationServicesApi.md#update_submission_status_batch) | **PUT** /evaluation/{evalId}/statusBatch | Update multiple SubmissionStatuses.


# **create_evaluation**
> Evaluation create_evaluation()

Creates a new Evaluation.

'Creates a new Evaluation. The passed request body should contain the following fields:  <ul>  <li>name - Give your new Evaluation a name.</li>  <li>contentSource - The ID of the parent Entity, such as a Folder or Project.</li>  <li>status - The initial state of the Evaluation, an  <a href=\"${org.sagebionetworks.evaluation.model.EvaluationStatus}\">EvaluationStatus</a></li>  </ul>  <p>  <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.CREATE</a> on the contentSource Entity.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.evaluation import Evaluation
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    evaluation = Evaluation(
        content_source="content_source_example",
        created_on="created_on_example",
        description="description_example",
        etag="etag_example",
        id="id_example",
        name="name_example",
        owner_id="owner_id_example",
        quota=SubmissionQuota(
            first_round_start="first_round_start_example",
            number_of_rounds=1,
            round_duration_millis=1,
            submission_limit=1,
        ),
        status=EvaluationStatus("PLANNED"),
        submission_instructions_message="submission_instructions_message_example",
        submission_receipt_message="submission_receipt_message_example",
    ) # Evaluation |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a new Evaluation.
        api_response = api_instance.create_evaluation(evaluation=evaluation)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->create_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **evaluation** | [**Evaluation**](Evaluation.md)|  | [optional]

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_evaluation_round**
> EvaluationRound create_evaluation_round(eval_id)

Create Evaluation Round

Create Evaluation Round

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.evaluation_round import EvaluationRound
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    evaluation_round = EvaluationRound(
        etag="etag_example",
        evaluation_id="evaluation_id_example",
        id="id_example",
        limits=[
            EvaluationRoundLimit(
                limit_type=EvaluationRoundLimitType("TOTAL"),
                maximum_submissions=1,
            ),
        ],
        round_end="round_end_example",
        round_start="round_start_example",
    ) # EvaluationRound |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create Evaluation Round
        api_response = api_instance.create_evaluation_round(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->create_evaluation_round: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Evaluation Round
        api_response = api_instance.create_evaluation_round(eval_id, evaluation_round=evaluation_round)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->create_evaluation_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **evaluation_round** | [**EvaluationRound**](EvaluationRound.md)|  | [optional]

### Return type

[**EvaluationRound**](EvaluationRound.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_submission**
> SubmissionModel create_submission()

Creates a Submission and sends a submission notification email to the submitter's team members. 

Creates a Submission and sends a submission notification email to the submitter's team members.  The passed request body should contain the following fields:  <ul>  <li>evaluationId - The ID of the Evaluation to which this Submission belongs.</li>  <li>entityId - The ID of the Entity being submitted.</li>  <li>versionNumber - The specific version of the Entity being submitted.</li>  </ul>  <p>  A Submission must be either a Team or an Individual submission.  A Team submission must include a Team ID in the teamId field and the request must include a submissionEligibilityHash request parameter.  A Team submission may also include a list of submission contributors. (The submitter is taken to be a contributor and need not be included in the list.) An individual submission must have a null teamId, a null or empty contributor list, and no submissionEligibilityHash parameter.  </p>  <p>  <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.SUBMIT</a>.  </p>  <p>  This call also creates an associated <a href=\"${org.sagebionetworks.evaluation.model.SubmissionStatus}\">SubmissionStatus</a>, initialized with a SubmissionStatusEnum value of RECEIVED.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.submission_model import SubmissionModel
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    challenge_endpoint = "challengeEndpoint_example" # str | The portal endpoint prefix to the an entity/challenge page. The entity ID of the challenge project is appended to create the complete URL. In normal operation, this parameter should be omitted.'  (optional)
    etag = "etag_example" # str | The current eTag of the Entity being submitted (optional)
    notification_unsubscribe_endpoint = "notificationUnsubscribeEndpoint_example" # str | The portal endpoint prefix for one-click email unsubscription. A signed, serialized token is appended to create the complete URL: <a href=\"${org.sagebionetworks.repo.model.message.NotificationSettingsSignedToken}\">NotificationSettingsSignedToken</a>. In normal operation, this parameter should be omitted.'  (optional)
    submission_eligibility_hash = "submissionEligibilityHash_example" # str | The hash provided by the <a href=\"${org.sagebionetworks.evaluation.model.TeamSubmissionEligibility}\">TeamSubmissionEligibility</a> object.  (optional)
    submission_model = SubmissionModel(
        contributors=[
            SubmissionContributor(
                created_on="created_on_example",
                principal_id="principal_id_example",
            ),
        ],
        created_on="created_on_example",
        docker_digest="docker_digest_example",
        docker_repository_name="docker_repository_name_example",
        entity_bundle_json="entity_bundle_json_example",
        entity_id="entity_id_example",
        evaluation_id="evaluation_id_example",
        evaluation_round_id="evaluation_round_id_example",
        id="id_example",
        name="name_example",
        submitter_alias="submitter_alias_example",
        team_id="team_id_example",
        user_id="user_id_example",
        version_number=1,
    ) # SubmissionModel |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates a Submission and sends a submission notification email to the submitter's team members. 
        api_response = api_instance.create_submission(challenge_endpoint=challenge_endpoint, etag=etag, notification_unsubscribe_endpoint=notification_unsubscribe_endpoint, submission_eligibility_hash=submission_eligibility_hash, submission_model=submission_model)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->create_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **challenge_endpoint** | **str**| The portal endpoint prefix to the an entity/challenge page. The entity ID of the challenge project is appended to create the complete URL. In normal operation, this parameter should be omitted.&#39;  | [optional]
 **etag** | **str**| The current eTag of the Entity being submitted | [optional]
 **notification_unsubscribe_endpoint** | **str**| The portal endpoint prefix for one-click email unsubscription. A signed, serialized token is appended to create the complete URL: &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.message.NotificationSettingsSignedToken}\&quot;&gt;NotificationSettingsSignedToken&lt;/a&gt;. In normal operation, this parameter should be omitted.&#39;  | [optional]
 **submission_eligibility_hash** | **str**| The hash provided by the &lt;a href&#x3D;\&quot;${org.sagebionetworks.evaluation.model.TeamSubmissionEligibility}\&quot;&gt;TeamSubmissionEligibility&lt;/a&gt; object.  | [optional]
 **submission_model** | [**SubmissionModel**](SubmissionModel.md)|  | [optional]

### Return type

[**SubmissionModel**](SubmissionModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_acl**
> delete_acl(eval_id)

This method is deprecated and should be removed from future versions of the API.

This method is deprecated and should be removed from future versions of the API.  Deletes the ACL (access control list) of the specified evaluation. The user should have the proper <a href=\"${org.sagebionetworks.evaluation.model.UserEvaluationPermissions}\">permissions</a> to delete the ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.

    # example passing only required values which don't have defaults set
    try:
        # This method is deprecated and should be removed from future versions of the API.
        api_instance.delete_acl(eval_id)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->delete_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_evaluation**
> delete_evaluation(eval_id)

Deletes an Evaluation.

Deletes an Evaluation.  <p>  <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.DELETE</a> on the specified Evaluation.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.

    # example passing only required values which don't have defaults set
    try:
        # Deletes an Evaluation.
        api_instance.delete_evaluation(eval_id)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->delete_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_evaluation_round**
> delete_evaluation_round(eval_id, round_id)

Delete Evaluation Round

Delete Evaluation Round

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    round_id = "roundId_example" # str | The ID of the evaluation round

    # example passing only required values which don't have defaults set
    try:
        # Delete Evaluation Round
        api_instance.delete_evaluation_round(eval_id, round_id)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->delete_evaluation_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **round_id** | **str**| The ID of the evaluation round |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resouce has been deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_submission**
> delete_submission(sub_id)

Deletes a Submission and its accompanying SubmissionStatus.

Deletes a Submission and its accompanying SubmissionStatus.  <b>This service is intended to only be used by ChallengesInfrastructure service account.</b>  <p>  <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.DELETE_SUBMISSION</a> on the specified Evaluation.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    sub_id = "subId_example" # str | The ID of the Submission

    # example passing only required values which don't have defaults set
    try:
        # Deletes a Submission and its accompanying SubmissionStatus.
        api_instance.delete_submission(sub_id)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->delete_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The ID of the Submission |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The resource has been deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_evaluation**
> Evaluation find_evaluation(name)

Finds an Evaluation by name.

Finds an Evaluation by name. <p> <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ</a> on the specified Evaluation. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.evaluation import Evaluation
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    name = "name_example" # str | The name of the desired Evaluation.

    # example passing only required values which don't have defaults set
    try:
        # Finds an Evaluation by name.
        api_response = api_instance.find_evaluation(name)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->find_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the desired Evaluation. |

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_acl**
> AccessControlList get_acl(eval_id)

Gets the access control list (ACL) governing the given evaluation.

Gets the access control list (ACL) governing the given evaluation. The user should have the proper <a href=\"${org.sagebionetworks.evaluation.model.UserEvaluationPermissions}\">permissions</a> to read the ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.access_control_list import AccessControlList
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.

    # example passing only required values which don't have defaults set
    try:
        # Gets the access control list (ACL) governing the given evaluation.
        api_response = api_instance.get_acl(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |

### Return type

[**AccessControlList**](AccessControlList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_evaluation_rounds**
> EvaluationRoundListResponse get_all_evaluation_rounds(eval_id)

Get all rounds of an Evaluation

Get all rounds of an Evaluation

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.evaluation_round_list_request import EvaluationRoundListRequest
from synclient.model.evaluation_round_list_response import EvaluationRoundListResponse
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    evaluation_round_list_request = EvaluationRoundListRequest(
        next_page_token="next_page_token_example",
    ) # EvaluationRoundListRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get all rounds of an Evaluation
        api_response = api_instance.get_all_evaluation_rounds(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_all_evaluation_rounds: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all rounds of an Evaluation
        api_response = api_instance.get_all_evaluation_rounds(eval_id, evaluation_round_list_request=evaluation_round_list_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_all_evaluation_rounds: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **evaluation_round_list_request** | [**EvaluationRoundListRequest**](EvaluationRoundListRequest.md)|  | [optional]

### Return type

[**EvaluationRoundListResponse**](EvaluationRoundListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submission_bundles**
> PaginatedResultsOfSubmissionBundle get_all_submission_bundles(eval_id)

Gets a collection of bundled Submissions and SubmissionStatuses to a given Evaluation.

Gets a collection of bundled Submissions and SubmissionStatuses to a given Evaluation.  <p> <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ_PRIVATE_SUBMISSION</a> on the specified Evaluation. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.paginated_results_of_submission_bundle import PaginatedResultsOfSubmissionBundle
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    limit = 10 # int | Limits the number of entities that will be fetched for this page. When null it will default to 10.'  (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  (optional) if omitted the server will use the default value of 0
    status = "status_example" # str | Submission Status (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a collection of bundled Submissions and SubmissionStatuses to a given Evaluation.
        api_response = api_instance.get_all_submission_bundles(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_all_submission_bundles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a collection of bundled Submissions and SubmissionStatuses to a given Evaluation.
        api_response = api_instance.get_all_submission_bundles(eval_id, limit=limit, offset=offset, status=status)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_all_submission_bundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **limit** | **int**| Limits the number of entities that will be fetched for this page. When null it will default to 10.&#39;  | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  | [optional] if omitted the server will use the default value of 0
 **status** | **str**| Submission Status | [optional]

### Return type

[**PaginatedResultsOfSubmissionBundle**](PaginatedResultsOfSubmissionBundle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submission_statuses**
> PaginatedResultsOfSubmissionStatus get_all_submission_statuses(eval_id)

Gets a collection of SubmissionStatuses to a specified Evaluation.

'Gets a collection of SubmissionStatuses to a specified Evaluation.  <p>  <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ</a> on the specified Evaluation. Furthermore, the caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ_PRIVATE_SUBMISSION</a> to see all data marked as \"private\" in the SubmissionStatuses.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.paginated_results_of_submission_status import PaginatedResultsOfSubmissionStatus
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    limit = 10 # int | Limits the number of entities that will be fetched for this page. When null it will default to 10.'  (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  (optional) if omitted the server will use the default value of 0
    status = "status_example" # str | Submission status (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a collection of SubmissionStatuses to a specified Evaluation.
        api_response = api_instance.get_all_submission_statuses(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_all_submission_statuses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a collection of SubmissionStatuses to a specified Evaluation.
        api_response = api_instance.get_all_submission_statuses(eval_id, limit=limit, offset=offset, status=status)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_all_submission_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **limit** | **int**| Limits the number of entities that will be fetched for this page. When null it will default to 10.&#39;  | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  | [optional] if omitted the server will use the default value of 0
 **status** | **str**| Submission status | [optional]

### Return type

[**PaginatedResultsOfSubmissionStatus**](PaginatedResultsOfSubmissionStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_submissions**
> PaginatedResultsOfSubmission get_all_submissions(eval_id)

Gets a collection of Submissions to a specified Evaluation.

'Gets a collection of Submissions to a specified Evaluation. <p> <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ_PRIVATE_SUBMISSION</a> on the specified Evaluation. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.paginated_results_of_submission import PaginatedResultsOfSubmission
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    limit = 10 # int | Limits the number of entities that will be fetched for this page. When null it will default to 10, max value 100.  (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  (optional) if omitted the server will use the default value of 0
    status = "status_example" # str | Status of submission. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a collection of Submissions to a specified Evaluation.
        api_response = api_instance.get_all_submissions(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_all_submissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a collection of Submissions to a specified Evaluation.
        api_response = api_instance.get_all_submissions(eval_id, limit=limit, offset=offset, status=status)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_all_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **limit** | **int**| Limits the number of entities that will be fetched for this page. When null it will default to 10, max value 100.  | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  | [optional] if omitted the server will use the default value of 0
 **status** | **str**| Status of submission. | [optional]

### Return type

[**PaginatedResultsOfSubmission**](PaginatedResultsOfSubmission.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_evaluations_paginated**
> PaginatedResultsOfEvaluation get_available_evaluations_paginated()

Gets a collection of Evaluations in which the user has SUBMIT permission, within a given range. 

Gets a collection of Evaluations in which the user has SUBMIT permission, within a given range. <p> <b>Note:</b> The response will contain only those Evaluations on which the caller must is granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.SUBMIT</a> permission. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.paginated_results_of_evaluation import PaginatedResultsOfEvaluation
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    active_only = False # bool | Retrieve active only evaluation queues (optional) if omitted the server will use the default value of False
    evaluation_ids = "evaluationIds_example" # str | an optional, comma-delimited list of evaluation IDs to which the response is limited  (optional)
    limit = 10 # int | Limits the number of entities that will be fetched for this page. When null it will default to 10.'  (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a collection of Evaluations in which the user has SUBMIT permission, within a given range. 
        api_response = api_instance.get_available_evaluations_paginated(active_only=active_only, evaluation_ids=evaluation_ids, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_available_evaluations_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **active_only** | **bool**| Retrieve active only evaluation queues | [optional] if omitted the server will use the default value of False
 **evaluation_ids** | **str**| an optional, comma-delimited list of evaluation IDs to which the response is limited  | [optional]
 **limit** | **int**| Limits the number of entities that will be fetched for this page. When null it will default to 10.&#39;  | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  | [optional] if omitted the server will use the default value of 0

### Return type

[**PaginatedResultsOfEvaluation**](PaginatedResultsOfEvaluation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation**
> Evaluation get_evaluation(eval_id)

Gets an Evaluation.

Gets an Evaluation.   <p>  <b>Note:</b> The caller must be granted the <a  href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\"  >ACCESS_TYPE.READ</a> on the specified Evaluation.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.evaluation import Evaluation
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.

    # example passing only required values which don't have defaults set
    try:
        # Gets an Evaluation.
        api_response = api_instance.get_evaluation(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluation_round**
> EvaluationRound get_evaluation_round(eval_id, round_id)

Get Evaluation Round

Get Evaluation Round

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.evaluation_round import EvaluationRound
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    round_id = "roundId_example" # str | The ID of the evaluation round

    # example passing only required values which don't have defaults set
    try:
        # Get Evaluation Round
        api_response = api_instance.get_evaluation_round(eval_id, round_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_evaluation_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **round_id** | **str**| The ID of the evaluation round |

### Return type

[**EvaluationRound**](EvaluationRound.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluations_by_content_source_paginated**
> PaginatedResultsOfEvaluation get_evaluations_by_content_source_paginated(id)

Gets Evaluations tied to a project.

Gets Evaluations tied to a project. <b>Note:</b> The response will contain only those Evaluations on which the caller is granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ</a> permission, unless specified otherwise with the accessType parameter. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.paginated_results_of_evaluation import PaginatedResultsOfEvaluation
from synclient.model.accesstype import ACCESSTYPE
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    id = "id_example" # str | the ID of the project
    access_type = ACCESSTYPE("CREATE") # ACCESSTYPE | The type of access for the user to filter for, optional and defaults to <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ</a>  (optional)
    active_only = False # bool | If 'true' then return only those evaluations with rounds defined and for which the current time is in one of the rounds.  (optional) if omitted the server will use the default value of False
    evaluation_ids = "evaluationIds_example" # str | an optional, comma-delimited list of evaluation IDs to which the response is limited  (optional)
    limit = 10 # int | Limits the number of entities that will be fetched for this page. When null it will default to 10.  (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Gets Evaluations tied to a project.
        api_response = api_instance.get_evaluations_by_content_source_paginated(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_evaluations_by_content_source_paginated: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets Evaluations tied to a project.
        api_response = api_instance.get_evaluations_by_content_source_paginated(id, access_type=access_type, active_only=active_only, evaluation_ids=evaluation_ids, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_evaluations_by_content_source_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the project |
 **access_type** | **ACCESSTYPE**| The type of access for the user to filter for, optional and defaults to &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.ACCESS_TYPE}\&quot;&gt;ACCESS_TYPE.READ&lt;/a&gt;  | [optional]
 **active_only** | **bool**| If &#39;true&#39; then return only those evaluations with rounds defined and for which the current time is in one of the rounds.  | [optional] if omitted the server will use the default value of False
 **evaluation_ids** | **str**| an optional, comma-delimited list of evaluation IDs to which the response is limited  | [optional]
 **limit** | **int**| Limits the number of entities that will be fetched for this page. When null it will default to 10.  | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  | [optional] if omitted the server will use the default value of 0

### Return type

[**PaginatedResultsOfEvaluation**](PaginatedResultsOfEvaluation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_evaluations_paginated**
> PaginatedResultsOfEvaluation get_evaluations_paginated()

Gets a collection of Evaluations, within a given range.

Gets a collection of Evaluations, within a given range.  <p>  <b>Note:</b> The response will contain only those Evaluations on which the caller is  granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ</a>  permission, unless specified otherwise with the accessType parameter.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.paginated_results_of_evaluation import PaginatedResultsOfEvaluation
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    access_type = "READ" # str | The type of access for the user to filter for, optional and defaults to <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ</a>  (optional) if omitted the server will use the default value of "READ"
    active_only = False # bool | If 'true' then return only those evaluations with rounds defined and for which the current time is in one of the rounds.  (optional) if omitted the server will use the default value of False
    evaluation_ids = "evaluationIds_example" # str | an optional, comma-delimited list of evaluation IDs to which the response is limited  (optional)
    limit = 10 # int | Maximum number of results returned (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a collection of Evaluations, within a given range.
        api_response = api_instance.get_evaluations_paginated(access_type=access_type, active_only=active_only, evaluation_ids=evaluation_ids, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_evaluations_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_type** | **str**| The type of access for the user to filter for, optional and defaults to &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.ACCESS_TYPE}\&quot;&gt;ACCESS_TYPE.READ&lt;/a&gt;  | [optional] if omitted the server will use the default value of "READ"
 **active_only** | **bool**| If &#39;true&#39; then return only those evaluations with rounds defined and for which the current time is in one of the rounds.  | [optional] if omitted the server will use the default value of False
 **evaluation_ids** | **str**| an optional, comma-delimited list of evaluation IDs to which the response is limited  | [optional]
 **limit** | **int**| Maximum number of results returned | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.  | [optional] if omitted the server will use the default value of 0

### Return type

[**PaginatedResultsOfEvaluation**](PaginatedResultsOfEvaluation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_submission_bundles**
> PaginatedResultsOfSubmissionBundle get_my_submission_bundles(eval_id)

Gets the requesting users bundled Submissions and SubmissionStatuses to a specified Evaluation.' 

Gets the requesting user's bundled Submissions and SubmissionStatuses to a specified Evaluation. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.paginated_results_of_submission_bundle import PaginatedResultsOfSubmissionBundle
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    limit = 10 # int | Limits the number of entities that will be fetched for this page. When null it will default to 10.'  (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Gets the requesting users bundled Submissions and SubmissionStatuses to a specified Evaluation.' 
        api_response = api_instance.get_my_submission_bundles(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_my_submission_bundles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the requesting users bundled Submissions and SubmissionStatuses to a specified Evaluation.' 
        api_response = api_instance.get_my_submission_bundles(eval_id, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_my_submission_bundles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **limit** | **int**| Limits the number of entities that will be fetched for this page. When null it will default to 10.&#39;  | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.  | [optional] if omitted the server will use the default value of 0

### Return type

[**PaginatedResultsOfSubmissionBundle**](PaginatedResultsOfSubmissionBundle.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_submissions**
> PaginatedResultsOfSubmission get_my_submissions(eval_id)

Gets the requesting user's Submissions to a specified Evaluation.

Gets the requesting user's Submissions to a specified Evaluation. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.paginated_results_of_submission import PaginatedResultsOfSubmission
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    limit = 10 # int | Limits the number of entities that will be fetched for this page. When null it will default to 10. (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.'  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Gets the requesting user's Submissions to a specified Evaluation.
        api_response = api_instance.get_my_submissions(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_my_submissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets the requesting user's Submissions to a specified Evaluation.
        api_response = api_instance.get_my_submissions(eval_id, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_my_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **limit** | **int**| Limits the number of entities that will be fetched for this page. When null it will default to 10. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The offset index determines where this page will start from. An index of 0 is the first entity. When null it will default to 0.&#39;  | [optional] if omitted the server will use the default value of 0

### Return type

[**PaginatedResultsOfSubmission**](PaginatedResultsOfSubmission.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission**
> SubmissionModel get_submission(sub_id)

Gets a Submission.

Gets a Submission.  <p>  <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ_PRIVATE_SUBMISSION</a> on the specified Evaluation.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.submission_model import SubmissionModel
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    sub_id = "subId_example" # str | The ID of the Submission

    # example passing only required values which don't have defaults set
    try:
        # Gets a Submission.
        api_response = api_instance.get_submission(sub_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The ID of the Submission |

### Return type

[**SubmissionModel**](SubmissionModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission_count**
> int get_submission_count(eval_id)

Gets the number of Submissions to a specified Evaluation.

Gets the number of Submissions to a specified Evaluation. <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ_PRIVATE_SUBMISSION</a> on the specified Evaluation. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.

    # example passing only required values which don't have defaults set
    try:
        # Gets the number of Submissions to a specified Evaluation.
        api_response = api_instance.get_submission_count(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_submission_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |

### Return type

**int**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_submission_status**
> SubmissionStatusModel get_submission_status(sub_id)

Gets the SubmissionStatus object associated with a specified Submission.

Gets the SubmissionStatus object associated with a specified Submission. <p> <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ</a> on the specified Evaluation. Furthermore, the caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ_PRIVATE_SUBMISSION</a> to see all data marked as \"private\" in the SubmissionStatus.   <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum frequency this method can be called</td>  <td>1 calls per second</td>  </tr>  </table>  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.submission_status_model import SubmissionStatusModel
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    sub_id = "subId_example" # str | The ID of the Submission

    # example passing only required values which don't have defaults set
    try:
        # Gets the SubmissionStatus object associated with a specified Submission.
        api_response = api_instance.get_submission_status(sub_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_submission_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The ID of the Submission |

### Return type

[**SubmissionStatusModel**](SubmissionStatusModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_submission_eligibility**
> TeamSubmissionEligibility get_team_submission_eligibility(eval_id, id)

Find out whether a Team and its members are eligible to submit to a given Evaluation queue (at the current time).' 

Find out whether a Team and its members are eligible to submit to a given Evaluation queue (at the current time).  The request must include an Evaluation ID and a Team ID.   The 'eligibilityStateHash' field of the returned object is a required parameter of the subsequent Team Submission request made for the given Evaluation and Team. (See: <a href=\"${POST.evaluation.submission}\">POST/evaluation/submission</a>)' 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.team_submission_eligibility import TeamSubmissionEligibility
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    id = "id_example" # str | The ID of a Team.

    # example passing only required values which don't have defaults set
    try:
        # Find out whether a Team and its members are eligible to submit to a given Evaluation queue (at the current time).' 
        api_response = api_instance.get_team_submission_eligibility(eval_id, id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->get_team_submission_eligibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **id** | **str**| The ID of a Team. |

### Return type

[**TeamSubmissionEligibility**](TeamSubmissionEligibility.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **has_access2**
> BooleanResult has_access2(eval_id, access_type)

Determines whether a specified Synapse user has a certain access type on evaluation.

Determines whether the logged in user has a certain <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE</a> on the specified Evaluation. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.boolean_result import BooleanResult
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    access_type = "accessType_example" # str | Synapse access type

    # example passing only required values which don't have defaults set
    try:
        # Determines whether a specified Synapse user has a certain access type on evaluation.
        api_response = api_instance.has_access2(eval_id, access_type)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->has_access2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **access_type** | **str**| Synapse access type |

### Return type

[**BooleanResult**](BooleanResult.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **redirect_url_for_file_handle**
> str redirect_url_for_file_handle(file_handle_id, sub_id)

Gets a pre-signed URL to access a requested File contained within a specified Submission. 

Gets a pre-signed URL to access a requested File contained within a specified Submission. <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.READ_PRIVATE_SUBMISSION</a> on the specified Evaluation. </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    file_handle_id = "fileHandleId_example" # str | the ID of the requested FileHandle contained in the Submission.
    sub_id = "subId_example" # str | The ID of the Submission
    redirect = True # bool | To redirect (optional)

    # example passing only required values which don't have defaults set
    try:
        # Gets a pre-signed URL to access a requested File contained within a specified Submission. 
        api_response = api_instance.redirect_url_for_file_handle(file_handle_id, sub_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->redirect_url_for_file_handle: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Gets a pre-signed URL to access a requested File contained within a specified Submission. 
        api_response = api_instance.redirect_url_for_file_handle(file_handle_id, sub_id, redirect=redirect)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->redirect_url_for_file_handle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_handle_id** | **str**| the ID of the requested FileHandle contained in the Submission. |
 **sub_id** | **str**| The ID of the Submission |
 **redirect** | **bool**| To redirect | [optional]

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_to_cancel_submission**
> request_to_cancel_submission(sub_id)

User requests to cancel their submission.

User requests to cancel their submission. Only the user who submitted a submission can make this request. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    sub_id = "subId_example" # str | The ID of the Submission

    # example passing only required values which don't have defaults set
    try:
        # User requests to cancel their submission.
        api_instance.request_to_cancel_submission(sub_id)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->request_to_cancel_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The ID of the Submission |

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The request has been made. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_acl**
> AccessControlList update_acl()

Updates the supplied access control list (ACL) for an evaluation.

Updates the supplied access control list (ACL) for an evaluation. The <a href=\"${org.sagebionetworks.repo.model.AccessControlList}\">ACL</a> to be updated should have the ID of the evaluation. The user should have the proper <a href=\"${org.sagebionetworks.evaluation.model.UserEvaluationPermissions}\">permissions</a> in order to update the ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.access_control_list import AccessControlList
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    access_control_list = AccessControlList(
        created_by="created_by_example",
        creation_date="creation_date_example",
        etag="etag_example",
        id="id_example",
        modified_by="modified_by_example",
        modified_on="modified_on_example",
        resource_access=[
            ResourceAccess(
                access_type=[
                    ACCESSTYPE("CREATE"),
                ],
                principal_id=1,
            ),
        ],
    ) # AccessControlList | The ACL being updated. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates the supplied access control list (ACL) for an evaluation.
        api_response = api_instance.update_acl(access_control_list=access_control_list)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->update_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_control_list** | [**AccessControlList**](AccessControlList.md)| The ACL being updated. | [optional]

### Return type

[**AccessControlList**](AccessControlList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_evaluation**
> Evaluation update_evaluation(eval_id)

Updates an Evaluation.

'Updates an Evaluation.   <p>  Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle  concurrent updates. Each time an Evaluation is updated a new etag will be  issued to the Evaluation. When an update is requested, Synapse will compare the  etag of the passed Evaluation with the current etag of the Evaluation. If the  etags do not match, then the update will be rejected with a  PRECONDITION_FAILED (412) response. When this occurs, the caller should  fetch the latest copy of the Evaluation and re-apply any changes, then re-attempt  the Evaluation update.  </p>   <p>  <b>Note:</b> The caller must be granted the <a  href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\"  >ACCESS_TYPE.UPDATE</a> on the specified Evaluation.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.evaluation import Evaluation
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    evaluation = Evaluation(
        content_source="content_source_example",
        created_on="created_on_example",
        description="description_example",
        etag="etag_example",
        id="id_example",
        name="name_example",
        owner_id="owner_id_example",
        quota=SubmissionQuota(
            first_round_start="first_round_start_example",
            number_of_rounds=1,
            round_duration_millis=1,
            submission_limit=1,
        ),
        status=EvaluationStatus("PLANNED"),
        submission_instructions_message="submission_instructions_message_example",
        submission_receipt_message="submission_receipt_message_example",
    ) # Evaluation |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates an Evaluation.
        api_response = api_instance.update_evaluation(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->update_evaluation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates an Evaluation.
        api_response = api_instance.update_evaluation(eval_id, evaluation=evaluation)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->update_evaluation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **evaluation** | [**Evaluation**](Evaluation.md)|  | [optional]

### Return type

[**Evaluation**](Evaluation.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_evaluation_round**
> EvaluationRound update_evaluation_round(eval_id, round_id)

Update Evaluation Round

Update Evaluation Round

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.evaluation_round import EvaluationRound
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    round_id = "roundId_example" # str | The ID of the evaluation round
    evaluation_round = EvaluationRound(
        etag="etag_example",
        evaluation_id="evaluation_id_example",
        id="id_example",
        limits=[
            EvaluationRoundLimit(
                limit_type=EvaluationRoundLimitType("TOTAL"),
                maximum_submissions=1,
            ),
        ],
        round_end="round_end_example",
        round_start="round_start_example",
    ) # EvaluationRound |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Evaluation Round
        api_response = api_instance.update_evaluation_round(eval_id, round_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->update_evaluation_round: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Evaluation Round
        api_response = api_instance.update_evaluation_round(eval_id, round_id, evaluation_round=evaluation_round)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->update_evaluation_round: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **round_id** | **str**| The ID of the evaluation round |
 **evaluation_round** | [**EvaluationRound**](EvaluationRound.md)|  | [optional]

### Return type

[**EvaluationRound**](EvaluationRound.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_submission_status**
> SubmissionStatusModel update_submission_status(sub_id)

Updates a SubmissionStatus object.

Updates a SubmissionStatus object.   <p>  Synapse employs an Optimistic Concurrency Control (OCC) scheme to handle concurrent updates. Each time an SubmissionStatus is updated a new etag will be issued to the SubmissionStatus. When an update is requested, Synapse will compare the etag of the passed SubmissionStatus with the current etag of the SubmissionStatus. If the etags do not match, then the update will be rejected with a PRECONDITION_FAILED (412) response. When this occurs, the caller should fetch the latest copy of the SubmissionStatus and re-apply any changes, then re-attempt the SubmissionStatus update.  </p>  <p>  <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.UPDATE_SUBMISSION</a> on the specified Evaluation.  </p>  </p>  <p>  <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum frequency this method can be called</td>  <td>1 calls per second</td>  </tr>  </table>  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.submission_status_model import SubmissionStatusModel
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    sub_id = "subId_example" # str | The ID of the Submission
    submission_status_model = SubmissionStatusModel(
        annotations=AnnotationsAnnotation(
            double_annos=[
                DoubleAnnotation(
                    is_private=True,
                    key="key_example",
                    value=3.14,
                ),
            ],
            long_annos=[
                LongAnnotation(
                    is_private=True,
                    key="key_example",
                    value=1,
                ),
            ],
            object_id="object_id_example",
            scope_id="scope_id_example",
            string_annos=[
                StringAnnotation(
                    is_private=True,
                    key="key_example",
                    value="value_example",
                ),
            ],
            version=1,
        ),
        can_cancel=True,
        cancel_requested=True,
        entity_id="entity_id_example",
        etag="etag_example",
        id="id_example",
        modified_on="modified_on_example",
        status=SubmissionStatusEnum("OPEN"),
        status_version=3.14,
        submission_annotations=AnnotationsV2(
            annotations={
                "key": AnnotationsValue(
                    type=AnnotationsValueType("STRING"),
                    value=[
                        "value_example",
                    ],
                ),
            },
            etag="etag_example",
            id="id_example",
        ),
        version_number=1,
    ) # SubmissionStatusModel |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Updates a SubmissionStatus object.
        api_response = api_instance.update_submission_status(sub_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->update_submission_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Updates a SubmissionStatus object.
        api_response = api_instance.update_submission_status(sub_id, submission_status_model=submission_status_model)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->update_submission_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_id** | **str**| The ID of the Submission |
 **submission_status_model** | [**SubmissionStatusModel**](SubmissionStatusModel.md)|  | [optional]

### Return type

[**SubmissionStatusModel**](SubmissionStatusModel.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_submission_status_batch**
> BatchUploadResponse update_submission_status_batch(eval_id)

Update multiple SubmissionStatuses.

Update multiple SubmissionStatuses. The maximum batch size is 500.  To allow upload of more than this maximum, the system supports uploading of a <i>series</i> of batches. Synapse employs optimistic concurrency on the series in the form of a batch token. Each request (except the first) must include the ''batch token'' returned in the response to the previous batch. If another client begins batch upload simultaneously, a PRECONDITION_FAILED (412) response will be generated and upload must restart from the first batch.  After the final batch is uploaded, the data for the Evaluation queue will be mirrored to the tables which support querying.  Therefore uploaded data will not appear in Evaluation queries until after the final batch is successfully uploaded.  It is the client''s responsibility to note in each batch request (1) whether it is the first batch in the series and (2) whether it is the last batch.  (For a single batch both are set to ''true''.)  Failure to use the flags correctly risks corrupted data (due to simultaneous, conflicting uploads by multiple clients) or data not appearing in query results.   <p>  <b>Note:</b> The caller must be granted the <a href=\"${org.sagebionetworks.repo.model.ACCESS_TYPE}\">ACCESS_TYPE.UPDATE_SUBMISSION</a> on the specified Evaluation.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import evaluation_services_api
from synclient.model.batch_upload_response import BatchUploadResponse
from synclient.model.submission_status_batch import SubmissionStatusBatch
from pprint import pprint
# Defining the host is optional and defaults to https://repo-prod.prod.sagebase.org/repo/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = synclient.Configuration(
    host = "https://repo-prod.prod.sagebase.org/repo/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = synclient.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with synclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = evaluation_services_api.EvaluationServicesApi(api_client)
    eval_id = "evalId_example" # str | The ID of the specified Evaluation.
    submission_status_batch = SubmissionStatusBatch(
        batch_token="batch_token_example",
        is_first_batch=True,
        is_last_batch=True,
        statuses=[
            SubmissionStatusModel(
                annotations=AnnotationsAnnotation(
                    double_annos=[
                        DoubleAnnotation(
                            is_private=True,
                            key="key_example",
                            value=3.14,
                        ),
                    ],
                    long_annos=[
                        LongAnnotation(
                            is_private=True,
                            key="key_example",
                            value=1,
                        ),
                    ],
                    object_id="object_id_example",
                    scope_id="scope_id_example",
                    string_annos=[
                        StringAnnotation(
                            is_private=True,
                            key="key_example",
                            value="value_example",
                        ),
                    ],
                    version=1,
                ),
                can_cancel=True,
                cancel_requested=True,
                entity_id="entity_id_example",
                etag="etag_example",
                id="id_example",
                modified_on="modified_on_example",
                status=SubmissionStatusEnum("OPEN"),
                status_version=3.14,
                submission_annotations=AnnotationsV2(
                    annotations={
                        "key": AnnotationsValue(
                            type=AnnotationsValueType("STRING"),
                            value=[
                                "value_example",
                            ],
                        ),
                    },
                    etag="etag_example",
                    id="id_example",
                ),
                version_number=1,
            ),
        ],
    ) # SubmissionStatusBatch |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update multiple SubmissionStatuses.
        api_response = api_instance.update_submission_status_batch(eval_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->update_submission_status_batch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update multiple SubmissionStatuses.
        api_response = api_instance.update_submission_status_batch(eval_id, submission_status_batch=submission_status_batch)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling EvaluationServicesApi->update_submission_status_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **eval_id** | **str**| The ID of the specified Evaluation. |
 **submission_status_batch** | [**SubmissionStatusBatch**](SubmissionStatusBatch.md)|  | [optional]

### Return type

[**BatchUploadResponse**](BatchUploadResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

