# synclient.DataAccessServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_requirement_status**](DataAccessServicesApi.md#get_access_requirement_status) | **GET** /accessRequirement/{requirementId}/status | Retrieve an access requirement status for a given access requirement ID.
[**get_request_for_update**](DataAccessServicesApi.md#get_request_for_update) | **GET** /accessRequirement/{requirementId}/dataAccessRequestForUpdate | Retrieve the Request for update.
[**get_user_own_research_project_for_update**](DataAccessServicesApi.md#get_user_own_research_project_for_update) | **GET** /accessRequirement/{requirementId}/researchProjectForUpdate | Retrieve an existing ResearchProject that the user owns.
[**list_ar_submissions**](DataAccessServicesApi.md#list_ar_submissions) | **POST** /accessRequirement/{requirementId}/submissions | Retrieve a list of submissions for a given access requirement ID.
[**list_info_for_approved_submissions**](DataAccessServicesApi.md#list_info_for_approved_submissions) | **POST** /accessRequirement/{requirementId}/approvedSubmissionInfo | Return approved data access submissions


# **get_access_requirement_status**
> AccessRequirementStatus get_access_requirement_status(requirement_id)

Retrieve an access requirement status for a given access requirement ID.

Retrieve an access requirement status for a given access requirement ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import data_access_services_api
from synclient.model.access_requirement_status import AccessRequirementStatus
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
    api_instance = data_access_services_api.DataAccessServicesApi(api_client)
    requirement_id = "requirementId_example" # str | the ID of the requirement.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an access requirement status for a given access requirement ID.
        api_response = api_instance.get_access_requirement_status(requirement_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DataAccessServicesApi->get_access_requirement_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requirement_id** | **str**| the ID of the requirement. |

### Return type

[**AccessRequirementStatus**](AccessRequirementStatus.md)

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

# **get_request_for_update**
> RequestInterface get_request_for_update(requirement_id)

Retrieve the Request for update.

Retrieve the Request for update.  If one does not exist, an Request with some re-filled information is returned. If a submission associated with the request is approved, and the requirement requires renewal, a refilled Renewal is returned. Only the owner of the request can perform this action. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import data_access_services_api
from synclient.model.request_interface import RequestInterface
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
    api_instance = data_access_services_api.DataAccessServicesApi(api_client)
    requirement_id = "requirementId_example" # str | the ID of the requirement.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the Request for update.
        api_response = api_instance.get_request_for_update(requirement_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DataAccessServicesApi->get_request_for_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requirement_id** | **str**| the ID of the requirement. |

### Return type

[**RequestInterface**](RequestInterface.md)

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

# **get_user_own_research_project_for_update**
> ResearchProject get_user_own_research_project_for_update(requirement_id)

Retrieve an existing ResearchProject that the user owns.

Retrieve an existing ResearchProject that the user owns.  If none exists, a ResearchProject with some re-filled information is returned to the user. Only the owner of the researchProject can perform this action. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import data_access_services_api
from synclient.model.research_project import ResearchProject
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
    api_instance = data_access_services_api.DataAccessServicesApi(api_client)
    requirement_id = "requirementId_example" # str | the ID of the requirement.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an existing ResearchProject that the user owns.
        api_response = api_instance.get_user_own_research_project_for_update(requirement_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DataAccessServicesApi->get_user_own_research_project_for_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requirement_id** | **str**| the ID of the requirement. |

### Return type

[**ResearchProject**](ResearchProject.md)

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

# **list_ar_submissions**
> SubmissionPage list_ar_submissions(requirement_id)

Retrieve a list of submissions for a given access requirement ID.

Retrieve a list of submissions for a given access requirement ID.  Only ACT member can perform this action. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import data_access_services_api
from synclient.model.submission_page_request import SubmissionPageRequest
from synclient.model.submission_page import SubmissionPage
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
    api_instance = data_access_services_api.DataAccessServicesApi(api_client)
    requirement_id = "requirementId_example" # str | the ID of the requirement.
    submission_page_request = SubmissionPageRequest(
        access_requirement_id="access_requirement_id_example",
        filter_by=SubmissionState("SUBMITTED"),
        is_ascending=True,
        next_page_token="next_page_token_example",
        order_by=SubmissionOrder("CREATED_ON"),
    ) # SubmissionPageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a list of submissions for a given access requirement ID.
        api_response = api_instance.list_ar_submissions(requirement_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DataAccessServicesApi->list_ar_submissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a list of submissions for a given access requirement ID.
        api_response = api_instance.list_ar_submissions(requirement_id, submission_page_request=submission_page_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DataAccessServicesApi->list_ar_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requirement_id** | **str**| the ID of the requirement. |
 **submission_page_request** | [**SubmissionPageRequest**](SubmissionPageRequest.md)|  | [optional]

### Return type

[**SubmissionPage**](SubmissionPage.md)

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

# **list_info_for_approved_submissions**
> SubmissionInfoPage list_info_for_approved_submissions(requirement_id)

Return approved data access submissions

Return the research project info for approved data access submissions, ordered by submission modified-on date, ascending 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import data_access_services_api
from synclient.model.submission_info_page import SubmissionInfoPage
from synclient.model.submission_info_page_request import SubmissionInfoPageRequest
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
    api_instance = data_access_services_api.DataAccessServicesApi(api_client)
    requirement_id = "requirementId_example" # str | the ID of the requirement.
    submission_info_page_request = SubmissionInfoPageRequest(
        access_requirement_id="access_requirement_id_example",
        next_page_token="next_page_token_example",
    ) # SubmissionInfoPageRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Return approved data access submissions
        api_response = api_instance.list_info_for_approved_submissions(requirement_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DataAccessServicesApi->list_info_for_approved_submissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Return approved data access submissions
        api_response = api_instance.list_info_for_approved_submissions(requirement_id, submission_info_page_request=submission_info_page_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling DataAccessServicesApi->list_info_for_approved_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requirement_id** | **str**| the ID of the requirement. |
 **submission_info_page_request** | [**SubmissionInfoPageRequest**](SubmissionInfoPageRequest.md)|  | [optional]

### Return type

[**SubmissionInfoPage**](SubmissionInfoPage.md)

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

