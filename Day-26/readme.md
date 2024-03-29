
## Dictionary and List Comprehension

### Tips
- Python Sequences: List, range, tuple, string 

- List Comprehension: 

    ```new_list = [new_item for item in list]```

- Conditional List Comprehension:

    ```new_list = [new_item for item in list if test]```


- Dictionary Comprehension:

    ```new_dict = [new_key: new_value for item in dict]```
    ```new_dict = [new_key: new_value for (key,value) in dict.items()]```

- Iterating dataframes: same way as dictionaries
    loop through rows of df

    ```
    for (index,row) in sample_df.iterrows():
        print(index)
    ```
    

### Note: 
- 
