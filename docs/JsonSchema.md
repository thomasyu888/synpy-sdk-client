# JsonSchema

The JSON schema is defined by: json-schema.org, specifically draft-07. Only features listed here are currently supported.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.8.2.2  | [optional] 
**ref** | **str** | https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.8.2.4.1  | [optional] 
**schema** | **str** | https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.8.1.1  | [optional] 
**const** | **str** | https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.6.1.3  | [optional] 
**_else** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**enum** | **[str]** | https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.6.1.2  | [optional] 
**_if** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**all_of** | [**[JsonSchema]**](JsonSchema.md) | Use allOf to &#39;extend&#39; or &#39;implement&#39; one or more schemas. https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.9.2.1.1  | [optional] 
**any_of** | [**[JsonSchema]**](JsonSchema.md) | https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.9.2.1.2  | [optional] 
**definitions** | [**{str: (JsonSchema,)}**](JsonSchema.md) | In an effort to support draft-07 implementations, we are using &#39;definitions&#39; instead of &#39;$defs&#39;. https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.appendix.A  | [optional] 
**description** | **str** | https://json-schema.org/draft/2019-09/json-schema-hypermedia.html#rfc.section.6.5.2&#39;  | [optional] 
**format** | **str** | https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.7.3&#39;  | [optional] 
**items** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**max_length** | **int** | https://tools.ietf.org/html/draft-handrews-json-schema-validation-02#section-6.3.1&#39; | [optional] 
**min_length** | **int** | https://tools.ietf.org/html/draft-handrews-json-schema-validation-02#section-6.3.2&#39;  | [optional] 
**one_of** | [**[JsonSchema]**](JsonSchema.md) | https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.9.2.1.3&#39;  | [optional] 
**pattern** | **str** | https://tools.ietf.org/html/draft-handrews-json-schema-validation-02#section-6.3.3  | [optional] 
**properties** | [**{str: (JsonSchema,)}**](JsonSchema.md) | https://json-schema.org/draft/2019-09/json-schema-core.html#rfc.section.9.3.2.1 | [optional] 
**required** | **[str]** | https://json-schema.org/draft/2019-09/json-schema-validation.html#rfc.section.6.5.3 | [optional] 
**source** | **str** | Used to indicate that this schema is derived from another object/schema. The value should be a URL reference to the original work. The &#39;source&#39; is solely descriptive and should have no impact on validation.  | [optional] 
**then** | [**JsonSchema**](JsonSchema.md) |  | [optional] 
**title** | **str** | https://json-schema.org/draft/2019-09/json-schema-hypermedia.html#rfc.section.6.5.1  | [optional] 
**type** | [**TYPE**](TYPE.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


