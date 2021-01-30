# ColumnModel

A column model contains the metadata of a single column of a TableEntity
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_type** | [**ColumnType**](ColumnType.md) |  | [optional] 
**default_value** | **str** | The default value for this column. Columns of type ENTITYID, FILEHANDLEID, USERID, and LARGETEXT are not allowed to have default values.  | [optional] 
**enum_values** | **[str]** | Columns of type STRING can be constrained to an enumeration values set on this list. The maximum number of entries for an enum is 100  | [optional] 
**facet_type** | [**FacetType**](FacetType.md) |  | [optional] 
**id** | **str** | The immutable ID issued to new columns | [optional] 
**maximum_list_length** | **int** | Required if using a columnType with a \&quot;_LIST\&quot; suffix. Describes the maximum number of values that will appear in that list.  | [optional]  if omitted the server will use the default value of 100
**maximum_size** | **float** | A parameter for columnTypes with a maximum size. For example, ColumnType. STRINGs have a default maximum size of 50 characters, but can be set to a maximumSize of 1 to 1000 characters. For columnType of STRING_LIST, this limits the size of individual string elements in the list  | [optional] 
**name** | **str** | The display name of the column | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


