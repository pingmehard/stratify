# %%
def sample_part_on_index(df, columns_name, index, value, random_state = None):

    for i in range(len(columns_name)):
        df = df[df[columns_name[i]] == index[i]]

    return df.sample(value, random_state=random_state)

# %%
def equalize(df, target_name, columns_name = None, random_state = None):

    if columns_name is not None:
        columns = columns_name.copy()
        columns.append(target_name)
    elif columns_name is None:
        columns = list(df.columns)

    df_dict = df[columns].value_counts().to_dict()
    
    df_dict_sorted = dict(sorted(df_dict.items(), key = lambda x: x[0]))
    temp_list = []
    min_value = max(df_dict_sorted.values()) + 1
    c = 1

    for index in df_dict_sorted:

        temp_list.append(index)

        if df_dict_sorted[index] < min_value:
            min_value = df_dict_sorted[index]

        if c % 2 == 0:
            for i in temp_list:
                df_dict_sorted[i] = min_value
            temp_list = []
            min_value = max(df_dict_sorted.values()) + 1
            
        c += 1

    sampled_dataframe = pd.DataFrame(columns=df.columns)
    df_temp = df.copy()

    for index in df_dict_sorted.keys():
        
        sampled_dataframe = pd.concat([sampled_dataframe, sample_part_on_index(df_temp, columns, index = index, value = df_dict_sorted[index], random_state = random_state)])

    return sampled_dataframe


