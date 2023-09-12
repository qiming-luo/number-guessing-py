# number-guessing-py
## game rules:
. 0 - 20
. computer and user both guess a number
. randomly generate a number called anchor_num
. the party who guessed a number closer to the anchor_num will score 1 point
. 3 plays == a game, whoever gets 2 points will win a game
. each user has a txt file to record the number of winning games (such as computer: 1; user_name: 0)
. each user has a user_name

## steps
1. prompt: create new user or select existed user
2. if existed user, show record
3. play game, while a game finished, 1. show record; 2. ask user if continuing
4. user decided to quite, show record
