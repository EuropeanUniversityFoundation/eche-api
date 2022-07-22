# Overview

This application is designed to provide easy access to the list of institutions holding an **Erasmus Charter for Higher Education (ECHE)**, both by regular users via the UI and by client applications via the API.

The documentation contained in this section explains the steps taken from retrieving the original file published by the European Commission to making the data available for browsing.

## Original and processed data

For this application to run, the data contained in the ECHE holders list goes through different stages of processing:

1. Preprocessing on import (removing "noise" in the data), as described in `01_ECHE_DATA/01_IMPORT`;
2. Normalizing the Erasmus Code and extracting data from it, as described in `01_ECHE_DATA/02_ERASMUS`;
3. Extracting the ISO 3166-1 alpha-2 country code, as described in `01_ECHE_DATA/03_COUNTRY`.

## Additional verified data

In addition to the original ECHE holders list data and the processed data that is retrieved, this application includes subsets of verified data from trusted sources, as described in `02_VERIFIED_DATA/01_SOURCES`.
