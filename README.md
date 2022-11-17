### Equalization of pandas strings

So we have to start from main solution - equal number of string by columns.
Shortly, we equalize strings by partitions and min max of count strings.

If we have unbalanced number of rows, we can equalize it, adding to the partition:

`new_df = equalize(df, columns_name = ['company','target'])`

![](images/image1.png?raw=true)

And we get finally equal groups of data rows:

![](images/image2.png?raw=true)
