# synclient.TableServicesApi

All URIs are relative to *https://repo-prod.prod.sagebase.org/repo/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snapshot**](TableServicesApi.md#create_snapshot) | **POST** /entity/{id}/table/snapshot | Request to create a new snapshot of a table.
[**csv_download_async_get**](TableServicesApi.md#csv_download_async_get) | **GET** /entity/{id}/table/download/csv/async/get/{asyncToken} | Asynchronously get the results of a csv download started with.
[**csv_download_async_start**](TableServicesApi.md#csv_download_async_start) | **POST** /entity/{id}/table/download/csv/async/start | Asynchronously start a csv download.
[**file_preview_redirect_url_for_row**](TableServicesApi.md#file_preview_redirect_url_for_row) | **GET** /entity/{id}/table/column/{columnId}/row/{rowId}/version/{versionNumber}/filepreview | Get the preview URL of the file associated with a specific version of a row and file handle column. 
[**file_redirect_url_for_row**](TableServicesApi.md#file_redirect_url_for_row) | **GET** /entity/{id}/table/column/{columnId}/row/{rowId}/version/{versionNumber}/file | Get the actual URL of the file associated with a specific version of a row and file handle column. 
[**get_column_for_table**](TableServicesApi.md#get_column_for_table) | **GET** /entity/{id}/column | Given the ID of a.
[**get_file_handles**](TableServicesApi.md#get_file_handles) | **POST** /entity/{id}/table/filehandles | .
[**get_table_transaction_result**](TableServicesApi.md#get_table_transaction_result) | **GET** /entity/{id}/table/transaction/async/get/{asyncToken} | Asynchronously get the results of a table update transaction started with.
[**query_async_get**](TableServicesApi.md#query_async_get) | **GET** /entity/{id}/table/query/async/get/{asyncToken} | Asynchronously get the results of a query started with.
[**query_async_start**](TableServicesApi.md#query_async_start) | **POST** /entity/{id}/table/query/async/start | Asynchronously start a query.
[**start_table_transaction_job**](TableServicesApi.md#start_table_transaction_job) | **POST** /entity/{id}/table/transaction/async/start | Start a table update job that will attempt to make all of the requested changes in a single transaction. 


# **create_snapshot**
> SnapshotResponse create_snapshot(id)

Request to create a new snapshot of a table.

Request to create a new snapshot of a table. The provided comment, label, and activity ID will be applied to the current version thereby creating a snapshot and locking the current version. After the snapshot is created a new version will be started with an 'in-progress' label.  NOTE: This service is for TableEntity only. Snapshots of EntityView require asynchronous processing and can be created via: POST /entity/{id}/table/transaction/async/start 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
from synclient.model.snapshot_response import SnapshotResponse
from synclient.model.snapshot_request import SnapshotRequest
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
    api_instance = table_services_api.TableServicesApi(api_client)
    id = "id_example" # str | The ID of a Table Entity.
    snapshot_request = SnapshotRequest(
        snapshot_activity_id="snapshot_activity_id_example",
        snapshot_comment="snapshot_comment_example",
        snapshot_label="snapshot_label_example",
    ) # SnapshotRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Request to create a new snapshot of a table.
        api_response = api_instance.create_snapshot(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->create_snapshot: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request to create a new snapshot of a table.
        api_response = api_instance.create_snapshot(id, snapshot_request=snapshot_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->create_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a Table Entity. |
 **snapshot_request** | [**SnapshotRequest**](SnapshotRequest.md)|  | [optional]

### Return type

[**SnapshotResponse**](SnapshotResponse.md)

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

# **csv_download_async_get**
> DownloadFromTableResult csv_download_async_get(id, async_token)

Asynchronously get the results of a csv download started with.

Asynchronously get the results of a csv download started with POST  Note: When the result is not ready yet, this method will return a status code of 202 (ACCEPTED) and the response body will be a AsynchronousJobStatus 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
from synclient.model.download_from_table_result import DownloadFromTableResult
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
    api_instance = table_services_api.TableServicesApi(api_client)
    id = "id_example" # str | The ID of a TableEntity.
    async_token = "asyncToken_example" # str | Async Token

    # example passing only required values which don't have defaults set
    try:
        # Asynchronously get the results of a csv download started with.
        api_response = api_instance.csv_download_async_get(id, async_token)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->csv_download_async_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a TableEntity. |
 **async_token** | **str**| Async Token |

### Return type

[**DownloadFromTableResult**](DownloadFromTableResult.md)

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

# **csv_download_async_start**
> AsyncJobId csv_download_async_start(id)

Asynchronously start a csv download.

Asynchronously start a csv download. Use the returned job id and  /entity/{id}/table/download/csv/async/get to get the results of the query 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
from synclient.model.async_job_id import AsyncJobId
from synclient.model.download_from_table_request import DownloadFromTableRequest
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
    api_instance = table_services_api.TableServicesApi(api_client)
    id = "id_example" # str | The ID of a TableEntity.
    download_from_table_request = DownloadFromTableRequest() # DownloadFromTableRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Asynchronously start a csv download.
        api_response = api_instance.csv_download_async_start(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->csv_download_async_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Asynchronously start a csv download.
        api_response = api_instance.csv_download_async_start(id, download_from_table_request=download_from_table_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->csv_download_async_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a TableEntity. |
 **download_from_table_request** | [**DownloadFromTableRequest**](DownloadFromTableRequest.md)|  | [optional]

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

# **file_preview_redirect_url_for_row**
> str file_preview_redirect_url_for_row(column_id, id, row_id, version_number)

Get the preview URL of the file associated with a specific version of a row and file handle column. 

Get the preview URL of the file associated with a specific version of a row and file handle column.  Note: This call will result in a HTTP temporary redirect (307), to the actual file URL if the caller meets all of the download requirements. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
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
    api_instance = table_services_api.TableServicesApi(api_client)
    column_id = "columnId_example" # str | The ID of the Table column
    id = "id_example" # str | The ID of the FileEntity to get.
    row_id = 3.14 # float | The ID of the Table Row
    version_number = 3.14 # float | The version of the Table Row
    redirect = True # bool | When set to false, the URL will be returned as text/plain instead of redirecting.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the preview URL of the file associated with a specific version of a row and file handle column. 
        api_response = api_instance.file_preview_redirect_url_for_row(column_id, id, row_id, version_number)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->file_preview_redirect_url_for_row: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the preview URL of the file associated with a specific version of a row and file handle column. 
        api_response = api_instance.file_preview_redirect_url_for_row(column_id, id, row_id, version_number, redirect=redirect)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->file_preview_redirect_url_for_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **str**| The ID of the Table column |
 **id** | **str**| The ID of the FileEntity to get. |
 **row_id** | **float**| The ID of the Table Row |
 **version_number** | **float**| The version of the Table Row |
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

# **file_redirect_url_for_row**
> str file_redirect_url_for_row(column_id, id, row_id, version_number)

Get the actual URL of the file associated with a specific version of a row and file handle column. 

Get the actual URL of the file associated with a specific version of a row and file handle column.  Note: This call will result in a HTTP temporary redirect (307), to the actual file URL if the caller meets all of the download requirements. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
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
    api_instance = table_services_api.TableServicesApi(api_client)
    column_id = "columnId_example" # str | The ID of the Table column
    id = "id_example" # str | The ID of the FileEntity to get.
    row_id = 3.14 # float | The ID of the Table Row
    version_number = 3.14 # float | The version of the Table Row
    redirect = True # bool | When set to false, the URL will be returned as text/plain instead of redirecting.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get the actual URL of the file associated with a specific version of a row and file handle column. 
        api_response = api_instance.file_redirect_url_for_row(column_id, id, row_id, version_number)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->file_redirect_url_for_row: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the actual URL of the file associated with a specific version of a row and file handle column. 
        api_response = api_instance.file_redirect_url_for_row(column_id, id, row_id, version_number, redirect=redirect)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->file_redirect_url_for_row: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **str**| The ID of the Table column |
 **id** | **str**| The ID of the FileEntity to get. |
 **row_id** | **float**| The ID of the Table Row |
 **version_number** | **float**| The version of the Table Row |
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

# **get_column_for_table**
> PaginatedColumnModels get_column_for_table(id)

Given the ID of a.

Given the ID of a <a href=\"${org.sagebionetworks.repo.model.table.TableEntity}\">TableEntity</a>, get its list of <ahref=\"${org.sagebionetworks.repo.model.table.ColumnModel}\">ColumnModels</a> that are currently assigned to the table.  <p>  <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum frequency this method can be called</td>  <td>6 calls per minute</td>  </tr>  </table>  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
from synclient.model.paginated_column_models import PaginatedColumnModels
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
    api_instance = table_services_api.TableServicesApi(api_client)
    id = "id_example" # str | The ID of a Table.

    # example passing only required values which don't have defaults set
    try:
        # Given the ID of a.
        api_response = api_instance.get_column_for_table(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->get_column_for_table: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a Table. |

### Return type

[**PaginatedColumnModels**](PaginatedColumnModels.md)

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

# **get_file_handles**
> TableFileHandleResults get_file_handles(id)

.

This method is used to get file handle information for rows in a TableEntity. The columns in the passed in RowReferenceSet need to be FILEHANDLEID columns and the rows in the passed in RowReferenceSet need to exists (a 400 will be returned if a row ID is provided that does not actually exist). The order of the returned rows of file handles is the same as the order of the rows requested, and the order of the file handles in each row is the same as the order of the columns requested.  Note: The caller must have the READ permission on the TableEntity to make this call.  <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum frequency this method can be called</td>  <td>1 calls per second</td>  </tr>  </table> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
from synclient.model.row_reference_set import RowReferenceSet
from synclient.model.table_file_handle_results import TableFileHandleResults
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
    api_instance = table_services_api.TableServicesApi(api_client)
    id = "id_example" # str | The ID of a TableEntity.
    row_reference_set = RowReferenceSet(
        etag="etag_example",
        headers=[
            SelectColumn(
                column_type=ColumnType("STRING"),
                id="id_example",
                name="name_example",
            ),
        ],
        rows=[
            RowReference(
                row_id=1,
                version_number=1,
            ),
        ],
        table_id="table_id_example",
    ) # RowReferenceSet |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # .
        api_response = api_instance.get_file_handles(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->get_file_handles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # .
        api_response = api_instance.get_file_handles(id, row_reference_set=row_reference_set)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->get_file_handles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a TableEntity. |
 **row_reference_set** | [**RowReferenceSet**](RowReferenceSet.md)|  | [optional]

### Return type

[**TableFileHandleResults**](TableFileHandleResults.md)

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

# **get_table_transaction_result**
> TableUpdateTransactionResponse get_table_transaction_result(async_token, id)

Asynchronously get the results of a table update transaction started with.

Asynchronously get the results of a table update transaction started with POST /entity/{id}/table/transaction/async/start</a>  Note: When the result is not ready yet, this method will return a status code of 202 (ACCEPTED) and the response body will be a AsynchronousJobStatus object. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
from synclient.model.table_update_transaction_response import TableUpdateTransactionResponse
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
    api_instance = table_services_api.TableServicesApi(api_client)
    async_token = "asyncToken_example" # str | The token returned when the job was started.
    id = "id_example" # str | The ID of a Table entity.

    # example passing only required values which don't have defaults set
    try:
        # Asynchronously get the results of a table update transaction started with.
        api_response = api_instance.get_table_transaction_result(async_token, id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->get_table_transaction_result: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_token** | **str**| The token returned when the job was started. |
 **id** | **str**| The ID of a Table entity. |

### Return type

[**TableUpdateTransactionResponse**](TableUpdateTransactionResponse.md)

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

# **query_async_get**
> QueryResultBundle query_async_get(async_token, id)

Asynchronously get the results of a query started with.

Asynchronously get the results of a query started with POST /entity/{id}/table/query/async/start  Note: When the result is not ready yet, this method will return a status code of 202 (ACCEPTED) and the response body will be a AsynchronousJobStatus object. 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
from synclient.model.query_result_bundle import QueryResultBundle
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
    api_instance = table_services_api.TableServicesApi(api_client)
    async_token = "asyncToken_example" # str | Async Token
    id = "id_example" # str | The ID of the TableEntity.

    # example passing only required values which don't have defaults set
    try:
        # Asynchronously get the results of a query started with.
        api_response = api_instance.query_async_get(async_token, id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->query_async_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_token** | **str**| Async Token |
 **id** | **str**| The ID of the TableEntity. |

### Return type

[**QueryResultBundle**](QueryResultBundle.md)

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

# **query_async_start**
> AsyncJobId query_async_start(id)

Asynchronously start a query.

Asynchronously start a query. Use the returned job id and GET /entity/{id}/table/query/async/get</a> to get the results of the query  Using a 'SQL like' syntax, query the current version of the rows in a single table. The following pseudo-syntax is the basic supported format:   SELECT <br>  [ALL | DISTINCT] select_expr [, select_expr ...] <br>  FROM synapse_table_id <br>  [WHERE where_condition] <br>  [GROUP BY {col_name [, [col_name * ...] } <br>  [ORDER BY {col_name [ [ASC | DESC] [, col_name [ [ASC | DESC]]}<br>  [LIMIT row_count [ OFFSET offset ]]<br>   <p>  Note: Sub-queries and joining tables is not supported.  </p>  <p>  This services depends on an index that is created/update asynchronously from table creation and update events. This means there could be short window of time when the index is inconsistent with the true state of the table. When the index is out-of-synch, then a status code of 202 (ACCEPTED) will be returned and the response body will be a TableStatus object. The TableStatus will indicates the current status of the index including how much work is remaining until the index is consistent with the truth of the table.  The 'partsMask' is an integer \"mask\" that can be combined into to request any desired part. As of this writing, the mask is defined as follows QueryBundleRequest  <ul>  <li>Query Results <i>(queryResults)</i> = 0x1</li>  <li>Query Count <i>(queryCount)</i> = 0x2</li>  <li>Select Columns <i>(selectColumns)</i> = 0x4</li>  <li>Max Rows Per Page <i>(maxRowsPerPage)</i> = 0x8</li>  <li>The Table Columns <i>(columnModels)</i> = 0x10</li>  <li>Facet statistics for each faceted column <i>(facetStatistics)</i> = 0x20</li>  <li>The sum of the file sizes <i>(sumFileSizesBytes)</i> = 0x40</li>  </ul>  </p>  <p>  For example, to request all parts, the request mask value should be: <br> 0x1 OR 0x2 OR 0x4 OR 0x8 OR 0x10 OR 0x20 OR 0x40 = 0x7F.  </p>  <p>  Note: The caller must have the READ permission on the TableEntity to make this call.  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
from synclient.model.async_job_id import AsyncJobId
from synclient.model.query_bundle_request import QueryBundleRequest
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
    api_instance = table_services_api.TableServicesApi(api_client)
    id = "id_example" # str | The ID of a TableEntity.
    query_bundle_request = QueryBundleRequest(
        concrete_type="concrete_type_example",
        entity_id="entity_id_example",
        part_mask=1,
        query=Query(
            additional_filters=[
                {},
            ],
            include_entity_etag=True,
            limit=1,
            offset=1,
            selected_facets=[
                FacetColumnRequest(
                    column_name="column_name_example",
                    concrete_type="concrete_type_example",
                ),
            ],
            sort=[
                SortItem(
                    column="column_example",
                    direction=SortDirection("ASC"),
                ),
            ],
            sql="sql_example",
        ),
    ) # QueryBundleRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Asynchronously start a query.
        api_response = api_instance.query_async_start(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->query_async_start: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Asynchronously start a query.
        api_response = api_instance.query_async_start(id, query_bundle_request=query_bundle_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->query_async_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a TableEntity. |
 **query_bundle_request** | [**QueryBundleRequest**](QueryBundleRequest.md)|  | [optional]

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

# **start_table_transaction_job**
> AsyncJobId start_table_transaction_job(id)

Start a table update job that will attempt to make all of the requested changes in a single transaction. 

Start a table update job that will attempt to make all of the requested changes in a single transaction. All updates will either succeed or fail as a unit.  All update requests must be for the same table.  <p>  Note: The caller must have the UPDATE permission on the TableEntity to make this call.  </p>  <p>  <b>Service Limits</b>  <table border=\"1\">  <tr>  <th>resource</th>  <th>limit</th>  </tr>  <tr>  <td>The maximum size of a PartialRow change </td>  <td>2 MB</td>  </tr>  <tr>  <td>The maximum size of a CSV that can be appended to a table</td>  <td>1 GB</td>  </tr>  </table>  </p> 

### Example

* Bearer (JWT) Authentication (bearerAuth):
```python
import time
import synclient
from synclient.api import table_services_api
from synclient.model.async_job_id import AsyncJobId
from synclient.model.table_update_transaction_request import TableUpdateTransactionRequest
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
    api_instance = table_services_api.TableServicesApi(api_client)
    id = "id_example" # str | The ID of a Table Entity.
    table_update_transaction_request = TableUpdateTransactionRequest(
        changes=[
            TableUpdateRequest(
                concrete_type="concrete_type_example",
                entity_id="entity_id_example",
            ),
        ],
        concrete_type="concrete_type_example",
        create_snapshot=True,
        entity_id="entity_id_example",
        snapshot_options=SnapshotRequest(
            snapshot_activity_id="snapshot_activity_id_example",
            snapshot_comment="snapshot_comment_example",
            snapshot_label="snapshot_label_example",
        ),
    ) # TableUpdateTransactionRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Start a table update job that will attempt to make all of the requested changes in a single transaction. 
        api_response = api_instance.start_table_transaction_job(id)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->start_table_transaction_job: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Start a table update job that will attempt to make all of the requested changes in a single transaction. 
        api_response = api_instance.start_table_transaction_job(id, table_update_transaction_request=table_update_transaction_request)
        pprint(api_response)
    except synclient.ApiException as e:
        print("Exception when calling TableServicesApi->start_table_transaction_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of a Table Entity. |
 **table_update_transaction_request** | [**TableUpdateTransactionRequest**](TableUpdateTransactionRequest.md)|  | [optional]

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

