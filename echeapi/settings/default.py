"""
Local settings example.
Duplicate this file as 'local.py' which should be ignored by git.
"""

# Flask requires a secret key to display flash messages.
SECRET_KEY = ''

# ECHE list source file (Excel).
# DATA_FILENAME = 'accredited-heis-erasmus-2021-2027-mar22_en.xlsx'
# DATA_FILENAME = 'accredited-heis-erasmus-2021-2027-jul22_en_0.xlsx'
# DATA_FILENAME = 'Accredited HEIs within the Erasmus+ programme 2021-2027_17102022.xlsx'
# DATA_FILENAME = 'Accredited-HEIS-Erasmus2021-2027_11012023.xlsx'
# DATA_FILENAME = 'Accredited-HEIs-within-the-Erasmus+Programme_2021-2027-08032023.xlsx'
# DATA_FILENAME = 'Accredited-HEIs-within-the-Erasmus-Programme_2021-2027-19042023.xlsx'
# DATA_FILENAME = 'Accredited-HEIs-within-the-Erasmus-Programme_2021-2027-13062023.xlsx'
# DATA_FILENAME = 'Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027_05072023.xlsx'
# DATA_FILENAME = '20231114_List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027.xlsx'
# DATA_FILENAME = '20231220_List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027_0.xlsx'
# DATA_FILENAME = '20240223_List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027.xlsx'
# DATA_FILENAME = '08042024_List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027.xlsx'
# DATA_FILENAME = '13062024_List_of_Accredited_HEIs_within_the_Erasmus_Programme_2021-2027.xlsx'
# DATA_FILENAME = '13062024_List_of_Accredited_HEIs_within_the_Erasmus_Programme_2021-2027_0.xlsx'
# DATA_FILENAME = '_List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027_27062024.xlsx'
# DATA_FILENAME = '_List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027_13082024.xlsx'
# DATA_FILENAME = 'List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027_29082024.xlsx'
# DATA_FILENAME = 'List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027_12092024.xlsx'
# DATA_FILENAME = 'List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027_02102024.xlsx'
# DATA_FILENAME = 'List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027_25102024.xlsx'
# DATA_FILENAME = 'List_of_Accredited_HEIs_within_the_Erasmus_Programme_2021-2027_16012025.xlsx'
# DATA_FILENAME = 'List_of_Accredited_HEIs_within_the_Erasmus_Programme_2021-2027_24022025_0.xlsx'
# DATA_FILENAME = 'List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027_10042025 (1) (2).xlsx'
DATA_FILENAME = 'List_of_Accredited_HEIs_within_the_Erasmus+_Programme_2021-2027-13052025.xlsx'

# Type of data contained in the 'Country' column.
# Override base settings depending on individual DATA_FILENAME issues.
# ECHE_COUNTRY_FIELD_TYPE = 'countryName'
ECHE_COUNTRY_FIELD_TYPE = 'countryCode'

# ECHE list headers and corresponding API keys.
# Override base settings depending on individual DATA_FILENAME issues.
ECHE_HEADERS_MAP = {
    # 'Proposal Number': 'proposalNumber',
    # 'Proposal ID': 'proposalNumber',
    'Proposal number': 'proposalNumber',
    # 'Erasmus Refcode': 'proposalNumber',
    'Erasmus Code': 'erasmusCode',
    # 'Erasmus code': 'erasmusCode',
    # 'Eramus Code': 'erasmusCode',
    # 'Erasms Code': 'erasmusCode',
    # None: 'erasmusCode',
    'PIC': 'pic',
    # 'Pic': 'pic',
    'OID': 'oid',
    # 'Organisation Legal Name': 'organisationLegalName',
    'Legal Name': 'organisationLegalName',
    # 'Organisation': 'organisationLegalName',
    'Street': 'street',
    # 'Postal Code': 'postalCode',
    'Post Cd': 'postalCode',
    # 'Postal code': 'postalCode',
    'City': 'city',
    # 'Country': 'country',
    'Country Cd': 'country',
    # 'Webpage': 'webpage',
    'Website Url': 'webpage',
    # 'ECHE Start Date': 'echeStartDate',
    'Erasmus Eche Start': 'echeStartDate',
    # 'ECHE Start': 'echeStartDate',
    # 'ECHE start': 'echeStartDate',
    # 'Start Date': 'echeStartDate',
    # 'ECHE End Date': 'echeEndDate',
    'Erasmus Eche End': 'echeEndDate',
    # 'ECHE End': 'echeEndDate',
    # 'End Date': 'echeEndDate',
}

# Date formats used for string conversion.
ECHE_DATE_FORMATS = {
    # 'echeStartDate': '%d/%m/%Y',
    # 'echeStartDate': '%d-%m-%Y',
    # 'echeStartDate': '%m/%d/%Y',
    'echeStartDate': '%Y-%m-%d',
    # 'echeEndDate': '%d/%m/%Y',
    # 'echeEndDate': '%d-%m-%Y',
    'echeEndDate': "%m/%d/%Y",
}
