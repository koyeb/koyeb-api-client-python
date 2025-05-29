# koyeb.LogsApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**query_logs**](LogsApi.md#query_logs) | **GET** /v1/streams/logs/query | Query logs
[**tail_logs**](LogsApi.md#tail_logs) | **GET** /v1/streams/logs/tail | Tails logs


# **query_logs**
> QueryLogsReply query_logs(type=type, app_id=app_id, service_id=service_id, deployment_id=deployment_id, instance_id=instance_id, stream=stream, regional_deployment_id=regional_deployment_id, start=start, end=end, order=order, limit=limit, regex=regex, text=text)

Query logs

### Example

* Api Key Authentication (Bearer):

```python
import koyeb
from koyeb.models.query_logs_reply import QueryLogsReply
from koyeb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.koyeb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = koyeb.Configuration(
    host = "https://app.koyeb.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with koyeb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = koyeb.LogsApi(api_client)
    type = 'type_example' # str |  (optional)
    app_id = 'app_id_example' # str |  (optional)
    service_id = 'service_id_example' # str |  (optional)
    deployment_id = 'deployment_id_example' # str |  (optional)
    instance_id = 'instance_id_example' # str |  (optional)
    stream = 'stream_example' # str |  (optional)
    regional_deployment_id = 'regional_deployment_id_example' # str |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime | (Optional) Must always be before `end`. Defaults to 15 minutes ago. (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | (Optional) Must always be after `start`. Defaults to now. (optional)
    order = 'order_example' # str | (Optional) `asc` or `desc`. Defaults to `desc`. (optional)
    limit = 'limit_example' # str | (Optional) Defaults to 100. Maximum of 1000. (optional)
    regex = 'regex_example' # str | (Optional) Apply a regex to filter logs. Can't be used with `text`. (optional)
    text = 'text_example' # str | (Optional) Looks for this string in logs. Can't be used with `regex`. (optional)

    try:
        # Query logs
        api_response = api_instance.query_logs(type=type, app_id=app_id, service_id=service_id, deployment_id=deployment_id, instance_id=instance_id, stream=stream, regional_deployment_id=regional_deployment_id, start=start, end=end, order=order, limit=limit, regex=regex, text=text)
        print("The response of LogsApi->query_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->query_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **app_id** | **str**|  | [optional] 
 **service_id** | **str**|  | [optional] 
 **deployment_id** | **str**|  | [optional] 
 **instance_id** | **str**|  | [optional] 
 **stream** | **str**|  | [optional] 
 **regional_deployment_id** | **str**|  | [optional] 
 **start** | **datetime**| (Optional) Must always be before &#x60;end&#x60;. Defaults to 15 minutes ago. | [optional] 
 **end** | **datetime**| (Optional) Must always be after &#x60;start&#x60;. Defaults to now. | [optional] 
 **order** | **str**| (Optional) &#x60;asc&#x60; or &#x60;desc&#x60;. Defaults to &#x60;desc&#x60;. | [optional] 
 **limit** | **str**| (Optional) Defaults to 100. Maximum of 1000. | [optional] 
 **regex** | **str**| (Optional) Apply a regex to filter logs. Can&#39;t be used with &#x60;text&#x60;. | [optional] 
 **text** | **str**| (Optional) Looks for this string in logs. Can&#39;t be used with &#x60;regex&#x60;. | [optional] 

### Return type

[**QueryLogsReply**](QueryLogsReply.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Validation error |  -  |
**401** | Returned when the token is not valid. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned in case of server error. |  -  |
**503** | Service is unavailable. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tail_logs**
> StreamResultOfLogEntry tail_logs(type=type, app_id=app_id, service_id=service_id, deployment_id=deployment_id, regional_deployment_id=regional_deployment_id, instance_id=instance_id, stream=stream, start=start, limit=limit, regex=regex, text=text)

Tails logs

### Example

* Api Key Authentication (Bearer):

```python
import koyeb
from koyeb.models.stream_result_of_log_entry import StreamResultOfLogEntry
from koyeb.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.koyeb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = koyeb.Configuration(
    host = "https://app.koyeb.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with koyeb.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = koyeb.LogsApi(api_client)
    type = 'type_example' # str |  (optional)
    app_id = 'app_id_example' # str |  (optional)
    service_id = 'service_id_example' # str |  (optional)
    deployment_id = 'deployment_id_example' # str |  (optional)
    regional_deployment_id = 'regional_deployment_id_example' # str |  (optional)
    instance_id = 'instance_id_example' # str |  (optional)
    stream = 'stream_example' # str |  (optional)
    start = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
    limit = 'limit_example' # str |  (optional)
    regex = 'regex_example' # str | (Optional) Apply a regex to filter logs. Can't be used with `text`. (optional)
    text = 'text_example' # str | (Optional) Looks for this string in logs. Can't be used with `regex`. (optional)

    try:
        # Tails logs
        api_response = api_instance.tail_logs(type=type, app_id=app_id, service_id=service_id, deployment_id=deployment_id, regional_deployment_id=regional_deployment_id, instance_id=instance_id, stream=stream, start=start, limit=limit, regex=regex, text=text)
        print("The response of LogsApi->tail_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->tail_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **app_id** | **str**|  | [optional] 
 **service_id** | **str**|  | [optional] 
 **deployment_id** | **str**|  | [optional] 
 **regional_deployment_id** | **str**|  | [optional] 
 **instance_id** | **str**|  | [optional] 
 **stream** | **str**|  | [optional] 
 **start** | **datetime**|  | [optional] 
 **limit** | **str**|  | [optional] 
 **regex** | **str**| (Optional) Apply a regex to filter logs. Can&#39;t be used with &#x60;text&#x60;. | [optional] 
 **text** | **str**| (Optional) Looks for this string in logs. Can&#39;t be used with &#x60;regex&#x60;. | [optional] 

### Return type

[**StreamResultOfLogEntry**](StreamResultOfLogEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**400** | Validation error |  -  |
**401** | Returned when the token is not valid. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned in case of server error. |  -  |
**503** | Service is unavailable. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

