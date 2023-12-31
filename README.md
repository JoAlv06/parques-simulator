# parques-simulator

This repository holds three forms of a simulation of the Colombian Board Game called Parques. The simulation is based on random moves that comply with the following ruleset:

**Rules of Parques Implemented into Program:**
1. Four players (Red, Green, Blue, Yellow).
2. Turn-based order (goes Red, Green, Blue, Yellow) that starts with a random color.
3. Four pieces per player at the start.
4. Two dice (numbered 1-6) are normally used (One Exception).
5. Each piece has to travel through 72 spaces to reach its finishing tile.
6. Each turn, the value of each die can be used to move one of the pieces that number of spaces forward.
7. The values of both dice can be applied to the same piece (ie. Dice 1 is 5, Dice 2 is 6, Piece Moves Forward 11 Spaces).
8. Jail zone on every corner of the board. When a piece is in jail, it is unable to be played.
9. At the start of the game, the pieces of all players are in jail.
10. To get a piece out of jail, doubles (both dice have the same value) must be rolled.
12. A piece is considered active if it is not on its finishing tile.
13. The game ends when the first player gets all of their pieces on the finishing tile.
14. If all active pieces are in jail, then the player can roll up to three times. If they roll doubles, then all of their pieces are moved onto their starting tile. If no doubles are rolled, then the turn is forfeited.
15. If a player rolls doubles, then the player gets to roll again after they've played their turn. There is no limit to the number of times a player can roll consecutive doubles.
16. If, of the active pieces, some are in jail and some are free to move, then a special set of rules applies:
      If only one piece is in jail and the player rolls doubles, then the player frees the jailed piece and moves one other piece by the value of one die.
      If more than one piece is in jail and the player rolls doubles, then the player frees the jailed pieces and does not move any free pieces.
      In either case, if the player does not roll doubles, then they must apply the values of the dice to the available pieces.
17. A player cannot choose not to apply the value of a die to any of their pieces.
18. There are two types of tiles: protected tiles and unprotected tiles
19. Multiple pieces of the same color can be on the same tile without problems.
20. There are special conditions if pieces of different colors land on the same tile.
      If the piece of one player is on an unprotected tile and the piece of an opposing player lands on the same tile, the piece that was on the tile first is sent         to its respective jail.
      If the piece of one player is on a protected tile and the piece of an opposing player lands on the same tile, the pieces can share the tile without problem.
21. The locations of the protected tiles are as follows:
      Seven spaces away from the starting tiles of each color
      Five spaces away from the space seven spaces away from the starting tiles of each color.
22. The starting tiles of each color are special. Normally, they behave as protected tiles, however, when a player has pieces in jail and an opposing player's pieces are on the first player's starting tile, if the first player rolls doubles and frees their jailed pieces, and the opposing player's pieces are sent to their own jail.
23. Once a piece traverses the board and passes the protected tile five spaces before its starting tile, it is now on an alternate route to its finishing tile. No piece of any other color can access this alternate route.
24. In order for a piece to land on its finishing tile, the exact value of the number of spaces that the piece is from the finishing tile must be applied to the piece (ie. no applying a value of 6 to a piece 3 spaces away from the finishing tile).
25. If there is only one active piece left on the board and it is within 6 spaces of the finishing tile, then only one die is rolled instead of two. As a side effect, no doubles can be rolled anymore for this player.
26. If there are multiple active pieces left on the board and none of them are in jail, but only one piece is actually movable (ie. there is one piece two spaces away from the finishing tile, the values of the dice are 5 and 6, and the movable piece is 8 spaces away), then the movable piece can move with the greater value of the two dice and the lower value can be thrown out.
27. A piece is unable to be moved because it is closer to the finishing tile than the lowest value of either of the die is still considered active. Therefore, even if the rest of the active pieces are in jail, the player does not get to roll up to three times as they would if all active pieces were in jail.


**First Decision:**

