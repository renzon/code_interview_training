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
0| | | | | | | | | | |  
1| | | | | | | | | | |  
2| | | | | | | | | | | 
3| | | | | | | | | | |
4| | | | | | | | | | | 
5| | | | | | | | | | | 
6| | | | | | | | | | | 
7| | | | | | | | | | | 
8| | | | | | | | | | | 
9| | | | | | | | | | |

### Round 1 
0E
0123456789
ABCDEFGHIJ
                              
Right: 3

