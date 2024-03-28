
## Read, Write, Open Files

### Tips
- open a file ```file = open("path/to/file/file-name.txt")```
- There are modes of opening a file
    - "r" -> read [Default]
    - "w" -> write
    - "a" -> append
    - "+" -> update

- every file you open you must close it ```file.close()```
- to read a file ```file.read()```


- better way is to use 'with' keyword: autocloses the file
    ```
    with open("path/to/file/file-name.txt") as file:
        //do something with file
    ```

- File Path
    - Relative path: relative from current working directory
    - Absolute path: from root directory

    
### Notes
- If you open a file with "w" mode and it doesnot exist, It will be created
