# uppercase_sql_keywords
Automatically uppercase the keywords in a .sql file

## Instructions
keywords.txt contains the list of possible keywords one wishes to uppercase.  
Place uppercase_keywords.py, kewyords.txt and the .sql file you wish to uppercase in the same directory.

Navigate to this directory in the console and type the following:

`python uppercase_keywords example.sql`

where example.sql is the name of the file containing the SQL code. This will generate a new file in the directory named `example_UPPER.sql`. This file will have all keywords uppercased.

## Example

Original code:
```
select
    table1.column1,
    avg(table1.column3 - table2.column4) as column2
from table1
    left join table2 on table1.column5 = table2.column2
where table1.column3 > 1
group by table1.column1;
```

Uppercased code:

```
SELECT
    table1.column1,
    AVG(table1.column3 - table2.column4) AS column2
FROM table1
    LEFT JOIN table2 ON table1.column5 = table2.column2
WHERE table1.column3 > 1
GROUP BY table1.column1;
```
