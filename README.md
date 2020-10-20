# A-Star-Pancake-Probelm
A Project for COMP 131: Artificial Intelligence

## Search Problem Definition:

Inital State: The pancake stack we start out on. Will not have a parent node and will have a path cost of zero.
                
Actions Available: Can preform a flip of any index in its stack (Except for the last index because of you flip that, you just get the same node again with a higher cost function for the stack overall)
                             
        
Effects of Actions: Will put the nodes in reverse order from the index we want to start the flip at all the way to the end of the arry
        
Goal test: Compare the current nodes pancake stack to the one we are Targeting: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]. If they are the same we return true, else we will return false.
        

        
         
Cost Function: I implmeneted a cost function where the algorithm paid one cost for each flip it made. That is to say, the cost of the path to any node is the same number of flips it took to get to that node. This can be stated in the equation: Cost = all_previous_flips + 1 
    
Heuristic Function: I implmeneted the gap heuristic function that was given to us. For any given pancake in the stack, if the pancake below it differes by the size of our current cake by more than 1, then we add a one to  the hueristic cost of the stack as a whole. I even compare the bottom pancake to the size of the plate, which I have set to a size of 11.
                           
   
## Running The Script
To see the a* impelmentation, run:
    
    python pancake_fliper.py 

        
## Unifor Cost Search Solution
The will take a lot loneger and find a correct answer. To see impelmentation of ucs, run:
       
    python ucs_pancake.py

Although I have written an impelmentation for this, I must warn that it runs very slowly and by my calculations it takes a lot longer to run than the A* solution. So it is not the most efficant program in the world and the a* runs much faster and is more efficant. It is really neat to see how a simple heuristic function actually helps the algorithm find were it needs to go.




## Interacting with Program: 
To run the a* program, run the pancake_fliper.py and follow these instructions:
    
The program will ask for the user to input pancakes into the stack one by one, so enter a correct number and the program will move on. If one enters an incorrect size or one that is already in the stack, then the program will ask for another number until it recives correct input
        
After the stack is full, it will produce a count down to the Search and then will preform the search. It will print out every stack it is currently exploring took
    
If it has reached the goal or the frontier is empty, it will either print out a message about the ideal path to the goal or qill print one about it's failure to reach the goal, then the program terminates.

Note: To run the USC program, run the ucs_pancake.py and follow these the same instructions above.





## Asumptions/Comments:
Each node only has 9 children from flipping indexs 1-8, this is because flippling the 9th index (the top most one) will not make a different pancake stack from the one we are already on (and would increase the total cost anyway) so I never bothered to create that child
      
I made the correct for of pancakes in the array be [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], so the correct order is techincally in reverse sorted order
    
For the UCS algorithm, I used the same Node class to implment my algorithm. Since the Node class had a int that kept track of the nodes heuristic cost, I set that value to 0 for every node when running UCS



## Acknowledgements:
   
I used the following website to give me a refresher on how to implement a priority queue since I have never done it in python before: https://www.educative.io/edpresso/what-is-the-python-priority-queue
    
I used another website to help me compare figure our how to compare two 
objects since the priority queue was resorting to that: https://portingguide.readthedocs.io/en/latest/comparisons.html


## Testing:  
I tested the A* program overall by playing around and pluggin different values in different orders. I have put a couple of sample orders and they are orginized by length of time it took for the calculation to complete
    
Easy examples: [10, 9, 8, 7, 6, 1, 2, 3, 4, 5], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [4, 5, 6, 3, 10, 2, 7, 8, 1, 9]
          
Hard examples: [2, 5, 6, 7, 8, 9, 3, 1, 10, 4]
          - [7, 9, 8, 2, 10, 6, 3, 4, 1, 5]
          - [7, 6, 3, 1, 10, 9, 8, 4, 2, 5]
          - [2, 3, 4, 9, 10, 7, 8, 1, 5, 6]
          - [4, 5, 8, 9, 6, 7, 3, 10, 2, 1]
          
          
To test the UCS program, I ran simpler problems to it and checked them against the A*'s soltuions. Here are some solutions to trying
 
 UCS examples: [10, 9, 8, 7, 6, 1, 2, 3, 4, 5], [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 9, 8, 7, 6, 5, 4, 1, 3, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 10, 9, 8, 7, 6, 5, 4, 3, 2]
