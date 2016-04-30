# Connect4-WinTracker

Author: Danny Peng

Given the list of moves that have occurred in a finished game of Connect 4, this algorithm determines which player has won and on which turn they have won.

All info taken from: https://www.reddit.com/r/dailyprogrammer/comments/3fva66/20150805_challenge_226_intermediate_connect_four/

The board is organized as rows as numbers 1-6 descending and columns as letters a-g. This was chosen to make the first moves in row 1.

    a b c d e f g
6   . . . . . . . 
5   . . . . . . . 
4   . . . . . . . 
3   . . . . . . . 
2   . . . . . . . 
1   . . . . . . . 

Input Description

Moves will be given by column only.  The players are X and O, with X going first using columns designated with an uppercase letter and O going second and moves designated with the lowercase letter of the column they chose.

C  d
D  d
D  b
C  f
C  c
B  a
A  d
G  e
E  g

Output Description

The program outputs the player ID who won, what move they won, and what final position (column and row) won. 

Example: 

X won at move 7 (with A2 B2 C2 D2)

Challenge Input

D  d
D  c    
C  c    
C  c
G  f
F  d
F  f
D  f
A  a
E  b
E  e
B  g
G  g
B  a

Challenge Output

O won at move 11 (with c1 d2 e3 f4)
