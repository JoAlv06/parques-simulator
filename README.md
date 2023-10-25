# parques-simulator
Simulator of the Colombian Board Game Parques, Complete with Randomized Moves


Rules of Parques Implemented into Program:
1. Four players (Red, Green, Blue, Yellow).
2. Turn-based order (goes Red, Green, Blue, Yellow) that starts with a random color.
3. Four pieces per player at the start.
4. Two dice (numbered 1-6) are normally used (One Exception).
5. Each piece has to travel through 72 spaces to reach the end.
6. Each turn, the value of each die can be used to move one of the pieces that number of spaces forward.
7. The values of both dice can be applied to the same piece (ie. Dice 1 is 5, Dice 2 is 6, Piece Moves Forward 11 Spaces).
8. Jail zone at all corners of the board. When a piece is in the jail zone, it is unable to be played.
9. At the start of the game, the pieces of all players are in jail.
10. To get a piece out of jail, doubles (both dice have the same value) must be rolled.
11. A piece is considered active if it is not off the board, which is only achievable by the piece reaching the end of its path.
12. If all active pieces are in jail, then the player can roll up to three times. If they roll doubles, then all of their pieces are moved onto their starting tile. If no doubles are rolled, then the turn is forfeited.
13. If a player rolls doubles, then the player gets to roll again after they've played their turn. There is no limit to the number of times a player can roll consecutive doubles.
14. If, of the active pieces, some are in jail and some are free to move, then a special set of rules applies:
      If only one piece is in jail and the player rolls doubles, then the player frees the jailed piece and moves one other piece by the value of one die.
      If more than one piece is in jail and the player rolls doubles, then the player frees the jailed pieces and does not move any free pieces.
      In either case, if the player does not roll doubles, then they must apply the values of the dice to the available pieces.
15. A player cannot choose to not apply the value of a die to one piece.
16. There are two types of tiles: protected tiles and unprotected tiles
17. Multiple pieces of the same color can be on the same tile without problems.
18. There are special conditions if pieces of different colors land on the same tile.
      If the piece of one player is on an unprotected tile and the piece of an opposing player lands on the same tile, the piece that was on the tile first is sent         to their respective jail.
      If the piece of one player is on a protected tile and the piece of an opposing player lands on the same tile, the pieces can share the tile without problem.
20. The locations of the protected tiles are as follows:
      Seven spaces away from the starting tiles of each color
      Five spaces away from the space seven spaces away from the starting tiles of each color.
21. The starting tiles of each color are special. Normally, they behave as protected tiles, however, if a player has pieces in jail and an opposing player's pieces are on the first player's starting tile, if the first player rolls doubles frees their jailed pieces, and the opposing player's pieces are sent to their own jail.
22. Once a piece traverses the board and is in t
