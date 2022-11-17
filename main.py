import pandas as pd

def equalize(df, columns_name = None, random_state = None):

    '''
    df - pandas dataframe
    columns_name - columns which used to groupby the dataframe and calc a window rolling
    random_state - shiffle strings in datafarme before stratification
    '''

    if columns_name is not None:
        columns = columns_name.copy()
    elif columns_name is None:
        columns = list(df.columns)
    
    # shuffle dataframe
    df = df.sample(df.shape[0], random_state = random_state)

    # rolling windows to get min max
    df['rolling'] = df.groupby(columns).cumcount() + 1
    max_of_window_list = df.groupby(['company'])['rolling'].max().values
    minimum_of_window = min(max_of_window_list)

    # get equalized dataframe
    stratified_df = df[df['rolling'] <= minimum_of_window]
    stratified_df.drop('rolling', axis = 1, inplace = True)

    print('top-5 rows:')
    print(stratified_df.head(5))

    return stratified_df
