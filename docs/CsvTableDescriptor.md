# CsvTableDescriptor

The description of a csv for upload or download.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**escape_character** | **str** | The escape character to be used for escaping a separator or quote in the resulting file. The default character &#39;\\\\&#39; will be used if this is not provided by the caller.  | [optional] 
**is_first_line_header** | **bool** | Is the first line a header? The default value of &#39;true&#39; will be used if this is not provided by the caller.  | [optional] 
**line_end** | **str** | The line feed terminator to be used for the resulting file. The default value of &#39;\\n&#39; will be used if this is not provided by the caller.  | [optional] 
**quote_character** | **str** | The character to be used for quoted elements in the resulting file. The default character &#39;\&quot;&#39; will be used if this is not provided by the caller.  | [optional] 
**separator** | **str** | The delimiter to be used for separating entries in the resulting file. The default character &#39;,&#39; will be used if this is not provided by the caller. For tab-separated values use &#39;\\t&#39;  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


