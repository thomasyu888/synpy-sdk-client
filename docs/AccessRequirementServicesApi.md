# synclient.AccessRequirementServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_access_requirement**](AccessRequirementServicesApi.md#convert_access_requirement) | **PUT** /accessRequirement/conversion | Convert an ACTAccessRequirement to a ManagedACTAccessRequirement.
[**create_access_requirement**](AccessRequirementServicesApi.md#create_access_requirement) | **POST** /accessRequirement | Add an Access Requirement to an Entity, or Team.
[**create_lock_access_requirement**](AccessRequirementServicesApi.md#create_lock_access_requirement) | **POST** /entity/{id}/lockAccessRequirement | Add a temporary access restriction that prevents access pending review by the Synapse ACT. 
[**delete_access_requirements**](AccessRequirementServicesApi.md#delete_access_requirements) | **DELETE** /accessRequirement/{requirementId} | Delete an Access Requirement.
[**get_access_requirement**](AccessRequirementServicesApi.md#get_access_requirement) | **GET** /accessRequirement/{requirementId} | Get an Access Requirement.
[**get_entity_access_requirements**](AccessRequirementServicesApi.md#get_entity_access_requirements) | **GET** /entity/{id}/accessRequirement | Retrieve paginated list of ALL Access Requirements associated with an entity.
[**get_subjects**](AccessRequirementServicesApi.md#get_subjects) | **GET** /accessRequirement/{requirementId}/subjects | Retrieve a page of subjects for a given Access Requirement ID.
[**get_team_access_requirements**](AccessRequirementServicesApi.md#get_team_access_requirements) | **GET** /team/{id}/accessRequirement | Retrieve paginated list of ALL Access Requirements associated with a Team.
[**update_access_requirement**](AccessRequirementServicesApi.md#update_access_requirement) | **PUT** /accessRequirement/{requirementId} | Modify an existing Access Requirement.


# **convert_access_requirement**
> AccessRequirement convert_access_requirement()

Convert an ACTAccessRequirement to a ManagedACTAccessRequirement.

Convert an ACTAccessRequirement to a ManagedACTAccessRequirement.  Only ACT member can perform this action. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import access_requirement_services_api
from synclient.model.access_requirement_conversion_request import AccessRequirementConversionRequest
from synclient.model.access_requirement import AccessRequirement
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
    api_instance = access_requirement_services_api.AccessRequirementServicesApi(api_client)
    access_requirement_conversion_request = AccessRequirementConversionRequest(
        access_requirement_id="access_requirement_id_example",
        current_version=3.14,
        etag="etag_example",
    ) # AccessRequirementConversionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Convert an ACTAccessRequirement to a ManagedACTAccessRequirement.
        api_response = api_instance.convert_access_requirement(access_requirement_conversion_request=access_requirement_conversion_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->convert_access_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_requirement_conversion_request** | [**AccessRequirementConversionRequest**](AccessRequirementConversionRequest.md)|  | [optional]

### Return type

[**AccessRequirement**](AccessRequirement.md)

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

# **create_access_requirement**
> AccessRequirement create_access_requirement()

Add an Access Requirement to an Entity, or Team.

Add an Access Requirement to an Entity, or Team. This service may only be used by the Synapse Access and Compliance Team. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import access_requirement_services_api
from synclient.model.access_requirement import AccessRequirement
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
    api_instance = access_requirement_services_api.AccessRequirementServicesApi(api_client)
    access_requirement = AccessRequirement(
        access_type=ACCESSTYPE("CREATE"),
        concrete_type="concrete_type_example",
        created_by="created_by_example",
        created_on="created_on_example",
        description="description_example",
        etag="etag_example",
        id=3.14,
        modified_by="modified_by_example",
        modified_on="modified_on_example",
        subject_ids=[
            RestrictableObjectDescriptor(
                id="id_example",
                type=RestrictableObjectType("ENTITY"),
            ),
        ],
        version_number=1,
    ) # AccessRequirement | the Access Requirement to create (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add an Access Requirement to an Entity, or Team.
        api_response = api_instance.create_access_requirement(access_requirement=access_requirement)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->create_access_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_requirement** | [**AccessRequirement**](AccessRequirement.md)| the Access Requirement to create | [optional]

### Return type

[**AccessRequirement**](AccessRequirement.md)

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

# **create_lock_access_requirement**
> AccessRequirement create_lock_access_requirement(id)

Add a temporary access restriction that prevents access pending review by the Synapse ACT. 

Add a temporary access restriction that prevents access pending review by the Synapse Access and Compliance Team. This service may be used only by an administrator of the specified entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import access_requirement_services_api
from synclient.model.access_requirement import AccessRequirement
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
    api_instance = access_requirement_services_api.AccessRequirementServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.

    # example passing only required values which don't have defaults set
    try:
        # Add a temporary access restriction that prevents access pending review by the Synapse ACT. 
        api_response = api_instance.create_lock_access_requirement(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->create_lock_access_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |

### Return type

[**AccessRequirement**](AccessRequirement.md)

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

# **delete_access_requirements**
> str delete_access_requirements(requirement_id)

Delete an Access Requirement.

Delete an Access Requirement. This service may only be used by the Synapse Access and Compliance Team. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import access_requirement_services_api
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
    api_instance = access_requirement_services_api.AccessRequirementServicesApi(api_client)
    requirement_id = "requirementId_example" # str | the ID of the requirement.

    # example passing only required values which don't have defaults set
    try:
        # Delete an Access Requirement.
        api_response = api_instance.delete_access_requirements(requirement_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->delete_access_requirements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requirement_id** | **str**| the ID of the requirement. |

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

# **get_access_requirement**
> AccessRequirement get_access_requirement(requirement_id)

Get an Access Requirement.

Get an Access Requirement to an Entity, or Team based on its ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import access_requirement_services_api
from synclient.model.access_requirement import AccessRequirement
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
    api_instance = access_requirement_services_api.AccessRequirementServicesApi(api_client)
    requirement_id = "requirementId_example" # str | the ID of the requirement.

    # example passing only required values which don't have defaults set
    try:
        # Get an Access Requirement.
        api_response = api_instance.get_access_requirement(requirement_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->get_access_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requirement_id** | **str**| the ID of the requirement. |

### Return type

[**AccessRequirement**](AccessRequirement.md)

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

# **get_entity_access_requirements**
> PaginatedResultsOfAccessRequirement get_entity_access_requirements(id)

Retrieve paginated list of ALL Access Requirements associated with an entity.

Retrieve paginated list of ALL Access Requirements associated with an entity. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import access_requirement_services_api
from synclient.model.paginated_results_of_access_requirement import PaginatedResultsOfAccessRequirement
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
    api_instance = access_requirement_services_api.AccessRequirementServicesApi(api_client)
    id = "id_example" # str | The ID of an Entity.
    limit = 10 # int | Limits the size of the page returned. For example, a page size of 10 require limit = 10. The maximum limit for this call is 50.  (optional)
    offset = 0 # int | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve paginated list of ALL Access Requirements associated with an entity.
        api_response = api_instance.get_entity_access_requirements(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->get_entity_access_requirements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve paginated list of ALL Access Requirements associated with an entity.
        api_response = api_instance.get_entity_access_requirements(id, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->get_entity_access_requirements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of an Entity. |
 **limit** | **int**| Limits the size of the page returned. For example, a page size of 10 require limit &#x3D; 10. The maximum limit for this call is 50.  | [optional]
 **offset** | **int**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.  | [optional]

### Return type

[**PaginatedResultsOfAccessRequirement**](PaginatedResultsOfAccessRequirement.md)

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

# **get_subjects**
> RestrictableObjectDescriptorResponse get_subjects(requirement_id)

Retrieve a page of subjects for a given Access Requirement ID.

Retrieve a page of subjects for a given Access Requirement ID.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import access_requirement_services_api
from synclient.model.restrictable_object_descriptor_response import RestrictableObjectDescriptorResponse
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
    api_instance = access_requirement_services_api.AccessRequirementServicesApi(api_client)
    requirement_id = "requirementId_example" # str | the ID of the requirement.
    next_page_token = "nextPageToken_example" # str | Next page (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a page of subjects for a given Access Requirement ID.
        api_response = api_instance.get_subjects(requirement_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->get_subjects: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve a page of subjects for a given Access Requirement ID.
        api_response = api_instance.get_subjects(requirement_id, next_page_token=next_page_token)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->get_subjects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requirement_id** | **str**| the ID of the requirement. |
 **next_page_token** | **str**| Next page | [optional]

### Return type

[**RestrictableObjectDescriptorResponse**](RestrictableObjectDescriptorResponse.md)

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

# **get_team_access_requirements**
> PaginatedResultsOfAccessRequirement get_team_access_requirements(id)

Retrieve paginated list of ALL Access Requirements associated with a Team.

Retrieve paginated list of ALL Access Requirements associated with a Team. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import access_requirement_services_api
from synclient.model.paginated_results_of_access_requirement import PaginatedResultsOfAccessRequirement
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
    api_instance = access_requirement_services_api.AccessRequirementServicesApi(api_client)
    id = "id_example" # str | the ID of the Team.
    limit = 10 # int | Limits the size of the page returned. For example, a page size of 10 require limit = 10. The maximum limit for this call is 50.  (optional) if omitted the server will use the default value of 10
    offset = 0 # int | The index of the pagination offset. For a page size of 10, the first page would be at offset = 0, and the second page would be at offset = 10.  (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # Retrieve paginated list of ALL Access Requirements associated with a Team.
        api_response = api_instance.get_team_access_requirements(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->get_team_access_requirements: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve paginated list of ALL Access Requirements associated with a Team.
        api_response = api_instance.get_team_access_requirements(id, limit=limit, offset=offset)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->get_team_access_requirements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the ID of the Team. |
 **limit** | **int**| Limits the size of the page returned. For example, a page size of 10 require limit &#x3D; 10. The maximum limit for this call is 50.  | [optional] if omitted the server will use the default value of 10
 **offset** | **int**| The index of the pagination offset. For a page size of 10, the first page would be at offset &#x3D; 0, and the second page would be at offset &#x3D; 10.  | [optional] if omitted the server will use the default value of 0

### Return type

[**PaginatedResultsOfAccessRequirement**](PaginatedResultsOfAccessRequirement.md)

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

# **update_access_requirement**
> AccessRequirement update_access_requirement(requirement_id)

Modify an existing Access Requirement.

Modify an existing Access Requirement.  This service may only be used by the Synapse Access and Compliance Team. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import access_requirement_services_api
from synclient.model.access_requirement import AccessRequirement
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
    api_instance = access_requirement_services_api.AccessRequirementServicesApi(api_client)
    requirement_id = "requirementId_example" # str | the ID of the requirement.
    access_requirement = AccessRequirement(
        access_type=ACCESSTYPE("CREATE"),
        concrete_type="concrete_type_example",
        created_by="created_by_example",
        created_on="created_on_example",
        description="description_example",
        etag="etag_example",
        id=3.14,
        modified_by="modified_by_example",
        modified_on="modified_on_example",
        subject_ids=[
            RestrictableObjectDescriptor(
                id="id_example",
                type=RestrictableObjectType("ENTITY"),
            ),
        ],
        version_number=1,
    ) # AccessRequirement | The modified Access Requirement. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Modify an existing Access Requirement.
        api_response = api_instance.update_access_requirement(requirement_id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->update_access_requirement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Modify an existing Access Requirement.
        api_response = api_instance.update_access_requirement(requirement_id, access_requirement=access_requirement)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling AccessRequirementServicesApi->update_access_requirement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **requirement_id** | **str**| the ID of the requirement. |
 **access_requirement** | [**AccessRequirement**](AccessRequirement.md)| The modified Access Requirement. | [optional]

### Return type

[**AccessRequirement**](AccessRequirement.md)

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

