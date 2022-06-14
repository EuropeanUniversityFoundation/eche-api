# Processing the ECHE list data: Country

In addition to the original ECHE list data, this script produces processed fields that convey normalized data points to be leveraged by client applications. The processed field related to the **Country** is described below.

## Matching a Country to a Country Code

The **Country** field contains country names in English, which are converted to an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code according with the applicable standards.

This API key may be useful for better interoperability with systems that store country codes, applications built for languages other than English, etc.

### Known differences between Country Codes in this API

While the `countryCode` is extracted from the `country` field, the `erasmusCodeCountryCode` is extracted from the `erasmusCode` field in accordance with the steps outlined in `02_ERASMUS.md`. In some circumstances, those codes will not match. **But why?**

In reality, the `erasmusCodePrefix` indicates the country of the entity responsible for issuing the Erasmus Code. This means, for example, that an institution in Greenland (`countryCode = GL`) will have an Erasmus Code issued in Denmark (`erasmusCodeCountryCode = DK`).

As such, differences between these country codes may be expected when dealing with particular issues of sovereignty, which are obviously outside the scope of this project. This caveat is presented for informational purposes only.
