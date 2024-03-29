
## Tkinter and Advanced Functions

### Tips
- Tkinter used for creating GUI
    
- The packer: The packer is one of Tk’s geometry-management mechanisms.

    Note that widgets do not appear until they have had their geometry specified with a geometry manager. It’s a common early mistake to leave out the geometry specification, and then be surprised when the widget is created but nothing appears. A widget will appear only after it has had, for example, the packer’s pack() method applied to it.

    Refer [here](https://docs.python.org/3/library/tkinter.html#the-packer) for documentation

- Advanced Python arguments:
    - Default argument
    - *args: Many positional arguments
        ```
        def add(*args): #this fn can expect unlimited number of arguments
            for n in args:
                print(n)
        ```
        datatype of *args is a tuple

    - **kwargs: Many keyworded arguments
        ```
        def calculate(**kwargs): #this fn expects a list of keyword arguments
            print(kwargs)

        calculate(add=5, multiply=6)
        ```
       datatype of **kwargs is a dict 


- There are alot of Tkinter widgets
    - label
    - button
    - Entry/input
    - text
    - spinbox
    - scale
    - radio-buttons
    - listbox of choices


- Tkinter layout managers:
    - pack() - default lpacks from top to bottom unless side specified
    - place() - precise positioning, have to give x and y
    - grid() - specify row and column
### Note: 
- its good to use ```.get()``` on dictionaries, as if a key doesnot exist, it will simply return None, instead of crashing
