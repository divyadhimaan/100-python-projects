
## Oops -  Class Inheritance

### Tips
- Refer [here](https://docs.python.org/3/library/turtle.html) for turtle documentation
- Refer [here](https://trinket.io/docs/colors) for trinklet colours
    
- Class Inheritance: A class can inherit attributes and methods from another classes.
    ```
    class Fish(Animal): //add name of super class
        def __init__(self):
            super().__init__() # initialize super class 
    ```
- Slicing Lists and Tuples:

    ```list_name[start_index : end_index : step] ```


    ```
    piano_keys = [a,b,c,d,e,f,g]
    piano_keys[2:5]
    ```

### Snake Game

The Snake game is an iconic arcade-style classic where players guide a snake that elongates upon consuming scattered food items throughout the game board. In this Python rendition of Snake, players maneuver the snake using arrow keys or alternative input methods, evading collisions with walls and the snake's own body. As the snake devours food, it lengthens, intensifying the challenge of navigation. With its simplistic visuals and captivating gameplay, this Python iteration offers a reminiscent experience akin to early mobile phone games. With straightforward controls and escalating difficulty levels, the Snake game promises endless amusement for players of all ages.