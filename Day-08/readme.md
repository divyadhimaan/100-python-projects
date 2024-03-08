
## Python Functions with Parameters

### Tips
- Functions with parameters
    ```
    def my_func(something): 
        //do this with something
        // then this

    myfunc(123) 
    ```
    here something is parameter and 123 is argument
    
    i.e. my_func expects a parameter which we will pass as an argument

- Functions can have multiple parameters as well.

- Python provides different ways of passing the arguments during the function call. 
    - Positional arguments

        Arguments are passed in the order of parameters. The order defined in the order function declaration.
        ```
        def my_func(a,b,c):
            do a
            do b
            and do c

        my_func(1,2,3)
        ```
    - Keyword arguments

        Parameter Names are used to pass the argument during the function call.
        ```
        def my_func(a,b,c):
            do a
            do b
            and do c

        my_func(b=2,a=1,c=3)
        ```

### Note: 

- For built in functions, click [here](https://docs.python.org/3/library/functions.html)
- Always test carefully for infinite loops
