# synclient.MembershipInvitationServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_invitations_by_team**](MembershipInvitationServicesApi.md#get_open_invitations_by_team) | **GET** /team/{id}/openInvitation | Retrieve the open invitations from a Team, optionally filtering by the invitee. 
[**get_open_invitations_by_user**](MembershipInvitationServicesApi.md#get_open_invitations_by_user) | **GET** /user/{id}/openInvitation | Retrieve the open invitations to a user, optionally filtering by the Team of origin. 


# **get_open_invitations_by_team**
> PaginatedResultsOfMembershipInvitation get_open_invitations_by_team(id)

Retrieve the open invitations from a Team, optionally filtering by the invitee. 

Retrieve the open invitations from a Team, optionally filtering by the invitee. An invitation is only open if it has not expired and if the user has not joined the Team. Note: certain fields may be omitted when returned if the field value is null 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import membership_invitation_services_api
from synclient.model.paginated_results_of_membership_invitation import PaginatedResultsOfMembershipInvitation
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
    api_instance = membership_invitation_services_api.MembershipInvitationServicesApi(api_client)
    id = "id_example" # str | the ID of the Team.
    invitee_id = "inviteeId_example" # str | the ID of the Synapse user to which invitations have been extended (optional)
    limit = 10 # int | the maximum number of invitations to return (optional) if omitted the server will use the default value of 10
    offset = 0 # int | the starting index of the returned results (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the open invitations from a Team, optionally filtering by the invitee. 
        api_response = api_instance.get_open_invitations_by_team(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling MembershipInvitationServicesApi->get_open_invitations_by_team: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the open invitations from a Team, optionally filtering by the invitee. 
        api_response = api_instance.get_open_invitations_by_team(id, invitee_id=invitee_id, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling MembershipInvitationServicesApi->get_open_invitations_by_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. |
 **invitee_id** | **str**| the ID of the Synapse user to which invitations have been extended | [optional]
 **limit** | **int**| the maximum number of invitations to return | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| the starting index of the returned results | [optional] if omitted the server will use the default value of 0

### Return type

[**PaginatedResultsOfMembershipInvitation**](PaginatedResultsOfMembershipInvitation.md)

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

# **get_open_invitations_by_user**
> PaginatedResultsOfMembershipInvitation get_open_invitations_by_user(id)

Retrieve the open invitations to a user, optionally filtering by the Team of origin. 

Retrieve the open invitations to a user, optionally filtering by the Team of origin. An invitation is only open if it has not expired and if the user has not joined the Team. Note: certain fields may be omitted when returned if the field value is null 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import membership_invitation_services_api
from synclient.model.paginated_results_of_membership_invitation import PaginatedResultsOfMembershipInvitation
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
    api_instance = membership_invitation_services_api.MembershipInvitationServicesApi(api_client)
    id = "id_example" # str | The ID of the Synapse user.
    limit = 10 # int | the maximum number of invitations to return. (optional) if omitted the server will use the default value of 10
    offset = 0 # int | the starting index of the returned results. (optional) if omitted the server will use the default value of 0
    team_id = "teamId_example" # str | the ID of the Team extending the invitations (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the open invitations to a user, optionally filtering by the Team of origin. 
        api_response = api_instance.get_open_invitations_by_user(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling MembershipInvitationServicesApi->get_open_invitations_by_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the open invitations to a user, optionally filtering by the Team of origin. 
        api_response = api_instance.get_open_invitations_by_user(id, limit=limit, offset=offset, team_id=team_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling MembershipInvitationServicesApi->get_open_invitations_by_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Synapse user. |
 **limit** | **int**| the maximum number of invitations to return. | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| the starting index of the returned results. | [optional] if omitted the server will use the default value of 0
 **team_id** | **str**| the ID of the Team extending the invitations | [optional]

### Return type

[**PaginatedResultsOfMembershipInvitation**](PaginatedResultsOfMembershipInvitation.md)

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

