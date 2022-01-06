
import pandas as pd
import argparse

# Python Function to groupby and find the max, crosstabbing the data

def groupby_find(file1, row_names, col_names, result_name, type, output_path = None):
    """

    :param file1: Input Excel or csv file (string)
    :param row_names: Input row names (string or list of strings)
    :param col_names: Column name make into individual columns (string)
    :param result_name: Column to use for results (string)
    :param type: Statistic to use with result_type. Choices are min, max or mean
    :param output_path: Output csv or Excel path (string)
    :return: dataframe if called by Python
    """
    # read in the file. Excel here.
    if '.xlsx' in file1:
        df = pd.read_excel(file1, sheet_name = 'Sheet1')

    # csv
    if '.csv' in file1:
        df = pd.read_csv(file1)

    if isinstance(row_names, str):
        row_names = [row_names]
    row_names.append(col_names)

    if type == 'min':
        df = df.groupby(row_names)[result_name].min().unstack()
    if type == 'max':
        df = df.groupby(row_names)[result_name].max().unstack()
    if type == 'mean':
        df = df.groupby(row_names)[result_name].mean().unstack()

    # Flatten column headers
    df = df.rename_axis(None, axis = 1).reset_index()
    if output_path:
        if '.csv' in output_path:
            df.to_csv(output_path, index = False)

        if '.xlsx' in output_path:
            df.to_excel(output_path, index = False)

    return df

# commandline usage
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Groupby and find the min or max')

    parser.add_argument('f1', metavar='file1', type=str, nargs=1,
                        help='File path of data to group by')

    parser.add_argument('rs', metavar='result_name', type=str, nargs=1,
                        help='Column to use to evaluate min, max or mean')

    parser.add_argument('cn', metavar='col_names', type=str, nargs=1,
                        help='Column to use as columns in group by')

    parser.add_argument('ty', metavar='stattype', type=str, nargs=1,
                        help='Min, max or mean type')

    parser.add_argument('o', metavar='output_path', type=str, nargs=1,
                        help='Output csv path')

    parser.add_argument('-r', '--row_names', metavar='row_names', type=str, nargs='+',
                        help='Columns to group rows on')

    args = parser.parse_args()
    groupby_find(args.f1[0], args.row_names, args.cn[0], args.rs[0], args.ty[0], args.o[0])
