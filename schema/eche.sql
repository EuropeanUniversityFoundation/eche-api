CREATE TABLE IF NOT EXISTS eche (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    proposalNumber TEXT NOT NULL,
    erasmusCode TEXT NOT NULL,
    pic TEXT NOT NULL,
    oid TEXT,
    organisationLegalName TEXT NOT NULL,
    street TEXT NOT NULL,
    postalCode TEXT,
    city TEXT NOT NULL,
    country TEXT NOT NULL,
    webpage TEXT,
    echeStartDate TEXT NOT NULL,
    echeEndDate TEXT NOT NULL,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
