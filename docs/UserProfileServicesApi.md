# synclient.UserProfileServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_my_own_user_bundle**](UserProfileServicesApi.md#get_my_own_user_bundle) | **GET** /user/bundle | Get the user bundle of the caller (my own bundle).
[**get_my_own_user_profile**](UserProfileServicesApi.md#get_my_own_user_profile) | **GET** /userProfile | Get the profile of the caller (my profile).
[**get_user_bundle_by_owner_id**](UserProfileServicesApi.md#get_user_bundle_by_owner_id) | **GET** /user/{id}/bundle | Get the user bundle of a specified user.
[**get_user_group_headers_by_aliases**](UserProfileServicesApi.md#get_user_group_headers_by_aliases) | **POST** /userGroupHeaders/aliases | Get Users and Groups that match the given list of aliases.
[**get_user_group_headers_by_ids**](UserProfileServicesApi.md#get_user_group_headers_by_ids) | **GET** /userGroupHeaders/batch | Batch get UserGroupHeaders.
[**get_user_group_headers_by_prefix**](UserProfileServicesApi.md#get_user_group_headers_by_prefix) | **GET** /userGroupHeaders | Get Users and Groups that match the given prefix.
[**get_user_groups**](UserProfileServicesApi.md#get_user_groups) | **GET** /userGroup | Get the user-groups in the system.
[**get_user_profile**](UserProfileServicesApi.md#get_user_profile) | **GET** /userProfile/{profileId} | Get the profile of a specified user.
[**get_user_profiles_paginated**](UserProfileServicesApi.md#get_user_profiles_paginated) | **GET** /user | Get all publicly available.
[**image_preview_redirect_url_for_user**](UserProfileServicesApi.md#image_preview_redirect_url_for_user) | **GET** /userProfile/{profileId}/image/preview | Get the actual URL of the image file associated with a user&#39;s profile.
[**image_redirect_url_for_user**](UserProfileServicesApi.md#image_redirect_url_for_user) | **GET** /userProfile/{profileId}/image | Get the actual URL of the image file associated with a user&#39;s profile.
[**list_user_profiles**](UserProfileServicesApi.md#list_user_profiles) | **POST** /userProfile | Batch get UserGroupHeaders.
[**update_user_profile**](UserProfileServicesApi.md#update_user_profile) | **PUT** /userProfile | Update your own profile.


# **get_my_own_user_bundle**
> UserBundle get_my_own_user_bundle(mask)

Get the user bundle of the caller (my own bundle).

Get the user bundle of the caller (my own bundle). <p><b>Note:</b> Private fields will be returned.</p> 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    mask = 'mask_example' # str | integer flag defining which components to include in the bundle <p> This integer is used as a bit-string of flags to specify which parts to include in the UserBundle. The mask is defined as follows: <ul> <li> UserProfile  = 0x1 </li> <li> ORCID  = 0x2 </li> <li> VerificationSubmission = 0x4 </li> <li> Is Certified = 0x8 </li> <li> Is Verified  = 0x10 </li> <li> Is ACT Member = 0x20 </li> </ul> </p> 

    try:
        # Get the user bundle of the caller (my own bundle).
        api_response = api_instance.get_my_own_user_bundle(mask)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->get_my_own_user_bundle: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mask** | **str**| integer flag defining which components to include in the bundle &lt;p&gt; This integer is used as a bit-string of flags to specify which parts to include in the UserBundle. The mask is defined as follows: &lt;ul&gt; &lt;li&gt; UserProfile  &#x3D; 0x1 &lt;/li&gt; &lt;li&gt; ORCID  &#x3D; 0x2 &lt;/li&gt; &lt;li&gt; VerificationSubmission &#x3D; 0x4 &lt;/li&gt; &lt;li&gt; Is Certified &#x3D; 0x8 &lt;/li&gt; &lt;li&gt; Is Verified  &#x3D; 0x10 &lt;/li&gt; &lt;li&gt; Is ACT Member &#x3D; 0x20 &lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;  | 

### Return type

[**UserBundle**](UserBundle.md)

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

# **get_my_own_user_profile**
> UserProfile get_my_own_user_profile()

Get the profile of the caller (my profile).

Get the profile of the caller (my profile). <p><b>Note:</b> Private user profile fields will be returned.</p>' 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    
    try:
        # Get the profile of the caller (my profile).
        api_response = api_instance.get_my_own_user_profile()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->get_my_own_user_profile: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

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

# **get_user_bundle_by_owner_id**
> UserBundle get_user_bundle_by_owner_id(id, mask)

Get the user bundle of a specified user.

Get the user bundle of a specified user. <p><b>Note:</b> Private fields (e.g. \"rStudioUrl\") are omitted unless the requester is the profile owner or an administrator.</p> 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    id = 'id_example' # str | The ID of the Synapse user.
mask = 'mask_example' # str | integer flag defining which components to include in the bundle <p> This integer is used as a bit-string of flags to specify which parts to include in the UserBundle. The mask is defined as follows: <ul> <li> UserProfile  = 0x1 </li> <li> ORCID  = 0x2 </li> <li> VerificationSubmission = 0x4 </li> <li> Is Certified = 0x8 </li> <li> Is Verified  = 0x10 </li> <li> Is ACT Member = 0x20 </li> </ul> </p> 

    try:
        # Get the user bundle of a specified user.
        api_response = api_instance.get_user_bundle_by_owner_id(id, mask)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->get_user_bundle_by_owner_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Synapse user. | 
 **mask** | **str**| integer flag defining which components to include in the bundle &lt;p&gt; This integer is used as a bit-string of flags to specify which parts to include in the UserBundle. The mask is defined as follows: &lt;ul&gt; &lt;li&gt; UserProfile  &#x3D; 0x1 &lt;/li&gt; &lt;li&gt; ORCID  &#x3D; 0x2 &lt;/li&gt; &lt;li&gt; VerificationSubmission &#x3D; 0x4 &lt;/li&gt; &lt;li&gt; Is Certified &#x3D; 0x8 &lt;/li&gt; &lt;li&gt; Is Verified  &#x3D; 0x10 &lt;/li&gt; &lt;li&gt; Is ACT Member &#x3D; 0x20 &lt;/li&gt; &lt;/ul&gt; &lt;/p&gt;  | 

### Return type

[**UserBundle**](UserBundle.md)

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

# **get_user_group_headers_by_aliases**
> UserGroupHeaderResponse get_user_group_headers_by_aliases(alias_list=alias_list)

Get Users and Groups that match the given list of aliases.

Get Users and Groups that match the given list of aliases.

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    alias_list = synclient.AliasList() # AliasList | The list of principal aliases to lookup. Each alias must be either a user name or team name. The maximum number of aliases per request is 100.  (optional)

    try:
        # Get Users and Groups that match the given list of aliases.
        api_response = api_instance.get_user_group_headers_by_aliases(alias_list=alias_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->get_user_group_headers_by_aliases: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias_list** | [**AliasList**](AliasList.md)| The list of principal aliases to lookup. Each alias must be either a user name or team name. The maximum number of aliases per request is 100.  | [optional] 

### Return type

[**UserGroupHeaderResponse**](UserGroupHeaderResponse.md)

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

# **get_user_group_headers_by_ids**
> UserGroupHeaderResponsePage get_user_group_headers_by_ids(ids, body=body)

Batch get UserGroupHeaders.

Batch get UserGroupHeaders. This fetches information about a collection of users or groups, specified by Synapse IDs. 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    ids = 'ids_example' # str | IDs are specified as request parameters at the end of the URL, separated by commas. For example: ids=1001,819 
body = None # object | Batch get UserGroupHeaders. This fetches information about a collection of users or groups, specified by Synapse IDs.  (optional)

    try:
        # Batch get UserGroupHeaders.
        api_response = api_instance.get_user_group_headers_by_ids(ids, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->get_user_group_headers_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | **str**| IDs are specified as request parameters at the end of the URL, separated by commas. For example: ids&#x3D;1001,819  | 
 **body** | **object**| Batch get UserGroupHeaders. This fetches information about a collection of users or groups, specified by Synapse IDs.  | [optional] 

### Return type

[**UserGroupHeaderResponsePage**](UserGroupHeaderResponsePage.md)

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

# **get_user_group_headers_by_prefix**
> UserGroupHeaderResponsePage get_user_group_headers_by_prefix(limit=limit, offset=offset, prefix=prefix, type_filter=type_filter)

Get Users and Groups that match the given prefix.

Get Users and Groups that match the given prefix.

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    limit = 10 # int | Limits the number of items that will be fetched for this page.  (optional) (default to 10)
offset = 0 # int | The offset index determines where this page will start from. An index of 0 is the first item.  (optional) (default to 0)
prefix = 'prefix_example' # str | The name to search for. (optional)
type_filter = 'type_filter_example' # str | Restrict the results to a type of principal. Available options: <a href=\"${org.sagebionetworks.repo.model.principal.TypeFilter}\">TypeFilter</a>.'  (optional)

    try:
        # Get Users and Groups that match the given prefix.
        api_response = api_instance.get_user_group_headers_by_prefix(limit=limit, offset=offset, prefix=prefix, type_filter=type_filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->get_user_group_headers_by_prefix: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of items that will be fetched for this page.  | [optional] [default to 10]
 **offset** | **int**| The offset index determines where this page will start from. An index of 0 is the first item.  | [optional] [default to 0]
 **prefix** | **str**| The name to search for. | [optional] 
 **type_filter** | **str**| Restrict the results to a type of principal. Available options: &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.principal.TypeFilter}\&quot;&gt;TypeFilter&lt;/a&gt;.&#39;  | [optional] 

### Return type

[**UserGroupHeaderResponsePage**](UserGroupHeaderResponsePage.md)

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

# **get_user_groups**
> PaginatedResultsOfUserGroup get_user_groups(ascending=ascending, limit=limit, offset=offset, sort=sort, body=body)

Get the user-groups in the system.

Get the user-groups in the system

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    ascending = True # bool | Return results in ascending order. (optional) (default to True)
limit = 10 # int | the maximum number of results to return. (optional) (default to 10)
offset = 0 # int | the starting index of the returned results. (optional) (default to 0)
sort = 'NONE' # str | Sort results. (optional) (default to 'NONE')
body = None # object | Get the user-groups in the system (optional)

    try:
        # Get the user-groups in the system.
        api_response = api_instance.get_user_groups(ascending=ascending, limit=limit, offset=offset, sort=sort, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->get_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ascending** | **bool**| Return results in ascending order. | [optional] [default to True]
 **limit** | **int**| the maximum number of results to return. | [optional] [default to 10]
 **offset** | **int**| the starting index of the returned results. | [optional] [default to 0]
 **sort** | **str**| Sort results. | [optional] [default to &#39;NONE&#39;]
 **body** | **object**| Get the user-groups in the system | [optional] 

### Return type

[**PaginatedResultsOfUserGroup**](PaginatedResultsOfUserGroup.md)

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

# **get_user_profile**
> UserProfile get_user_profile(profile_id)

Get the profile of a specified user.

Get the profile of a specified user. <p><b>Note:</b> Private fields (e.g. \"rStudioUrl\") are omitted unless the requester is the profile owner or an administrator.</p>' 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the Synapse user.

    try:
        # Get the profile of a specified user.
        api_response = api_instance.get_user_profile(profile_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->get_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the Synapse user. | 

### Return type

[**UserProfile**](UserProfile.md)

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

# **get_user_profiles_paginated**
> PaginatedResultsOfUserProfile get_user_profiles_paginated(ascending=ascending, limit=limit, offset=offset, sort=sort, body=body)

Get all publicly available.

Get all publicly available <a href=\"${org.sagebionetworks.repo.model.UserProfile}\">UserProfile</a> data in the system 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    ascending = True # bool | Used to indicate whether the sort direction is ascending or not. (optional) (default to True)
limit = 100 # int | Limits the number of items that will be fetched for this page  (optional) (default to 100)
offset = 0 # int | The offset index determines where this page will start from. An index of 0 is the first item. (optional) (default to 0)
sort = 'sort_example' # str | Used to indicate upon which field(s) to sort. (optional)
body = None # object | Get all publicly available <a href=\"${org.sagebionetworks.repo.model.UserProfile}\">UserProfile</a> data in the system  (optional)

    try:
        # Get all publicly available.
        api_response = api_instance.get_user_profiles_paginated(ascending=ascending, limit=limit, offset=offset, sort=sort, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->get_user_profiles_paginated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ascending** | **bool**| Used to indicate whether the sort direction is ascending or not. | [optional] [default to True]
 **limit** | **int**| Limits the number of items that will be fetched for this page  | [optional] [default to 100]
 **offset** | **int**| The offset index determines where this page will start from. An index of 0 is the first item. | [optional] [default to 0]
 **sort** | **str**| Used to indicate upon which field(s) to sort. | [optional] 
 **body** | **object**| Get all publicly available &lt;a href&#x3D;\&quot;${org.sagebionetworks.repo.model.UserProfile}\&quot;&gt;UserProfile&lt;/a&gt; data in the system  | [optional] 

### Return type

[**PaginatedResultsOfUserProfile**](PaginatedResultsOfUserProfile.md)

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

# **image_preview_redirect_url_for_user**
> str image_preview_redirect_url_for_user(profile_id, redirect=redirect)

Get the actual URL of the image file associated with a user's profile.

Get the actual URL of the image file associated with a user''s profile. <p> Note: This call will result in a HTTP temporary redirect (307), to the actual file URL if the caller meets all of the download requirements. </p> 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the Synapse user.
redirect = True # bool | When set to false, the URL will be returned as text/plain instead of redirecting.  (optional)

    try:
        # Get the actual URL of the image file associated with a user's profile.
        api_response = api_instance.image_preview_redirect_url_for_user(profile_id, redirect=redirect)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->image_preview_redirect_url_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the Synapse user. | 
 **redirect** | **bool**| When set to false, the URL will be returned as text/plain instead of redirecting.  | [optional] 

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

# **image_redirect_url_for_user**
> str image_redirect_url_for_user(profile_id, redirect=redirect)

Get the actual URL of the image file associated with a user's profile.

Get the actual URL of the image file associated with a user's profile. <p> Note: This call will result in a HTTP temporary redirect (307), to the actual file URL if the caller meets all of the download requirements. </p> 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    profile_id = 'profile_id_example' # str | The ID of the Synapse user.
redirect = True # bool | When set to false, the URL will be returned as text/plain instead of redirecting.  (optional)

    try:
        # Get the actual URL of the image file associated with a user's profile.
        api_response = api_instance.image_redirect_url_for_user(profile_id, redirect=redirect)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->image_redirect_url_for_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**| The ID of the Synapse user. | 
 **redirect** | **bool**| When set to false, the URL will be returned as text/plain instead of redirecting.  | [optional] 

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

# **list_user_profiles**
> ListWrapperOfUserProfile list_user_profiles(id_list=id_list)

Batch get UserGroupHeaders.

Batch get UserGroupHeaders. This fetches information about a collection of users or groups, specified by Synapse IDs.' 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    id_list = synclient.IdList() # IdList | IDs are specified as request parameters at the end of the URL, separated by commas. For example: ids=1001,819  (optional)

    try:
        # Batch get UserGroupHeaders.
        api_response = api_instance.list_user_profiles(id_list=id_list)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->list_user_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_list** | [**IdList**](IdList.md)| IDs are specified as request parameters at the end of the URL, separated by commas. For example: ids&#x3D;1001,819  | [optional] 

### Return type

[**ListWrapperOfUserProfile**](ListWrapperOfUserProfile.md)

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

# **update_user_profile**
> UserProfile update_user_profile(user_profile=user_profile)

Update your own profile.

Update your own profile  <p><b>Note: </b> The user associated with the UserProfile \"ownerId\" must match the identity of the caller, otherwise an Unauthorized response will occur.</p> 

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
    api_instance = synclient.UserProfileServicesApi(api_client)
    user_profile = synclient.UserProfile() # UserProfile |  (optional)

    try:
        # Update your own profile.
        api_response = api_instance.update_user_profile(user_profile=user_profile)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserProfileServicesApi->update_user_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_profile** | [**UserProfile**](UserProfile.md)|  | [optional] 

### Return type

[**UserProfile**](UserProfile.md)

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

