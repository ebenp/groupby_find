'''
Test of groupby_find in Python
'''
from groupby_find import groupby_find

if __name__ == "__main__":
    df = groupby_find('test1.xlsx', ['location_id', 'date'],'chemical_name', 'result','min')
    print(df)