Per the rules laid out, different algorithms may need to be implemented in the code depending on the states of the pieces. A piece can be in four states: In Jail, Finished (Safe), Free to Move (Free), or Closer to the Finishing Tile Than The Lowest Value of the Dice (TooClose). Based on the possible permutations that the four pieces can be in, 15 different algorithms were developed. These will be labeled strat1, strat2,..., strat15. The different permutations of the states that correspond to each strat can be found in the PossiblePermutationsOfStatesOfFourPieces.tsv file.
For all of the following strats, rolling doubles implies the activation of a recursive method call to the main algorithm that chooses one of the following strats:
- strat1 - Roll Up to Three Times for Doubles. If Doubles Rolled, Free Pieces From Jail.
- strat2 - If Doubles are Rolled, Free the Pieces in Jail. Else, Move the One Free Piece.
- strat3 - If Doubles are Rolled, Free the One Piece in Jail and Move the One Free Piece. Else, Move the One Free Piece.
- strat4 - If Doubles are Rolled, Free the Pieces in Jail. Else, Decide to Move From The Two Free Pieces.
- strat5 - If Doubles are Rolled, Free the One Piece in Jail and Move One Free Piece. Else, Decide to Move From the Two Free Pieces.
- strat6 - Decide to Move From the Two Free Pieces.
- strat7 - If Doubles Are Rolled, Free the One Piece From Free and Move One Free Piece. Else, Decide to Move From the Three Free Pieces.
- strat8 - Decide to Move From the Three Free Pieces.
- strat9 - Decide to Move From the Four Free Pieces.
- strat10 - If No Doubles Are Rolled, The Turn is Skipped.
- strat11 - If Doubles Are Rolled, Free the Piece(s) From Jail. Else, the Turn is Skipped.
- strat12 - Move the One Free Piece With the Values From Both Dice. If the Sum of the Values of the Dice is Greater than the Number of Spaces the Piece is Away From the Finishing Tile, Then the Piece Moves with the Greater Value, and the Lesser Value is Thrown Out. Doubles Still Apply.
- strat13 - Like strat11, Except When the Free Piece is Within Six Spaces of the Finishing Tile, Only One Die is Rolled. 
- strat14 - Like strat11, Except When Doubles Are Rolled, Free the One Piece in Jail and Move the One Free Piece.
- strat15 - One Die. If the Value is Greater Than the Number of Spaces Between the Piece and the Finishing Tile, Then Skip the Turn.


The reason why both strat13 and strat15 exist is due to the method by which the simulator decides whether a piece is too close to the finishing tile to move. strat12 catches the cases where a piece is not considered TooClose because the values of the individual die are less than the number of spaces that the piece is away from the finishing tile, but the piece is still within 6 spaces of the finishing tile
strat14 catches the cases where the piece is considered TooClose, however, because only one die is supposed to be rolled in this case, the initial dice roll that decided that the piece was TooClose is thrown out completely in favor of rolling one single die.




**Second Decision:**

In order to be able to generate the possible moves for the simulation to choose from, four general-purpose algorithms were created, one for choosing possible moves for one piece, two pieces, three pieces, and four pieces. The criteria for choosing the possible moves of the Free pieces was based on a number assigned to each piece, based on its ability to move with the values of the dice. 
- A piece was assigned a value of 1 if it could only move the number of spaces of the die of the least value.
- A piece was assigned a value of 2 if it could move the number of spaces of the value of either die, but it could not move the number of spaces equal to the sum of the values of both dice.
- A piece was assigned a value of 3 if it could also move the number of spaces equal to the sum of the values of both dice.

The combinations of 1's, 2's, and 3's determine the number of possible moves a player has. 
- For 1 piece, there are 3 combinations
- For 2 pieces, there are 9 combinations
- For 3 pieces, there are 27 combinations
- For 4 pieces, there are 81 combinations

In order to shorten the code for the 4-piece move possibilities generator, 12 helper methods were created that could reduce the selection options from 81 options to 15 options. Each one of these helper methods is named with the following convention:
NumberOfOnes|NumberOfTwos|NumberOfThrees
ie. oneTwoOne, threeOneZero, zeroZeroFour
The combinations that correspond to each helper can be found in the Parques Possible Moves - 4Combo.tsv file

The same thing was done to shorten the code for the 3-piece move possibilities generator, which used 7 helper methods were used to reduce the selection options from 27 options to 10 options. Each one of the helper methods is named with the same convention as before.
The combinations that correspond to each helper can be found in the Parques Possible Moves - 3Combo.tsv file



**Third Decision:**

The decision on which possible move for each player to take is made randomly using a random number generator. With the working framework of a Parques simulator in place, one can theoretically implement machine-learning algorithms in order to determine the best strategies of play for this board game. 


**Different Versions of the Simulator:**

There are two text-based versions of the program available. One goes turn-by-turn at the pace of the user. The other simulates however many games of Parques as specified by user input and then gives a statistical breakdown of wins by color. 
There is one visual Python-based Processing version of the program available. This program creates a visual representation of the simulator, where one can see the game played on a 2D board.
