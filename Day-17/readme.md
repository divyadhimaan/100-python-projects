
## Oops -  classes, attributes and methods

### Tips

- definition of class is done by using keyword 'class'
    ```
    class MyClass:
        pass
    ```

- Creating object for class:
    ```
    my_class = MyClass()
    ```

- Constructor for class: It is a method that tells what needs to be done when object/attribute is created. Usually used to initialize the attributes of the class.
    ```
    class MyClass:
        def __init__(self):
            #initialize attributes
    ```
    Constructor can also have parameters.
    ```
    class MyClass:
        def __init__(self, param1):
            self.id = param1

    my_class = MyClass(12)     
    ```

- Methods: functions associated with class

### Note: 
- Name of the class is usually in PascalCase notation
