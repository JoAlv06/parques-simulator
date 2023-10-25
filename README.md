# parques-simulator
Simulator of the Colombian Board Game Parques, Complete with Randomized Moves

This repository holds two forms of a simulation of the Colombian Board Game called Parques. One is a text-based simulator in Python and the other is a visual simulator in Python formatted for use in Processing. The simulation is based on random moves that comply with the following ruleset:



Rules of Parques Implemented into Program:
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



