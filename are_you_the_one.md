# Are You The one problem
given 10 men and 10 woman and only one set of them which has 10 perfect
couples.

## Goal

Find the perfect set of couples in 10 rounds at least to get 1 million dollars

## Rounds

There are 10 round and in each one you do, in this sequence:

1. Can test exactly one couple for match or not
2. If couple matches, can not be used any more
3. Given a set, returns the number of perfect couples, but each perfect couple
4. If there is not even one perfect couple on set, $250,000 dollars are lost

# Combinations

Men can be seen as places to be filled in a line and woman like letters
So lets say correct matching is:

0123456789
ABCDEFGHIJ

So all possible permutations is 10! = 3,628,800
 

 |A|B|C|D|E|F|G|H|I|J|
0|X|X|X|X|X|O|X|X|X|X|  
1|X|X|X|X|X|X|X|O|X|X|  
2|X|X|X|X| |X| |X|X|X| 
3|X|X|X|X| |X| |X|X|X|
4|X|X|X|X|X|X|X|X|O|X| 
5|X|X|X|X|X|X|X|X|X|O| 
6|X|X|O|X|X|X|X|X|X|X| 
7|X|X|X|O|X|X|X|X|X|X| 
8| | |X|X|X|X|X|X|X|X| 
9| | |X|X|X|X|X|X|X|X|

### Round 8 
7D
0123456789
FHEGIJCDBA
OO  O OO                      
Right: 4

### Round 7 
1H
0123456789
FHBIJACDEG
OOXXXXOOXX                    
Right: 4

### Round 6 
3J
0123456789
FHBCAIJDEG
OOXXXXXOXX                    
Right: 3 -> 6C correct, secret

### Round 5 
1H
0123456789
FHBJAICDEG
OOXXXXOOXX                      
Right: 4

### Round 4 
1C
0123456789
FHIJABCDEG
OOXXXXOOXX                       
Right: 4

### Round 3 
1A
0123456789
FIJABCDEGH
                              
Right: 1 Lost 250,000

### Round 2 
0F
0123456789
FJABCDEGHI
                              
Right: 1 Lost 250,000

### Round 1 
0E
0123456789
ABCDEFGHIJ
                              
Right: 0 Lost 250,000

