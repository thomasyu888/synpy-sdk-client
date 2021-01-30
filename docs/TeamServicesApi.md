# synclient.TeamServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_team_member**](TeamServicesApi.md#add_team_member) | **PUT** /team/{id}/member/{principalId} | Add a member to the Team.
[**add_team_member_via_signed_token**](TeamServicesApi.md#add_team_member_via_signed_token) | **PUT** /teamMember | Add a member to the Team.
[**create_team**](TeamServicesApi.md#create_team) | **POST** /team | Create a new Team.
[**delete_team**](TeamServicesApi.md#delete_team) | **DELETE** /team/{id} | Delete the Team.
[**file_preview_redirect_url_for_team_icon**](TeamServicesApi.md#file_preview_redirect_url_for_team_icon) | **GET** /team/{id}/icon/preview | Retrieve the download URL for the Team icon preview, or receive a redirect response to said URL. 
[**file_redirect_url_for_team_icon**](TeamServicesApi.md#file_redirect_url_for_team_icon) | **GET** /team/{id}/icon | Retrieve the download URL for the Team icon, or receive a redirect response to said URL 
[**get_team**](TeamServicesApi.md#get_team) | **GET** /team/{id} | Retrieve the metadata for a specified Team.
[**get_team_acl**](TeamServicesApi.md#get_team_acl) | **GET** /team/{id}/acl | Retrieve the AccessControlList for a specified Team.
[**get_team_ids_by_member**](TeamServicesApi.md#get_team_ids_by_member) | **GET** /user/{id}/team/id | Retrieve a paginated list of IDs of Teams to which the given user belongs.
[**get_team_member**](TeamServicesApi.md#get_team_member) | **GET** /team/{id}/member/{principalId} | .
[**get_team_member_count**](TeamServicesApi.md#get_team_member_count) | **GET** /teamMembers/count/{id} | Retrieve the number of Team members matching the supplied name prefix.
[**get_team_members**](TeamServicesApi.md#get_team_members) | **GET** /teamMembers/{id} | Retrieve a paginated list of Team members matching the supplied name prefix.
[**get_team_membership_status**](TeamServicesApi.md#get_team_membership_status) | **GET** /team/{id}/member/{principalId}/membershipStatus | Retrieve the Team Membership Status bundle for a team and user.
[**get_teams_by_member**](TeamServicesApi.md#get_teams_by_member) | **GET** /user/{id}/team | Retrieve a paginated list of Teams to which the given user belongs.
[**get_teams_by_name_fragment**](TeamServicesApi.md#get_teams_by_name_fragment) | **GET** /teams | Retrieve a paginated list of Teams in alphabetical order by Team name.
[**list_team_members_given_teamand_user_list**](TeamServicesApi.md#list_team_members_given_teamand_user_list) | **POST** /team/{id}/memberList | Returns the TeamMember info for a team and a given list of members&#39; principal IDs. 
[**list_team_members_given_userand_team_list**](TeamServicesApi.md#list_team_members_given_userand_team_list) | **POST** /user/{id}/memberList | Returns the TeamMember info for a user and a given list of Team IDs.
[**list_teams**](TeamServicesApi.md#list_teams) | **POST** /teamList | Retrieve a list of Teams given their IDs.
[**remove_team_member**](TeamServicesApi.md#remove_team_member) | **DELETE** /team/{id}/member/{principalId} | Remove the given member from the specified Team.
[**update_team**](TeamServicesApi.md#update_team) | **PUT** /team | Update the Team metadata for the specified Team.
[**update_team_acl**](TeamServicesApi.md#update_team_acl) | **PUT** /team/acl | Update the Access Control List for the specified Team.


# **add_team_member**
> add_team_member(id, principal_id, notification_unsubscribe_endpoint=notification_unsubscribe_endpoint, team_endpoint=team_endpoint)

Add a member to the Team.

Add a member to the Team.  If the one making the request is the user to be added, then the user must have an open invitation from the Team.  If the one making the request is an administrator on the Team, then there must be a pending request from the user to the Team, asking to be added. If both teamEndpoint and notificationUnsubscribeEndpoint are provided, notification email(s) will be sent to the appropriate parties. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
principal_id = 'principal_id_example' # str | the member's principal ID
notification_unsubscribe_endpoint = 'notification_unsubscribe_endpoint_example' # str | the portal prefix for one-click email unsubscription. A signed, serialized token is appended to create the complete URL: <ahref=\"${org.sagebionetworks.repo.model.message.NotificationSettingsSignedToken}\">NotificationSettingsSignedToken</a>'  (optional)
team_endpoint = 'team_endpoint_example' # str | the portal prefix for the Team URL. The team ID is appended to create the complete URL.  (optional)

    try:
        # Add a member to the Team.
        api_instance.add_team_member(id, principal_id, notification_unsubscribe_endpoint=notification_unsubscribe_endpoint, team_endpoint=team_endpoint)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->add_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **principal_id** | **str**| the member&#39;s principal ID | 
 **notification_unsubscribe_endpoint** | **str**| the portal prefix for one-click email unsubscription. A signed, serialized token is appended to create the complete URL: &lt;ahref&#x3D;\&quot;${org.sagebionetworks.repo.model.message.NotificationSettingsSignedToken}\&quot;&gt;NotificationSettingsSignedToken&lt;/a&gt;&#39;  | [optional] 
 **team_endpoint** | **str**| the portal prefix for the Team URL. The team ID is appended to create the complete URL.  | [optional] 

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
**204** | The resource has been added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_team_member_via_signed_token**
> ResponseMessage add_team_member_via_signed_token(notification_unsubscribe_endpoint=notification_unsubscribe_endpoint, team_endpoint=team_endpoint, join_team_signed_token=join_team_signed_token)

Add a member to the Team.

Add a member to the Team.  Note: The request is authenticated by a hash message authentication code in the request body, generated by Synapse.  The intended use of this service is by the portal, completing a round trip with a 'one-click join-team' link provided to the user by Synapse via email. If both teamEndpoint and notificationUnsubscribeEndpoint are provided, notification email(s) will be sent to the appropriate parties. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    notification_unsubscribe_endpoint = 'notification_unsubscribe_endpoint_example' # str | notification unsubscribe endpoint (optional)
team_endpoint = 'team_endpoint_example' # str | Team end point (optional)
join_team_signed_token = synclient.JoinTeamSignedToken() # JoinTeamSignedToken |  (optional)

    try:
        # Add a member to the Team.
        api_response = api_instance.add_team_member_via_signed_token(notification_unsubscribe_endpoint=notification_unsubscribe_endpoint, team_endpoint=team_endpoint, join_team_signed_token=join_team_signed_token)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->add_team_member_via_signed_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **notification_unsubscribe_endpoint** | **str**| notification unsubscribe endpoint | [optional] 
 **team_endpoint** | **str**| Team end point | [optional] 
 **join_team_signed_token** | [**JoinTeamSignedToken**](JoinTeamSignedToken.md)|  | [optional] 

### Return type

[**ResponseMessage**](ResponseMessage.md)

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

# **create_team**
> Team create_team(team=team)

Create a new Team.

Create a new Team. The passed request body may contain the following fields:  <ul>  <li>name - Give your new Team a name.  The name must be unique, not used by an existing Team (required).</li>  <li>description - a short text description of the Team''s purpose (optional).</li>  <li>icon - a fileHandle ID for an icon image file previously uploaded to Synapse (optional).</li>  </ul>  <p>  To specify a Team icon, the icon file must first be uploaded to Synapse as <a href=\"${org.sagebionetworks.repo.model.file.FileHandle}\">FileHandle</a> (see <a href=\"${org.sagebionetworks.file.controller.UploadController}\">File Services</a>). The FileHandle ID can then be put into the Team''s icon field. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    team = synclient.Team() # Team |  (optional)

    try:
        # Create a new Team.
        api_response = api_instance.create_team(team=team)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->create_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | [**Team**](Team.md)|  | [optional] 

### Return type

[**Team**](Team.md)

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

# **delete_team**
> delete_team(id)

Delete the Team.

Delete the Team. Note: The client must be a Team administrator to make this request. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.

    try:
        # Delete the Team.
        api_instance.delete_team(id)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->delete_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 

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

# **file_preview_redirect_url_for_team_icon**
> str file_preview_redirect_url_for_team_icon(id, redirect=redirect)

Retrieve the download URL for the Team icon preview, or receive a redirect response to said URL. 

Retrieve the download URL for the Team icon preview, or receive a redirect response to said URL. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
redirect = True # bool | if true or omitted, then redirect to the URL.  If false then simply return the URL.  (optional)

    try:
        # Retrieve the download URL for the Team icon preview, or receive a redirect response to said URL. 
        api_response = api_instance.file_preview_redirect_url_for_team_icon(id, redirect=redirect)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->file_preview_redirect_url_for_team_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **redirect** | **bool**| if true or omitted, then redirect to the URL.  If false then simply return the URL.  | [optional] 

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

# **file_redirect_url_for_team_icon**
> str file_redirect_url_for_team_icon(id, redirect=redirect)

Retrieve the download URL for the Team icon, or receive a redirect response to said URL 

Retrieve the download URL for the Team icon, or receive a redirect response to said URL.

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
redirect = True # bool | if true or omitted, then redirect to the URL.  If false then simply return the URL.  (optional)

    try:
        # Retrieve the download URL for the Team icon, or receive a redirect response to said URL 
        api_response = api_instance.file_redirect_url_for_team_icon(id, redirect=redirect)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->file_redirect_url_for_team_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **redirect** | **bool**| if true or omitted, then redirect to the URL.  If false then simply return the URL.  | [optional] 

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

# **get_team**
> Team get_team(id)

Retrieve the metadata for a specified Team.

Retrieve the metadata for a specified Team.  <p>  <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum frequency this method can be called</td>  <td>1 calls per second</td>  </tr>  </table>  </p> 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.

    try:
        # Retrieve the metadata for a specified Team.
        api_response = api_instance.get_team(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 

### Return type

[**Team**](Team.md)

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

# **get_team_acl**
> AccessControlList get_team_acl(id)

Retrieve the AccessControlList for a specified Team.

Retrieve the AccessControlList for a specified Team.

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.

    try:
        # Retrieve the AccessControlList for a specified Team.
        api_response = api_instance.get_team_acl(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->get_team_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 

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

# **get_team_ids_by_member**
> PaginatedTeamIds get_team_ids_by_member(id, ascending=ascending, next_page_token=next_page_token, sort=sort)

Retrieve a paginated list of IDs of Teams to which the given user belongs.

Retrieve a paginated list of IDs of Teams to which the given user belongs. If sorting is desired, both sort and ascending must be specified. If they are omitted, results are not sorted. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | The ID of the Synapse user.
ascending = True # bool | the direction of sort: true for ascending, and false for descending (optional)
next_page_token = 'next_page_token_example' # str | controls pagination (optional)
sort = 'sort_example' # str | the field to sort the team IDs on. Available options <a href=\"${org.sagebionetworks.repo.model.TeamSortOrder}\">TeamSortOrder</a>  (optional)

    try:
        # Retrieve a paginated list of IDs of Teams to which the given user belongs.
        api_response = api_instance.get_team_ids_by_member(id, ascending=ascending, next_page_token=next_page_token, sort=sort)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->get_team_ids_by_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Synapse user. | 
 **ascending** | **bool**| the direction of sort: true for ascending, and false for descending | [optional] 
 **next_page_token** | **str**| controls pagination | [optional] 
 **sort** | **str**| the field to sort the team IDs on. Available options &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.TeamSortOrder}\&quot;&gt;TeamSortOrder&lt;/a&gt;  | [optional] 

### Return type

[**PaginatedTeamIds**](PaginatedTeamIds.md)

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

# **get_team_member**
> TeamMember get_team_member(id, principal_id)

.

'<p>  <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum frequency this method can be called</td>  <td>1 calls per second</td>  </tr>  </table>  </p>' 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
principal_id = 'principal_id_example' # str | the member's principal ID

    try:
        # .
        api_response = api_instance.get_team_member(id, principal_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->get_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **principal_id** | **str**| the member&#39;s principal ID | 

### Return type

[**TeamMember**](TeamMember.md)

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

# **get_team_member_count**
> Count get_team_member_count(id, fragment=fragment)

Retrieve the number of Team members matching the supplied name prefix.

Retrieve the number of Team members matching the supplied name prefix.  If the prefix is omitted then the number of members in the team is returned.  <br>  Note:  This service has JSONP support:  If the request parameter \"callback=jsMethod\" is included (where 'jsMethod' is any function name you wish), then the response body will be wrapped in \"jsMethod(...);\". 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
fragment = 'fragment_example' # str | a prefix of the user's first or last name or email address  (optional)

    try:
        # Retrieve the number of Team members matching the supplied name prefix.
        api_response = api_instance.get_team_member_count(id, fragment=fragment)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->get_team_member_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **fragment** | **str**| a prefix of the user&#39;s first or last name or email address  | [optional] 

### Return type

[**Count**](Count.md)

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

# **get_team_members**
> PaginatedResultsOfTeamMember get_team_members(id, fragment=fragment, limit=limit, member_type=member_type, offset=offset)

Retrieve a paginated list of Team members matching the supplied name prefix.

Retrieve a paginated list of Team members matching the supplied name prefix.  If the prefix is omitted then all members are returned.  <br>  Note:  This service has JSONP support:  If the request parameter \"callback=jsMethod\" is included (where 'jsMethod' is any function name you wish), then the response body will be wrapped in \"jsMethod(...);\". 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
fragment = 'fragment_example' # str | a prefix of the user's first or last name or email address (optional)
limit = 10 # int | the maximum number of members to return. (optional) (default to 10)
member_type = 'ALL' # str | the type of team user to retrieve (optional) (default to 'ALL')
offset = 0 # int | the starting index of the returned results (optional) (default to 0)

    try:
        # Retrieve a paginated list of Team members matching the supplied name prefix.
        api_response = api_instance.get_team_members(id, fragment=fragment, limit=limit, member_type=member_type, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->get_team_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **fragment** | **str**| a prefix of the user&#39;s first or last name or email address | [optional] 
 **limit** | **int**| the maximum number of members to return. | [optional] [default to 10]
 **member_type** | **str**| the type of team user to retrieve | [optional] [default to &#39;ALL&#39;]
 **offset** | **int**| the starting index of the returned results | [optional] [default to 0]

### Return type

[**PaginatedResultsOfTeamMember**](PaginatedResultsOfTeamMember.md)

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

# **get_team_membership_status**
> TeamMembershipStatus get_team_membership_status(id, principal_id)

Retrieve the Team Membership Status bundle for a team and user.

Retrieve the Team Membership Status bundle for a team and user.  This says whether a user is a member of a Team, whether there are outstanding membership requests or invitations, and whether the client making the request can add the given user to the given Team. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
principal_id = 'principal_id_example' # str | the member's principal ID

    try:
        # Retrieve the Team Membership Status bundle for a team and user.
        api_response = api_instance.get_team_membership_status(id, principal_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->get_team_membership_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **principal_id** | **str**| the member&#39;s principal ID | 

### Return type

[**TeamMembershipStatus**](TeamMembershipStatus.md)

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

# **get_teams_by_member**
> PaginatedResultsOfTeam get_teams_by_member(id, limit=limit, offset=offset)

Retrieve a paginated list of Teams to which the given user belongs.

Retrieve a paginated list of Teams to which the given user belongs.

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | The ID of the Synapse user.
limit = 10 # int | the maximum number of Teams to return (default 10) (optional) (default to 10)
offset = 0 # int | the starting index of the returned results (default 0) (optional) (default to 0)

    try:
        # Retrieve a paginated list of Teams to which the given user belongs.
        api_response = api_instance.get_teams_by_member(id, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->get_teams_by_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Synapse user. | 
 **limit** | **int**| the maximum number of Teams to return (default 10) | [optional] [default to 10]
 **offset** | **int**| the starting index of the returned results (default 0) | [optional] [default to 0]

### Return type

[**PaginatedResultsOfTeam**](PaginatedResultsOfTeam.md)

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

# **get_teams_by_name_fragment**
> PaginatedResultsOfTeam get_teams_by_name_fragment(fragment=fragment, limit=limit, offset=offset)

Retrieve a paginated list of Teams in alphabetical order by Team name.

Retrieve a paginated list of Teams matching the supplied name fragment (optional), in alphabetical order by Team name.  <br>  Note:  This service has JSONP support:  If the request parameter \"callback=jsMethod\" is included (where 'jsMethod' is any function name you wish), then the response body will be wrapped in \"jsMethod(...);\". 

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
    api_instance = synclient.TeamServicesApi(api_client)
    fragment = 'fragment_example' # str | a prefix of the Team name, or a prefix of any sub-string in the name preceded by a space. If omitted, all Teams are returned.  (optional)
limit = 10 # int | the maximum number of Teams to return. (optional) (default to 10)
offset = 0 # int | the starting index of the returned results (default 0) (optional) (default to 0)

    try:
        # Retrieve a paginated list of Teams in alphabetical order by Team name.
        api_response = api_instance.get_teams_by_name_fragment(fragment=fragment, limit=limit, offset=offset)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->get_teams_by_name_fragment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fragment** | **str**| a prefix of the Team name, or a prefix of any sub-string in the name preceded by a space. If omitted, all Teams are returned.  | [optional] 
 **limit** | **int**| the maximum number of Teams to return. | [optional] [default to 10]
 **offset** | **int**| the starting index of the returned results (default 0) | [optional] [default to 0]

### Return type

[**PaginatedResultsOfTeam**](PaginatedResultsOfTeam.md)

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

# **list_team_members_given_teamand_user_list**
> ListWrapperOfTeamMember list_team_members_given_teamand_user_list(id, id_list=id_list)

Returns the TeamMember info for a team and a given list of members' principal IDs. 

Returns the TeamMember info for a team and a given list of members' principal IDs. Invalid IDs in the list are ignored:  The results list is simply smaller than the list of IDs passed in. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
id_list = synclient.IdList() # IdList |  (optional)

    try:
        # Returns the TeamMember info for a team and a given list of members' principal IDs. 
        api_response = api_instance.list_team_members_given_teamand_user_list(id, id_list=id_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->list_team_members_given_teamand_user_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **id_list** | [**IdList**](IdList.md)|  | [optional] 

### Return type

[**ListWrapperOfTeamMember**](ListWrapperOfTeamMember.md)

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

# **list_team_members_given_userand_team_list**
> ListWrapperOfTeamMember list_team_members_given_userand_team_list(id, id_list=id_list)

Returns the TeamMember info for a user and a given list of Team IDs.

Returns the TeamMember info for a user and a given list of Team IDs. Not Found status is returned if the user ID is invalid, any of the Team IDs are invalid, or the user is not in any of the given teams. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | The ID of the Synapse user.
id_list = synclient.IdList() # IdList | Team IDs (optional)

    try:
        # Returns the TeamMember info for a user and a given list of Team IDs.
        api_response = api_instance.list_team_members_given_userand_team_list(id, id_list=id_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->list_team_members_given_userand_team_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Synapse user. | 
 **id_list** | [**IdList**](IdList.md)| Team IDs | [optional] 

### Return type

[**ListWrapperOfTeamMember**](ListWrapperOfTeamMember.md)

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

# **list_teams**
> ListWrapperOfTeam list_teams(id_list=id_list)

Retrieve a list of Teams given their IDs.

Retrieve a list of Teams given their IDs. Invalid IDs in the list are ignored:  The results list is simply smaller than the list of IDs passed in. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id_list = synclient.IdList() # IdList |  (optional)

    try:
        # Retrieve a list of Teams given their IDs.
        api_response = api_instance.list_teams(id_list=id_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->list_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_list** | [**IdList**](IdList.md)|  | [optional] 

### Return type

[**ListWrapperOfTeam**](ListWrapperOfTeam.md)

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

# **remove_team_member**
> remove_team_member(id, principal_id)

Remove the given member from the specified Team.

Remove the given member from the specified Team. Note:  The client must either be a Team administrator or the member being removed. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    id = 'id_example' # str | the ID of the Team.
principal_id = 'principal_id_example' # str | the member's principal ID

    try:
        # Remove the given member from the specified Team.
        api_instance.remove_team_member(id, principal_id)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->remove_team_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. | 
 **principal_id** | **str**| the member&#39;s principal ID | 

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

# **update_team**
> Team update_team(team=team)

Update the Team metadata for the specified Team.

Update the Team metadata for the specified Team. Note: The client must be a Team administrator to make this request. 

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
    api_instance = synclient.TeamServicesApi(api_client)
    team = synclient.Team() # Team | the new metadata for the Team (optional)

    try:
        # Update the Team metadata for the specified Team.
        api_response = api_instance.update_team(team=team)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->update_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team** | [**Team**](Team.md)| the new metadata for the Team | [optional] 

### Return type

[**Team**](Team.md)

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

# **update_team_acl**
> AccessControlList update_team_acl(access_control_list=access_control_list)

Update the Access Control List for the specified Team.

Update the Access Control List for the specified Team.

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
    api_instance = synclient.TeamServicesApi(api_client)
    access_control_list = synclient.AccessControlList() # AccessControlList | the updated Access Control List (optional)

    try:
        # Update the Access Control List for the specified Team.
        api_response = api_instance.update_team_acl(access_control_list=access_control_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TeamServicesApi->update_team_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_control_list** | [**AccessControlList**](AccessControlList.md)| the updated Access Control List | [optional] 

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

