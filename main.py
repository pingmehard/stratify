import pandas as pd

def row_number(df: pd.DataFrame, partition_by: list | None = None, order_by: list | None = None, ascending = True) -> pd.DataFrame:
    '''
    :df: - pandas dataframe\n
    :partition_by: - divide dataframe by windows which stated in list format. New counter (1,2,3...) each new unique string sequence.\n
    :order_by: - columns which needs to be sorted\n
    :ascending: - sort order, True means that it starts from 1,2,3...a,b,c.., False - reversed\n
    '''
    if partition_by is not None:
        columns = partition_by.copy()
    elif partition_by is None:
        columns = list(df.columns)

    if order_by is not None:
        if type(ascending) == bool:
            df['row_number'] = df.sort_values(order_by, ascending=ascending).groupby(columns).cumcount() + 1
        elif type(ascending) == list:
            df['row_number'] = df.sort_values(order_by, ascending=ascending).groupby(columns).cumcount() + 1
        df = df.sort_values(order_by, ascending=ascending)
    else:
        df['row_number'] = df.groupby(columns).cumcount() + 1

    return df

def equalize(df: pd.DataFrame, columns_name: list | None = None, random_state: int | None = None) -> pd.DataFrame:

    '''
    :df: - pandas dataframe\n
    :columns_name: - columns which used to groupby the dataframe and calc a window rolling\n
    :random_state: - shiffle strings in datafarme before stratification\n
    '''

    if columns_name is not None:
        columns = columns_name.copy()
    elif columns_name is None:
        columns = list(df.columns)
    
    # shuffle dataframe
    df = df.sample(df.shape[0], random_state = random_state)

    # rolling windows to get min max
    df['rolling'] = df.groupby(columns).cumcount() + 1
    max_of_window_list = df.groupby(columns)['rolling'].max().values
    minimum_of_window = min(max_of_window_list)

    # get equalized dataframe
    stratified_df = df[df['rolling'] <= minimum_of_window]
    stratified_df.drop('rolling', axis = 1, inplace = True)

    print('top-5 rows:')
    print(stratified_df.head(5))

    return stratified_df
