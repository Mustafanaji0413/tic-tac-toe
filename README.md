# Tick, Tack, Toe Game.

The perfect Tic, Tac, Toe game is a Python terminal game that runs in the Code Institute mock terminal on Heroku. Its a fun and interactive game that takes us right back to our child hood memories. Challenge yourself in a singel-player game, or get revenge from your long time rival in a multplayer game.

<img width="800" alt="Screenshot 2022-11-04 at 19 00 39" src="https://user-images.githubusercontent.com/115544231/200068450-e89c9ec2-d544-41a9-9e7d-35b73807bec5.png">

## How to play
 Tic, Tac, Toe is a singel or multiplayer game. In the game there is a board with 3 x 3 options. 

 (If multiplayer) The palyers take turn putting marks on the 3 x 3 board. The end goal of the game is to be the player that gets three of the same symbols in a row, horizontally, vertically or diagonally. The player that first gets 3 of his/her symbols in a row wins the game. 

 ## Game Rules
 A player can choose between two symbols with his opponent, usual game uses “X” and “O”.

1. The player that gets to play first will get the "X" mark (we call him/her player 1) and the player that gets to play second will get the "O" mark (we call him/her player 2).

2. Player 1 and 2 take turns making moves with Player 1 playing mark “X” and Player 2 playing mark “O”.

3. A player marks any of the 3x3 squares with his mark (“X” or “O”) and their aim is to create a straight line horizontally, vertically or diagonally with two intensions:

4. One of the players gets three of his/her marks in a row (vertically, horizontally, or diagonally) i.e. that player wins the game.

5. If no one can create a straight line with their own mark and all the positions on the board are occupied, then the game ends in a draw/tie.

## Fulfillment Plan
The fulfillment plan is as follows: 
<img>

- First the game will start with rule description on how to play.
- Under the rules there will be an example board that shows each positions number. 
- Under the example boatd is official game board.
- And under the game board there is instruciton on what to do and how to quit the game. <img>
Then Player 1 will make his/her move by placing his  “X” mark on the board. Then Player 2 will make his/her move by placing mark “O” on the board. This will keep on going until the board is full of marks.

Then the program will check if Player 1 with “X” wins or Player 2 with “O” wins and that scenario will be follows: (could be vertically, horizontally or diagonally).
<img> <img>
If none of the players win, the program will check for draw.

 ## Features
 ### Exsisting features
 
 - Board generation 
 <img>
 
 - Accepts user input
 - Checks for wins
 - Checks for draw
 - Checks for loss
 <img>

 - Input validation and error chceking
 - - You cannot enter a number samller than 1 or bigger than 9. 
 - - You must enter a number.
 - - You cannot choose a position already taken. 
 - - You can press q to quit the game. 

 <img>

 ## Future Features 
 - Play against computer. 
 - Choose dificulty level on computer.
 - keep scores.
 - Play multiple rounds

 ## Testing
 I have manually tested this project by doing the following: 
 - Passed the code through a PEP8 linter and confirmed there are no major issues.
 - given invalid inputs: strings when numbers are expected, out of bound inputs, same input that is already occupied. 

 ### Bugs
 #### Solved bugs
 - I was having difficulties on how to read number inside a string. I found the solution on stack overflow to use ".numeric". That solved my issue. 
 - I also had issues when entering a valid number it told me "Please try again". I found that the mistake I made was I had forgotten to enter what my isnum is going to return. The solution was to enter a boolian to check if i entered a number. If the boolian was true if would allow me to enter a number without any errors. 
 - Another issue a ran into was how to give the player the option to enter "q" to quit. First I tried using break to end the game, but i was not working. After spoke to tutor support and further reserch I found that we cant break because we are not in a loop. So I resorted back to boolians to solve the issue. 