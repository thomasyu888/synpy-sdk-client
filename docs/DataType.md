# DataType

Enumeration of data types the describe the contents of objects like Tables and Files.  * SENSITIVE_DATA: The default type assigned to all Tables and Files. Sensitive_data indicates that the contents 'might' contain Protected Health Data (PHI), data with access restriction, data with special terms-of-use, or data that should not be released to the public.  * OPEN_DATA: Open_data is data that is safe to release to the public. Open_data must not include Protected Health Data (PHI), data with access restrictions, or any type of terms-of-use. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Enumeration of data types the describe the contents of objects like Tables and Files.  * SENSITIVE_DATA: The default type assigned to all Tables and Files. Sensitive_data indicates that the contents &#39;might&#39; contain Protected Health Data (PHI), data with access restriction, data with special terms-of-use, or data that should not be released to the public.  * OPEN_DATA: Open_data is data that is safe to release to the public. Open_data must not include Protected Health Data (PHI), data with access restrictions, or any type of terms-of-use.  |  must be one of ["SENSITIVE_DATA", "OPEN_DATA", ]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


