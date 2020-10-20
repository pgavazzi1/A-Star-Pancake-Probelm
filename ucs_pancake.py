#
# ucs_pancake.py
# hw 2, COMP131
# Fall 2020
#
# Simulates the pancake search problem with a UCS algorithm, and runs very 
# slowly. 
#


from pancake_fliper import Node
from queue import PriorityQueue
import time 


################# SIMULAION IMPLEMENTATION ##################

# function name: execut_flip
# Parameters: A list of integers with the correct stack of pancake numbers
#             and a index of were to start the flip from
# Returns: A list of ints with the flipped numbers
# Does: Creates a new list with a flipped set of integers compared to the 
#       original list
def execut_flip(pancake_stack, bottom_index):
    
    # Creates a temporary integer list that collects the ints to be flipped 
    # and puts them in reverse order by inserting each int at the front of the
    # Tempororary
    temp_list =[]
    for i in range( bottom_index, len(pancake_stack) ):
        temp_list.insert(0, pancake_stack[i])  
    
    # Creates a new list and poulate it with the bottom half of our temporary 
    # list 
    new_list =[0,0,0,0,0,0,0,0,0,0]
    for i in range(0, bottom_index ):
        new_list[i] = pancake_stack[i]
    
    # Inserts the flipped numbers at the end of the array 
    temp_index = 0
    for i in range( bottom_index, len(pancake_stack) ):
        new_list[i] = temp_list[temp_index]
        temp_index += 1
        
    return new_list
        



# function name: calc_path_cost
# Parameters: A node that is that parent of the one we are calculating the 
#             path cost for
# Returns: The calculated path cost 
# Does: Calculates the path cost for our new node, which is equal to 1 plus 
#       the parent node's path cost
def calc_path_cost( node_parent ):

    #Just add one for each flip
    return node_parent.backwards_cost + 1 
    
# function name: goal_test
# Parameters: list of ints which represents the stack of pancakes
# Returns: True if the stack passes the goal test, False othewise
# Does: Compares the pancake_stack list to our correct_stack list and returns
#       The result 
def goal_test( pancake_stack ) :
    
    # This is the correct order of  intergers (pancakes) that we are looking 
    # for
    correct_stack = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    if pancake_stack == correct_stack:
        return True
    return False
    



# function name: make_node
# Parameters: A node that repsents the parent node and an int that contains
#             the index we want to start our flip at 
# Returns: a newly created node
# Does: Creates new values for the path cost and pancake
#       stack; then creates a new node with these values
def make_node( node_parent, flip_index ):
    
    #Create new stack, then calculate how much effort it took to flip it
    stack_copy       = node_parent.cake_stack
    new_stack        = execut_flip( stack_copy, flip_index )
    path_cost        = calc_path_cost( node_parent )
    heuristic_cost   = 0
    
    return Node( new_stack, node_parent, path_cost, heuristic_cost )

 

# function name: check_frontier
# Parameters: A priority queue with the fronteir of nodes, and our current 
#             node
# Returns: None if we do not find a duplictae stack in the frontier, else
#          it will return the node duplicate it found
# Does: Creates a temporary queue to house the nodes in the priority queue
#       and then checks each one against our current node's stack and returns
#       the result
def check_frontier( check_node, frontier ):
    
    temp_queue = PriorityQueue()
    node_to_return = None
    i = 0
    
    # Put all of our nodes from the frontier into a tempoary queue
    while not frontier.empty():
        temp_queue.put( frontier.get() )
        i += 1
    
    # For each node in the frontier then, comapre it's pancake stack to the
    # stack of our node we are checking. If it they are not the same you can
    # add the node back into the frontier
    while not temp_queue.empty():
        temp_node = temp_queue.get()
        
        # If a node in the frontier has the same pancake stack as our node,
        # Do not add node back to frontier and save it to return latter   
        if temp_node[1].cake_stack == check_node.cake_stack:
            node_to_return = temp_node[1]
            continue
        frontier.put( temp_node )
        
    return node_to_return



# function name: check_explored
# Parameters: The node we are checking against and a list of pancake stacks 
#             we have already explored
# Returns: True if the current node contains a duplicate node that we already
#          explored, else returns false 
# Does: Goes 1 by 1 through each node in the list of already explored pancake
#       stacks and compares against the stack of our node we are checking,
#       returns the result 
def check_explored( check_node, explored_stacks ):
    
    list_length = len(explored_stacks)
    
    for i in range(0, list_length):
        if check_node.cake_stack == explored_stacks[i]:
            return True
    return False

# function name: compare_nodes
# Parameters: none
# Returns: which ever node has a lower backwards cost
# Does: compares two nodes backwards costs and returns the result
def compare_nodes( node_1, node_2 ):
    
    if node_1.backwards_cost <= node_2.backwards_cost :
        return node_1
    return node_2




