
## Exception handling and JSON formatting

- Errors:
    - FileNotFound
    - KeyError
    - IndexError
    - TypeError

- Catch Exceptions:
    ```
    try:
        // something that might cause exception
    except:
        //executes when exception occurs
        // can be multiple exceptions
    else:
        // executes when no exception
    finally:
        // executes no matter what happens
    ```

- Raise exception
    ```
        raise KeyError
    ```

- JSON is composed of bunch of nested list and dictionaries.
- JSON library
    - Write: json.dump() -> dict to json
    - Read: json.load() -> json to dict
    - Update: json.update()
- Refer [here](https://docs.python.org/3/library/json.html#module-json) for json documentation

## Nato Phonetics

- Error handling: Code now handles the keyError, if user enters digits/symbols instead of alphabets

## Password Manager

- Search Functionality: Based on the website name
- Better data storage: JSON file.