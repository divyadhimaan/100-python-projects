
## Randomization and Python List

### Tips

- Randomization - pseudo random number generator
- Use Library module - Random
    - randrange(start, stop, step) -> between a range
    - randint(a, b) -> for int
    - random() -> float ( 0 and 1
    )

    ```
    import random
    print(random.randint(1, 10))
    ```

    For more information: Click [here](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences)

- List
    - Mutable 
    - list_name.len() // to get length of list
    - Use offset to get values from a list (starting with 0)
    ```
    example = ["apple", "orange", "banana", "mango"]
    print(example[0]) // apple
    print(example[2]) // banana
    ```
    - list_name.append() // to add value to end of the 

    For more information. Click [here](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
### Note: 

- Good to split code into smaller modules. Good for collaboration.
- Be careful about IndexError, i.e. size of the list

