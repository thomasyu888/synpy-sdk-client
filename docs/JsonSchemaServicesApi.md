# synclient.JsonSchemaServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organziation**](JsonSchemaServicesApi.md#create_organziation) | **POST** /schema/organization | Create a new Organization.
[**create_schema_async_get**](JsonSchemaServicesApi.md#create_schema_async_get) | **GET** /schema/type/create/async/get/{asyncToken} | Get the results of an asynchronous job that was started to create a new JSON schema. 
[**create_schema_async_start**](JsonSchemaServicesApi.md#create_schema_async_start) | **POST** /schema/type/create/async/start | Start an asynchronous job to create a new JSON schema.
[**delete_json_schema**](JsonSchemaServicesApi.md#delete_json_schema) | **DELETE** /schema/type/registered/{id} | 
[**delete_organization**](JsonSchemaServicesApi.md#delete_organization) | **DELETE** /schema/organization/{id} | Delete the identified Organization.
[**get_json_schema**](JsonSchemaServicesApi.md#get_json_schema) | **GET** /schema/type/registered/{id} | Get a registered JSON schema using its $id.
[**get_organization_acl**](JsonSchemaServicesApi.md#get_organization_acl) | **GET** /schema/organization/{id}/acl | Get the ACL associated of an Organization.
[**get_organization_by_name**](JsonSchemaServicesApi.md#get_organization_by_name) | **GET** /schema/organization | Lookup an Organization by name.
[**get_validation_schema_results**](JsonSchemaServicesApi.md#get_validation_schema_results) | **GET** /schema/type/validation/async/get/{asyncToken} | Get the results of an asynchronous job that was started to compile a &#39;validation&#39; schema for a JSON schema. 
[**list_json_schemas**](JsonSchemaServicesApi.md#list_json_schemas) | **POST** /schema/list | List all JSON schemas for an Organization.
[**list_json_schemas_versions**](JsonSchemaServicesApi.md#list_json_schemas_versions) | **POST** /schema/version/list | List the version information for each version of a given schema.
[**list_organizations**](JsonSchemaServicesApi.md#list_organizations) | **POST** /schema/organization/list | List all organizations.
[**start_get_validation_schema**](JsonSchemaServicesApi.md#start_get_validation_schema) | **POST** /schema/type/validation/async/start | Start validating JSON schema 
[**update_organization_acl**](JsonSchemaServicesApi.md#update_organization_acl) | **PUT** /schema/organization/{id}/acl | Update the AccessControlList (ACL) for the identified Organization.


# **create_organziation**
> Organization create_organziation()

Create a new Organization.

Create a new Organization by providing a unique organization name. The new Organization will have an auto-generated AcessControlList (ACL) granting the caller all relevant permission on the newly created Organization. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.create_organization_request import CreateOrganizationRequest
from synclient.model.organization import Organization
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    create_organization_request = CreateOrganizationRequest(
        organization_name="jUR,rZ#UM/?R,FpHl6$ARjbhJk C>i d'qT\{<?'es#)#iKcYM{Rag2/!KB!k@50Xh.:Ts";mGL,i&zY[P@M"lzfB+Y,Twzvu~N^z"mfqecVU{SoA{QA<Y8XX0<}J;KXm9W'g~?)DvDDLE7A'(u+-7Tfp&\`F+7b?{%@=iEPLVY*a@Arb_6cfy~~0GcD_@buY=U?otJ(e#=I@b(uK%|5-Ido{f(x#mYhedHbSAWry*4gA\uL+|1Y=xW6>DW&&m Eg[)IYQ&\[?p=P.ek~^LC\~$<5#|HB*o.:|!Szv.~L*?@&6v4UXGg0x3|5:,#c2"8&x J'k[k<E>5;m13zh"dHt9Qev+@>n,",
    ) # CreateOrganizationRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new Organization.
        api_response = api_instance.create_organziation(create_organization_request=create_organization_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->create_organziation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_organization_request** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)|  | [optional]

### Return type

[**Organization**](Organization.md)

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

# **create_schema_async_get**
> CreateSchemaResponse create_schema_async_get(async_token)

Get the results of an asynchronous job that was started to create a new JSON schema. 

Get the results of an asynchronous job that was started to create a new JSON schema.  Note: If the job has not completed, this method will return a status code of 202 (ACCEPTED) and the response body will be a AsynchronousJobStatus object. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.create_schema_response import CreateSchemaResponse
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    async_token = "asyncToken_example" # str | Forward the token returned when the job was started.

    # example passing only required values which don't have defaults set
    try:
        # Get the results of an asynchronous job that was started to create a new JSON schema. 
        api_response = api_instance.create_schema_async_get(async_token)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->create_schema_async_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_token** | **str**| Forward the token returned when the job was started. |

### Return type

[**CreateSchemaResponse**](CreateSchemaResponse.md)

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

# **create_schema_async_start**
> AsyncJobId create_schema_async_start()

Start an asynchronous job to create a new JSON schema.

Start an asynchronous job to create a new JSON schema. A JSON schema must include an $id that is a relative URL of that schema. The pseudo-BNF syntax for a valid $id is as follows:  < $id > ::= < organization name > \"-\" < schema name > [ \"-\"  < semantic version > ]  < organization name > ::= < dot separated alpha numeric >   < schema name > ::= < dot separated alpha numeric >  < semantic version > ::= See: https://semver.org/  < dot separated alpha numeric > :: = < alpha numeric > ( \".\" < alpha numeric > )*  < alpha numeric > ::= < letter > ( < identifier > )*  < letter > ::= [a-zA-Z]  < identifier > ::= < letter > | < digit >  < digit > :: = [0-9]  Take the following example, if organizationName=\"my.organization\", schemaName=\"foo.Bar.json\", and semanticVersion=\"0.1.2\", then $id=\"my.organization-foo.Bar.json-0.1.2\". Note: The semantic version is optional. When provide the semantic version is a label for a specific version that allows other schemas to reference it by its version. When a semantic version is include, that version of the schema is immutable. This means if a semantic version is included in a registered schema's $id, all $refs within the schema must also include a semantic version.  All $ref within a JSON schema must either be references to \"definitions\" within the schema or references other registered JSON schemas. References to non-registered schemas is not currently supported. To reference a registered schema $ref should equal the $id of the referenced schema. To reference the example schema from above use $ref=\"my.organization-foo.Bar.json-0.1.2\".  Note: The semantic version of a referenced schema is optional. When the semantic version is excluded in a $ref the reference is assumed to reference the latest version of the schema. So $ref=\"my.organization-foo.Bar.json\" would be a reference to the latest version of that schema. While $ref=\"my.organization-foo.Bar.json-0.1.2\" would be a reference to the version 0.1.2  To monitor the progress of the job and to get the final results use: GET /schema/type/create/async/get/{asyncToken}  Note: The caller must be granted the CREATE permission on the Organization in the schema's $id. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.create_schema_request import CreateSchemaRequest
from synclient.model.async_job_id import AsyncJobId
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    create_schema_request = CreateSchemaRequest(
        concrete_type="concrete_type_example",
        dry_run=True,
        schema=JsonSchema(
            id="id_example",
            ref="ref_example",
            schema="schema_example",
            const="const_example",
            _else={},
            enum=[
                "enum_example",
            ],
            _if={},
            all_of=[
                {},
            ],
            any_of=[
                {},
            ],
            definitions={
                "key": {},
            },
            description="description_example",
            format="format_example",
            items={},
            max_length=1,
            min_length=1,
            one_of=[
                {},
            ],
            pattern="pattern_example",
            properties={
                "key": {},
            },
            required=[
                "required_example",
            ],
            source="source_example",
            then={},
            title="title_example",
            type=TYPE("null"),
        ),
    ) # CreateSchemaRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start an asynchronous job to create a new JSON schema.
        api_response = api_instance.create_schema_async_start(create_schema_request=create_schema_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->create_schema_async_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_schema_request** | [**CreateSchemaRequest**](CreateSchemaRequest.md)|  | [optional]

### Return type

[**AsyncJobId**](AsyncJobId.md)

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

# **delete_json_schema**
> delete_json_schema(id)



Delete the given schema using its $id. If the $id excludes a semantic version, all versions of the schema will be deleted. If the $id includes a semantic version then just that version will be deleted. Caution: This operation cannot be undone.  Note: The caller must be granted the DELETE permission on the schema's organization. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    id = "id_example" # str | The $id of the schema to delete.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_json_schema(id)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->delete_json_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The $id of the schema to delete. |

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

# **delete_organization**
> str delete_organization(id)

Delete the identified Organization.

Delete the identified Organization. All schemas defined within the Organization''s name-space must first be deleted before an Organization can be deleted.  Note: The caller must be granted the DELETE permission on the Organization. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    id = "id_example" # str | The ID of the Organization.

    # example passing only required values which don't have defaults set
    try:
        # Delete the identified Organization.
        api_response = api_instance.delete_organization(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->delete_organization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Organization. |

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

# **get_json_schema**
> JsonSchema get_json_schema(id)

Get a registered JSON schema using its $id.

Get a registered JSON schema using its $id.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.json_schema import JsonSchema
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    id = "id_example" # str | The $id of the schema to delete.

    # example passing only required values which don't have defaults set
    try:
        # Get a registered JSON schema using its $id.
        api_response = api_instance.get_json_schema(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->get_json_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The $id of the schema to delete. |

### Return type

[**JsonSchema**](JsonSchema.md)

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

# **get_organization_acl**
> AccessControlList get_organization_acl(id)

Get the ACL associated of an Organization.

Get the AcessControlList (ACL) associated with the identified Organization.  Note: The caller must be granted the READ permission to get an Organization's ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    id = "id_example" # str | The ID of the Organization.

    # example passing only required values which don't have defaults set
    try:
        # Get the ACL associated of an Organization.
        api_response = api_instance.get_organization_acl(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->get_organization_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Organization. |

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

# **get_organization_by_name**
> Organization get_organization_by_name(name)

Lookup an Organization by name.

Lookup an Organization by name.

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.organization import Organization
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    name = "name_example" # str | The name of the Organization to lookup.

    # example passing only required values which don't have defaults set
    try:
        # Lookup an Organization by name.
        api_response = api_instance.get_organization_by_name(name)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->get_organization_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the Organization to lookup. |

### Return type

[**Organization**](Organization.md)

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

# **get_validation_schema_results**
> GetValidationSchemaResponse get_validation_schema_results(async_token)

Get the results of an asynchronous job that was started to compile a 'validation' schema for a JSON schema. 

Get the results of an asynchronous job that was started to compile a 'validation' schema for a JSON schema.  Note: If the job has not completed, this method will return a status code of 202 (ACCEPTED) and the response body will be a AsynchronousJobStatus object. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.get_validation_schema_response import GetValidationSchemaResponse
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    async_token = "asyncToken_example" # str | Forward the token returned when the job was started.

    # example passing only required values which don't have defaults set
    try:
        # Get the results of an asynchronous job that was started to compile a 'validation' schema for a JSON schema. 
        api_response = api_instance.get_validation_schema_results(async_token)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->get_validation_schema_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_token** | **str**| Forward the token returned when the job was started. |

### Return type

[**GetValidationSchemaResponse**](GetValidationSchemaResponse.md)

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

# **list_json_schemas**
> ListJsonSchemaInfoResponse list_json_schemas()

List all JSON schemas for an Organization.

List all JSON schemas for an Organization. Each call will return a single page of schemas. Forward the provided nextPageToken to get the next page. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.list_json_schema_info_response import ListJsonSchemaInfoResponse
from synclient.model.list_json_schema_info_request import ListJsonSchemaInfoRequest
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    list_json_schema_info_request = ListJsonSchemaInfoRequest(
        next_page_token="next_page_token_example",
        organization_name="organization_name_example",
    ) # ListJsonSchemaInfoRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all JSON schemas for an Organization.
        api_response = api_instance.list_json_schemas(list_json_schema_info_request=list_json_schema_info_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->list_json_schemas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_json_schema_info_request** | [**ListJsonSchemaInfoRequest**](ListJsonSchemaInfoRequest.md)|  | [optional]

### Return type

[**ListJsonSchemaInfoResponse**](ListJsonSchemaInfoResponse.md)

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

# **list_json_schemas_versions**
> ListJsonSchemaVersionInfoResponse list_json_schemas_versions()

List the version information for each version of a given schema.

List the version information for each version of a given schema. Each call will return a single page of results. Forward the provide nextPageToken to get the next page of results. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.list_json_schema_version_info_response import ListJsonSchemaVersionInfoResponse
from synclient.model.list_json_schema_version_info_request import ListJsonSchemaVersionInfoRequest
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    list_json_schema_version_info_request = ListJsonSchemaVersionInfoRequest(
        next_page_token="next_page_token_example",
        organization_name="organization_name_example",
        schema_name="schema_name_example",
    ) # ListJsonSchemaVersionInfoRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List the version information for each version of a given schema.
        api_response = api_instance.list_json_schemas_versions(list_json_schema_version_info_request=list_json_schema_version_info_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->list_json_schemas_versions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_json_schema_version_info_request** | [**ListJsonSchemaVersionInfoRequest**](ListJsonSchemaVersionInfoRequest.md)|  | [optional]

### Return type

[**ListJsonSchemaVersionInfoResponse**](ListJsonSchemaVersionInfoResponse.md)

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

# **list_organizations**
> ListOrganizationsResponse list_organizations()

List all organizations.

List all organizations. Each call will return a single page of Organizations. Forward the provided nextPageToken to get the next page. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.list_organizations_request import ListOrganizationsRequest
from synclient.model.list_organizations_response import ListOrganizationsResponse
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    list_organizations_request = ListOrganizationsRequest(
        next_page_token="next_page_token_example",
    ) # ListOrganizationsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all organizations.
        api_response = api_instance.list_organizations(list_organizations_request=list_organizations_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->list_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_organizations_request** | [**ListOrganizationsRequest**](ListOrganizationsRequest.md)|  | [optional]

### Return type

[**ListOrganizationsResponse**](ListOrganizationsResponse.md)

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

# **start_get_validation_schema**
> AsyncJobId start_get_validation_schema()

Start validating JSON schema 

To use a JSON schema for validation, the JSON schema plus all of its dependency schemas must be provided to a JSON schema validator. The 'validation' schema is simply a JSON schema with all of its dependencies added to the 'definitions' section of the schema, making the schema self-contained.  Use this call to start an asynchronous job that will compile the 'validation' schema for a given JSON schema $id.  To monitor the progress of the job and to get the final results use: GET /schema/type/validation/async/get/{asyncToken} 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
from synclient.model.get_validation_schema_request import GetValidationSchemaRequest
from synclient.model.async_job_id import AsyncJobId
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    get_validation_schema_request = GetValidationSchemaRequest(
        id="id_example",
        concrete_type="concrete_type_example",
    ) # GetValidationSchemaRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start validating JSON schema 
        api_response = api_instance.start_get_validation_schema(get_validation_schema_request=get_validation_schema_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->start_get_validation_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_validation_schema_request** | [**GetValidationSchemaRequest**](GetValidationSchemaRequest.md)|  | [optional]

### Return type

[**AsyncJobId**](AsyncJobId.md)

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

# **update_organization_acl**
> AccessControlList update_organization_acl(id)

Update the AccessControlList (ACL) for the identified Organization.

Update the AccessControlList (ACL) for the identified Organization.  Note: The caller must be granted the CHANGE_PERMISSIONS permission to update an Organization's ACL. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import json_schema_services_api
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
    api_instance = json_schema_services_api.JsonSchemaServicesApi(api_client)
    id = "id_example" # str | The ID of the Organization.
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
    ) # AccessControlList |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the AccessControlList (ACL) for the identified Organization.
        api_response = api_instance.update_organization_acl(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->update_organization_acl: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the AccessControlList (ACL) for the identified Organization.
        api_response = api_instance.update_organization_acl(id, access_control_list=access_control_list)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling JsonSchemaServicesApi->update_organization_acl: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Organization. |
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

