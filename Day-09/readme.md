
## Dictionaries, Nesting

### Tips
- Dictionaries are key-value pairs
    ```{key: value}```
- To retreive an item from dictionary:
    ```my_dict["key1"]```
- For adding new item:
    ```my_dict["key3"] = "value3"```
- Create Empty dictionary as: 
    ```my_dict2 = {}```
- Wiping out dictionary
    ```my_dict = {}```
- Dictionaries are mutable. FOr editing an item:
    ```my_dict["key1"] = "value12"```
- Iterate over dictionary
    ```
    for key in my_dict:
        print(key)
        print(my_dict[key])
    ```
- Value of dictionary item can be a list or a dictionary as well.
    ```
        my_dict3 = {
            key: [List],
            key2: {Dict},
        }
    ```

### Note: 
- Its good practice to indent and make dictionaries more readable. 
    ```
    my_dict = {
        "key1": "value1",
        "key2": "value2,
    }
    ```
- While editing an item, if specified key does not exist, it will create a new key and assign the value to it.
- Keys in dictionary should be unique
