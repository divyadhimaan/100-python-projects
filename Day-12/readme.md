
## Namespaces: local and global scope

### Tips

- Local scope: Exists within the functions
    ```
    def drink_potion():
        potion_strength = 2 //local variable
        print(potion_strength)

    drink_potion()
    print(drink_strength) - ❌
    ```
- Global scope: Exists throughout the code
    ```
    potion_health = 10 //global variable
    def drink_potion():
        potion_strength = 2
        print(potion_strength)

    drink_potion()
    print(potion_health) - ✅
    ```
- Even if you use same variable names for local ad global variales -> still two different variables will be created

- Modify global variables
    ```
    enemies = 1

    def inc_enemy():
        global enemies //refer to it
        enemies += 1
    ```


### Note: 
- There is no Block scope in python
    ```
    game_level = 3
    enemies = ["skeletons", "zombie", "alein"]

    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy) //still can be accessed
    ```
 - Always name global and local variables different.

 - Use global scope for Constants (all uppercase)
