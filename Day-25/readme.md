
## Working with CSV files

### Tips

- CSV are used to represent tabular data.
- CSV: Comma separated values
- Use csv library for operarions on data 
    ```
    import csv
    with open(PATH) as file:
    data = csv.reader(file)
    for row in data:
        print(row)
    ```

- For pandas documentation, check [here](https://pandas.pydata.org/docs/)

    ```
    import pandas as pd

    data = pd.read_csv(PATH)
    Temperatures = data["temp"]
    ```

- What data Pandas work with?

    When working with tabular data, such as data stored in spreadsheets or databases, pandas is the right tool for you. pandas will help you to explore, clean, and process your data. 
    
- Dataframe: [here](https://pandas.pydata.org/docs/reference/frame.html)
    
    In pandas, a data table is called a DataFrame. A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

    ```In above expample data is dataframe```
    
- Series: (here)[https://pandas.pydata.org/docs/reference/series.html]

    A Pandas Series is like a column in a table. It is a one-dimensional array holding data of any type.

    ```In above expample data["temp"] is series```

-  read a csv file using pandas
    ```
    import pandas as pd
    data = pd.read_csv(PATH)
    ```
- Creating dataframe from dictionary
    ```
    data_dict = {
        "students": ["A", "B", "C"],
        "scores": [76,65,98]
    }

    df = pd.DataFrame(data_dict)
    ```
- 
### Notes
- It is very difficult to use CSV library for large datasets, use Pandas library