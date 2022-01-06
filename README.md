# groupby_find
Groupby and pivot wider data for the min, max or mean. Useful for spreading the data on the command line.

See an example Excel file under [tests/test1.xlsx](tests/test1.xlsx)

If using an Excel file the desired sheet should be named Sheet1.

This can be imported as a function.

```
from groupby_find import groupby_find

df = groupby_find('test1.xlsx', ['location_id', 'date'],'chemical_name', 'result','min')

# an output csv or Excel file is optional.
groupby_find('test1.xlsx', ['location_id', 'date'],'chemical_name', 'result','min', 'out.csv')
```

Commandline usage is also allowed with the row_names parameter 
at the end to allow list use.

```
python groupby_find.py tests/test1.xlsx result chemical_name min out.csv -r location_id date
```