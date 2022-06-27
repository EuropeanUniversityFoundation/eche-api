# Processing the ECHE list data: Erasmus Code

In addition to the original ECHE list data, this script produces processed fields that convey normalized data points to be leveraged by client applications. The processed fields related to the **Erasmus Code** are described below.

## Normalizing the Erasmus Code

The **Erasmus Code** identifier presents a challenge for client applications when used as a unique identifier due to the fact that it includes spaces (` `). Certain software is known for collapsing multiple consecutive space characters (i.e. web browsers, spreadsheet applications) leading to many known issues in real life client applications.

As such, while the original Erasmus Codes are retained, the ECHE List API also provides a normalized version of this identifier which follows a set of rules:

1. Normalized Erasmus Codes are all **uppercase**;
2. Normalized Erasmus Codes always begin with a letter;
3. Normalized Erasmus Codes always begin with a _country_ component;
4. The _country_ component has a length of **three characters**;
5. The _country_ component may have **one, two or three letters**;
6. Any _country_ component with **one letter** is followed by **two spaces**;
7. Any _country_ component with **two letters** is followed by **one space**;
8. The only known _country_ components with **three letters** are `IRL` and `LUX`;
9. The _country_ component is followed by a _city_ component;
10. The _city_ component always starts and ends with a letter;
11. The _city_ component may contain letters and hyphens;
12. The _city_ component has variable length;
13. Normalized Erasmus Codes always end with a _number_ component;
14. The _number_ component has a length of **two or three digits**;
15. The _number_ component may have a leading zero to match the above rule.

**NOTE:** the _country_ and _city_ nomenclature, in this context, is colloquial. Some caveats apply, as described further in this document.

The following regular expression encapsulates all of the above:

```
^([IRL]|[LUX]|[A-Z]{2}[ ]{1}|[A-Z]{1}[ ]{2})[A-Z][A-Z-]+[A-Z]\d{2,3}$
```

### Known differences between original and normalized Erasmus Codes

This script is mostly focused on normalizing spacing inside the Erasmus Codes, but other changes are applied and may be observed in the API output.

This script will replace **any** non alphabetical character within the _city_ component with a `-` character (hyphen).

This script will add a leading zero to **any** _number_ component with a single digit.

### Advice on displaying Erasmus Codes in HTML

Since web browsers usually collapse multiple consecutive spaces, Erasmus Codes may appear differently than how they are present in the actual markup. To avoid this effect, the following CSS rule should be applied to the `<element>` containing the Erasmus Code:

```
element {
  white-space: pre-wrap;
}
```

## Extracting the Erasmus Code prefix

After an Erasmus Code has been normalized as described above, it is possible to extract the prefix, also referred to as the _country_ component. This prefix consists of **one, two or three letters** and contains **no spaces**.

This API key may be useful for grouping entries without the need to process the Erasmus Codes, either original or normalized.

## Matching an Erasmus Code to a Country Code

The _country_ component, or prefix of a normalized Erasmus Code is also converted to an [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code, according to a known correspondence list.

This API key may be useful for grouping entries without the need to process the Erasmus Codes, either original or normalized.

## Further notes on the _country_ and _city_ components

It is not uncommon for the Erasmus Code to contain a _city_ component that is different from the `city` field, since the components in the Erasmus code are related to its issuance, and not necessarily to the physical or legal address of an institution.

The same holds true for the _country_ component - please refer to `03_COUNTRY.md` for more information on this topic.
