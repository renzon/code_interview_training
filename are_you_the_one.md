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
0|O|X|X|X|X|X|X|X|X|X|  
1|X|O|X|X|X|X|X|X|X|X|  
2|X|X|X|X|X|O|X|X|X|X| 
3|X|X|X|O|X|X|X|X|X|X|
4|X|X|X|X|X|X| | |X|X| 
5|X|X|X|X|X|X| | |X|X| 
6|X|X| |X|X|X|X| |X| | 
7|X|X| |X| |X|X|X|X| | 
8|X|X| |X| |X|X|X|X| | 
9|X|X|X|X|X|X|X|X|O|X|


### Round 7
9I - TRUE   
0123456789 
ABFDGHJECI 
OOOO     O
Right: 5 

### Round 6
7G - FALSE  
0123456789 
ABFDJCEHGI 
OOOOXXXXXO
Right: 5 

### Round 5
2F -  TRUE 
0123456789 
ABFDJCEGHI 
OOOOXXXXXO
Right: 5 
  
### Round 4
1B - True  
0123456789 
ABEDCJFGHI 
OOXOXXXXXO
Right: 4 
  
### Round 3
3D - True  
0123456789 
ABJDCEFGHI 
OOXOXXXXXO
Right: 4   

### Round 2
0A - True  
0123456789 
ACBDEFGHIJ 
OXXOXXXXXX      
Right: 2   

### Round 1 
0F - Falso
0123456789
ABCDEFGHIJ
OOXOXXXXXX                          
Right: 3 