# uppercase_sql_keywords
Automatically uppercase the keywords in a .sql file

## Instructions
keywords.txt contains the list of keywords one wishes to uppercase.
Place the uppercase_keywords.py, kewyords.txt and the .sql file you wish to uppercase in the same directory.

Navigate to this directory in the console and type the following:

`python uppercase_keywords example.sql`

where example.sql is the name of the file containing the SQL code. This will generate a new file in the directory named `example_UPPER.sql`. This file will have all keywords uppercased.

## Example

Original code:


Uppercased code:

