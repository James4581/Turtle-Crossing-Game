# Turtle-Crossing-Game
A game where a turtle has to cross the road without getting hit by a car. 

# player.py
I create a player class using the turtle library. Turtle is a small turtle shape that starts at the bottom of the screen. The turtle can only move forward and resets it's position once reaching the end of the screen.

# scoreboard.py
A scoreboard class using turtle. Adds one with user reaches end. When hit by car, ends game and displays final score. 

# car_manager.py
Created a car class. Used turtle and random python libraries to generate cars in random locations with a random color from a list. Once cars go all the way to the left, the reset. Cars also increase each level the player increases. 

# main.py
Used our classes to create a scoreboard object, player object, and 15 car objects. The user can move forward across the screen, scoring a point and resetting if reaching the top of the screen. The speed of the cars will then increase and the scoreboard will add a point. If the user is hit by a car, the game will end and display their final score. 



