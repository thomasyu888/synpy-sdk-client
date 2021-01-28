# synclient.MembershipRequestServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_requests_by_team**](MembershipRequestServicesApi.md#get_open_requests_by_team) | **GET** /team/{id}/openRequest | Retrieve the open requests submitted to a Team, optionally filtering by the requester.
[**get_open_requests_by_user**](MembershipRequestServicesApi.md#get_open_requests_by_user) | **GET** /user/{id}/openRequest | Retrieve the open requests submitted by a user, optionally filtering by the Team. 


# **get_open_requests_by_team**
> PaginatedResultsOfMembershipRequest get_open_requests_by_team(id, limit=limit, offset=offset, requestor_id=requestor_id)

Retrieve the open requests submitted to a Team, optionally filtering by the requester.

Retrieve the open requests submitted to a Team, optionally filtering by the requester. An request is only open if it has not expired and if the requester has not been added the Team.  <p>  <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum frequency this method can be called</td>  <td>40 calls per minute</td>  </tr>  </table>  </p>' 

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
    api_instance = synclient.MembershipRequestServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
limit = 10 # int | the maximum number of requests to return (default 10) (optional) (default to 10)
offset = 0 # int | the starting index of the returned results (default 0) (optional) (default to 0)
requestor_id = 'requestor_id_example' # str | the ID of the user requesting admission to the Team (optional)

    try:
        # Retrieve the open requests submitted to a Team, optionally filtering by the requester.
        api_response = api_instance.get_open_requests_by_team(id, limit=limit, offset=offset, requestor_id=requestor_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipRequestServicesApi->get_open_requests_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **limit** | **int**| the maximum number of requests to return (default 10) | [optional] [default to 10]
 **offset** | **int**| the starting index of the returned results (default 0) | [optional] [default to 0]
 **requestor_id** | **str**| the ID of the user requesting admission to the Team | [optional] 

### Return type

[**PaginatedResultsOfMembershipRequest**](PaginatedResultsOfMembershipRequest.md)

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

# **get_open_requests_by_user**
> PaginatedResultsOfMembershipRequest get_open_requests_by_user(id, limit=limit, offset=offset, team_id=team_id)

Retrieve the open requests submitted by a user, optionally filtering by the Team. 

Retrieve the open requests submitted by a user, optionally filtering by the Team. An request is only open if it has not expired and if the requester has not been added the Team. Note:  The 'id' in the URI must be the same ID as that of the authenticated user issuing the request. 

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
    api_instance = synclient.MembershipRequestServicesApi(api_client)
    id = 'id_example' # str | The ID of the Synapse user.
limit = 10 # int | the maximum number of requests to return (optional) (default to 10)
offset = 0 # int | the starting index of the returned results. (optional) (default to 0)
team_id = 'team_id_example' # str | ID of a Synapse Team. (optional)

    try:
        # Retrieve the open requests submitted by a user, optionally filtering by the Team. 
        api_response = api_instance.get_open_requests_by_user(id, limit=limit, offset=offset, team_id=team_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MembershipRequestServicesApi->get_open_requests_by_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Synapse user. | 
 **limit** | **int**| the maximum number of requests to return | [optional] [default to 10]
 **offset** | **int**| the starting index of the returned results. | [optional] [default to 0]
 **team_id** | **str**| ID of a Synapse Team. | [optional] 

### Return type

[**PaginatedResultsOfMembershipRequest**](PaginatedResultsOfMembershipRequest.md)

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