# function name: a_star
# Parameters: a priority queue with the frontier of 
# Returns: A node if we find one that satifies our test, else returns FAILURE
# Does: Initizes the search with a user generated pancake stack, then searches
#       through a 
def Uniform_cost_search(pancake_stack, frontier) :
    
    #initalize the first state 
    inital_state = Node( pancake_stack, None , 0, 0 )
    frontier.put( (inital_state.total_cost , inital_state) )
    
    #Keep track of nodes we have already explored
    explored_stacks = []

    while not frontier.empty():
        
        # So it only gets the node and not the priority value, and put its
        # pancake stack into
        curr_node =  frontier.get()[1]
        print( "\nExploring node:",curr_node.cake_stack,)
        explored_stacks.append(curr_node.cake_stack)

        if goal_test( curr_node.cake_stack ):
            return curr_node
        
        #create new node for each flippable index in the pancake list
        for flip_index in range(0,9):
            new_node = make_node( curr_node, flip_index )
            curr_node.add_new_child( new_node )
            
            # check if it's pancake stack is already in the frontier or 
            # already been explored
            node_in_frontier = check_frontier( new_node, frontier )
            node_explored    = check_explored( new_node, explored_stacks )
            
            # Put node into frontier if it is not already in there and has a
            # stack that has not been explored already 
            if not node_explored and node_in_frontier == None:
                frontier.put( (new_node.total_cost , new_node) )
                
            # Put node into frontier if it is not already in there and has a
            # stack that has not been explored already 
            if node_in_frontier != None:
                node_to_add = compare_nodes( node_in_frontier, new_node )
                frontier.put( (node_to_add.total_cost , node_to_add) )
                
    #If all else fails, return FAILURE
    return 'FAILURE'
            
            
            
            
    
    
# function name: print_result
# Parameters: a variable with the result of our search which is either a node
#             with the goal pancake stack on it or 'FAILURE'
# Returns: nothing
# Does: Prints either a message about the algorithms failure or calls a 
#       function to print the path from the starting stack to the goal pancake
#       stack
def print_result(result):
   
    if result == 'FAILURE':
        print('\n\n\n##########  CANNNOT FIND PATH  ##########\n')
        
    else :
        print('\n\n\n##########  IDEAL PATH  ##########\n')
        print("Start Path:")
        print_path(result)
        print("Finished!")
        print("\nTotal Path Cost:", result.backwards_cost )
        
    
    
    
    

# function name: print_path
# Parameters: a node on the ideal path to the goal
# Returns: nothing
# Does: recursively prints the node's stack
def print_path(node):
    
    if node.parent != None:
        print_path(node.parent)
        
    print("     ", node.cake_stack)




# function name: check_num
# Parameters: a user inputed string, a list of available pancake sizes, and 
#             a listof what we currently have in the pancake stack to search
#             on
# Returns: nothing
# Does: Checks user input to make sure it can be carried out and ask for new 
#       input if need be. Then once an adequate pancake size has been given
#       by the user, add it to the stack
def check_num(user_number, available_numbers, init_stack):
    
    got_correct_number = False
    while not got_correct_number:
            
        # Run checks to make sure that first the input is a integer
        if isinstance(user_number, str) and not user_number.isdigit():
            user_number = input('Please enter a valid available number: ')
            continue
            
        # Convert to an integer and make sure it is in the correct range and
        # is still available, ask for a new inupt if not
        user_number = int(user_number)
        for i in range( 0, len( available_numbers )):
            if available_numbers[i] == user_number:
                init_stack.append(user_number)
                available_numbers.remove(user_number)
                got_correct_number = True
                break

        if not got_correct_number:
            user_number = input('Please enter a valid available number: ')
            continue 
    
    
# function name: create_stack
# Parameters: none
# Returns: a list with the the user specified order of pancakes
# Does: asks the user for input about where to oder the pancakes and creates
#       a list to pancakes
def create_stack():
    
    init_stack = []
    available_numbers= [ 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    
    for i in range(1, 11):
        print("     Current Stack:", init_stack)
        print("     available Numbers:", available_numbers)
        
        if i == 1:
            print('\nWhat available number would you like to put in the 1st '
                  'position of the stack?')
        if i >= 2:
            print('\nWhat available number would you like to put in the next '
                  'position in the stack?')
        
        user_number = input('Enter number: ')
        
        # Check to make sure th number is in the okay range
        check_num(user_number, available_numbers, init_stack)
            
        print('\n')
        
    return init_stack
        
    
# function name: main
# Parameters: none
# Returns: nothing
# Does: Starts the simulation and calls functions to get user input on a 
#       pancake stack, simulate UCS search, and print the result of the search
#       Also, added a timmer in there as a nice grace period between
#       finalizing the stack and starting the search.
#       
if __name__ == "__main__":

    print('\n\n\n##########  HELLO  ##########\n')
    print('Welcome to the UCS Pancake Flipper!')    
      
    print('\n\nNow to create our initial Pancake Stack: \n\n')
    pancake_stack = create_stack()
    frontier = PriorityQueue()
    
    # Create a timer that counts down to the start of our problem
    t = 5
    print("Starting Search with stack", pancake_stack, "in:")
    while t: 
        mins, secs = divmod(t, 60) 
        timer = '{:02d}:{:02d}'.format(mins, secs) 
        print(timer) 
        time.sleep(1) 
        t -= 1
    
    print('\n\n\n##########  STARTING SEARCH  ##########\n')
    
    result = Uniform_cost_search(pancake_stack, frontier)
    
    #Print how our function ended
    print_result(result)
    
    print("\n\n\nAll done now, Thanks for playing!")
    print("\n\n\n\n\n\n")
   
    
    