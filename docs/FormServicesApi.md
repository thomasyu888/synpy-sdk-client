# synclient.FormServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_form_data**](FormServicesApi.md#create_form_data) | **POST** /form/data | Create a new FormData object.
[**create_group**](FormServicesApi.md#create_group) | **POST** /form/group | Create a FormGroup with the provided name.
[**delete_form_data**](FormServicesApi.md#delete_form_data) | **DELETE** /form/data/{id} | Delete a FormData object.
[**get_form_group**](FormServicesApi.md#get_form_group) | **GET** /form/group/{id} | Get a FormGroup with the provided ID.
[**get_group_acl**](FormServicesApi.md#get_group_acl) | **GET** /form/group/{id}/acl | Get the ACL for a FormGroup
[**list_form_status**](FormServicesApi.md#list_form_status) | **POST** /form/data/list | List FormData objects and their associated status. 
[**list_form_status_reviewer**](FormServicesApi.md#list_form_status_reviewer) | **POST** /form/data/list/reviewer | List FormData objects and their associated status. 
[**reviewer_accept_form**](FormServicesApi.md#reviewer_accept_form) | **PUT** /form/data/{id}/accept | Called by the form reviewing service to accept a submitted data.
[**reviewer_reject_form**](FormServicesApi.md#reviewer_reject_form) | **PUT** /form/data/{id}/reject | Called by the form reviewing service to reject a submitted data.
[**submit_form_data**](FormServicesApi.md#submit_form_data) | **POST** /form/data/{id}/submit | Submit the identified FormData from review.
[**update_form_data**](FormServicesApi.md#update_form_data) | **PUT** /form/data/{id} | Update a FormData object.
[**update_group_acl**](FormServicesApi.md#update_group_acl) | **PUT** /form/group/{id}/acl | Update the ACL for a FormGroup.


# **create_form_data**
> FormData create_form_data(group_id, form_change_request=form_change_request)

Create a new FormData object.

Create a new FormData object. The caller will own the resulting object and will have access to read, update, and delete the FormData object.  Note: The caller must have the SUBMIT permission on the FormGrup to  reate/update/submit FormData. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    group_id = 'group_id_example' # str | The identifier of the group that manages this data. 
form_change_request = synclient.FormChangeRequest() # FormChangeRequest |  (optional)

    try:
        # Create a new FormData object.
        api_response = api_instance.create_form_data(group_id, form_change_request=form_change_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->create_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier of the group that manages this data.  | 
 **form_change_request** | [**FormChangeRequest**](FormChangeRequest.md)|  | [optional] 

### Return type

[**FormData**](FormData.md)

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

# **create_group**
> FormGroup create_group(name)

Create a FormGroup with the provided name.

Create a FormGroup with the provided name. This method is idempotent. If a group with the provided name already exists and the caller has READ permission the existing FormGroup will be returned.  The created FormGroup will have an Access Control List (ACL) with the creator listed as an administrator. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    name = 'name_example' # str | A globally unique name for the group. Required. Between 3 and 256 characters. 

    try:
        # Create a FormGroup with the provided name.
        api_response = api_instance.create_group(name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| A globally unique name for the group. Required. Between 3 and 256 characters.  | 

### Return type

[**FormGroup**](FormGroup.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_form_data**
> str delete_form_data(id)

Delete a FormData object.

Delete an existing FormData object. The caller must be the creator of the FormData object.  Note: Cannot delete a FormData object once it has been submitted and caller must have the SUBMIT permission on the identified group to update the group's ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    id = 'id_example' # str | The ID of the FormData.

    try:
        # Delete a FormData object.
        api_response = api_instance.delete_form_data(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->delete_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FormData. | 

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

# **get_form_group**
> FormGroup get_form_group(id)

Get a FormGroup with the provided ID.

Get a FormGroup with the provided ID.  Note: The caller must have the READ permission on the identified group. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    id = 'id_example' # str | The ID to the FormGroup.

    try:
        # Get a FormGroup with the provided ID.
        api_response = api_instance.get_form_group(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->get_form_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID to the FormGroup. | 

### Return type

[**FormGroup**](FormGroup.md)

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

# **get_group_acl**
> AccessControlList get_group_acl(id)

Get the ACL for a FormGroup

Get the Access Control List (ACL) for a FormGroup.  Note: The caller must have READ permission on the identified group. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    id = 'id_example' # str | The ID of the FormGroup.

    try:
        # Get the ACL for a FormGroup
        api_response = api_instance.get_group_acl(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->get_group_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FormGroup. | 

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

# **list_form_status**
> ListResponse list_form_status(list_request=list_request)

List FormData objects and their associated status. 

List FormData objects and their associated status that match the filters of the provided request that are owned by the caller. Note: Only objects owned by the caller will be returned. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    list_request = synclient.ListRequest() # ListRequest |  (optional)

    try:
        # List FormData objects and their associated status. 
        api_response = api_instance.list_form_status(list_request=list_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->list_form_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)|  | [optional] 

### Return type

[**ListResponse**](ListResponse.md)

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

# **list_form_status_reviewer**
> ListResponse list_form_status_reviewer(list_request=list_request)

List FormData objects and their associated status. 

List FormData objects and their associated status that match the filters of the provided request for the entire group. This is used by service accounts to review submissions. Filtering by WAITING_FOR_SUBMISSION is not allowed for this call.  Note: The caller must have the READ_PRIVATE_SUBMISSION permission on the identified group to update the group's ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    list_request = synclient.ListRequest() # ListRequest |  (optional)

    try:
        # List FormData objects and their associated status. 
        api_response = api_instance.list_form_status_reviewer(list_request=list_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->list_form_status_reviewer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_request** | [**ListRequest**](ListRequest.md)|  | [optional] 

### Return type

[**ListResponse**](ListResponse.md)

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

# **reviewer_accept_form**
> FormData reviewer_accept_form(id)

Called by the form reviewing service to accept a submitted data.

Called by the form reviewing service to accept a submitted data.  Note: The caller must have the READ_PRIVATE_SUBMISSION permission on the identified group to update the group's ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    id = 'id_example' # str | The ID of the FormData.

    try:
        # Called by the form reviewing service to accept a submitted data.
        api_response = api_instance.reviewer_accept_form(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->reviewer_accept_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FormData. | 

### Return type

[**FormData**](FormData.md)

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

# **reviewer_reject_form**
> FormData reviewer_reject_form(id, form_rejection=form_rejection)

Called by the form reviewing service to reject a submitted data.

Called by the form reviewing service to reject a submitted data.  Note: The caller must have the READ_PRIVATE_SUBMISSION permission on the identified group to update the group's ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    id = 'id_example' # str | The ID of the FormData.
form_rejection = synclient.FormRejection() # FormRejection |  (optional)

    try:
        # Called by the form reviewing service to reject a submitted data.
        api_response = api_instance.reviewer_reject_form(id, form_rejection=form_rejection)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->reviewer_reject_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FormData. | 
 **form_rejection** | [**FormRejection**](FormRejection.md)|  | [optional] 

### Return type

[**FormData**](FormData.md)

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

# **submit_form_data**
> FormData submit_form_data(id)

Submit the identified FormData from review.

Submit the identified FormData from review.  Note: The caller must have the SUBMIT permission on the identified group to update the group's ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    id = 'id_example' # str | The ID of the FormData.

    try:
        # Submit the identified FormData from review.
        api_response = api_instance.submit_form_data(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->submit_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FormData. | 

### Return type

[**FormData**](FormData.md)

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

# **update_form_data**
> FormData update_form_data(id, form_change_request=form_change_request)

Update a FormData object.

Update an existing FormData object. The caller must be the creator of the FormData object. Once a FormData object has been submitted, it cannot be updated until it has been processed. If the submission is accepted it becomes immutable. Rejected submission are editable. Updating a rejected submission will change its status back to waiting_for_submission.  Note: The caller must have the SUBMIT permission on the FormGrup to create/update/submit FormData. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    id = 'id_example' # str | The ID of the FormData.
form_change_request = synclient.FormChangeRequest() # FormChangeRequest |  (optional)

    try:
        # Update a FormData object.
        api_response = api_instance.update_form_data(id, form_change_request=form_change_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->update_form_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FormData. | 
 **form_change_request** | [**FormChangeRequest**](FormChangeRequest.md)|  | [optional] 

### Return type

[**FormData**](FormData.md)

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

# **update_group_acl**
> AccessControlList update_group_acl(id, access_control_list=access_control_list)

Update the ACL for a FormGroup.

Update the Access Control List (ACL) for a FormGroup.  The following define the permissions in this context:  * READ - Grants read access to the group. READ does not grant access to FormData of the group. * CHANGE_PERMISSIONS - Grants access to update the group's ACL. * SUBMIT - Grants access to both create and submit FormData to the group. * READ_PRIVATE_SUBMISSION - Grants administrator's access to the submitted FormData, including both FormData reads and status updates. This permission should be reserved for the service account that evaluates submissions.  Users automatically have read/update access to FormData that they create.  Note: The caller must have the CHANGE_PERMISSIONS permission on the identified group to update the group's ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
from __future__ import print_function
import time
import synclient
from synclient.rest import ApiException
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
    api_instance = synclient.FormServicesApi(api_client)
    id = 'id_example' # str | The ID of the FormGroup.
access_control_list = synclient.AccessControlList() # AccessControlList |  (optional)

    try:
        # Update the ACL for a FormGroup.
        api_response = api_instance.update_group_acl(id, access_control_list=access_control_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FormServicesApi->update_group_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the FormGroup. | 
 **access_control_list** | [**AccessControlList**](AccessControlList.md)|  | [optional] 

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

