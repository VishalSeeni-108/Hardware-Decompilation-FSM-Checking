import pyrtl
import pyparsing
from collections import deque

with open("register_test.blif", "r") as f:
    blif = f.read()

# print(blif)

pyrtl.importexport.input_from_blif(blif, merge_io_vectors=False, clock_name='clk')

# netlist = pyrtl.working_block()
# for x in netlist.logic:
#     if(x.op == 'w'):
#         print(x)
#         print("Inputs: " + str(x.args))
#         print("Outputs: " + str(x.dests))


for log_net in pyrtl.visualization.net_graph():
    print(log_net)
    #Search for registers
    if(hasattr(log_net, 'op') and log_net.op == 'r' and hasattr(log_net, 'dests')):
            print("Register Found")
            #Perform DFS to find loops
            #Queue destinations
            destinations = deque()
            for dest in log_net.dests: #Rewrite to use net_connections to find destinations from register easier
                for pot_dest in pyrtl.visualization.net_graph():
                    if(hasattr(pot_dest, 'op') and hasattr(pot_dest, 'args')):
                        for inputs in pot_dest.args:
                            if(inputs.name == dest.name):
                                 print("Adding destination: ", pot_dest)
                                 destinations.append(pot_dest)
                                 break; 

            #Loop through destinations and search for further branches to explore. Make sure to add already
            #visited nodes to visited list
            visited = []
            loop_found = False
            for destination in destinations: #TODO - Need to fix recursive looping, Python does not allow items to be queued while iterating over the same deque, maybe use a while loop and a stack and pop off new destinations
                print("Searching destination: ", destination)
                for dest in destination.dests:
                    #Process node - check if any of the destinations of the current node is an input to the original register
                    for input in log_net.args:
                        if(dest.name == input.name):
                            print("Loop found - "  "this register" + " is a potential state register") #Need to find a way to print register name
                            loop_found = True
                            break;            
                    if(loop_found):
                        break; 

                if(loop_found): 
                    break; 

                #Queue for searching
                for pot_dest in pyrtl.visualization.net_graph():
                    if(hasattr(pot_dest, 'op') and hasattr(pot_dest, 'args')):
                        for inputs in pot_dest.args:
                            if(inputs.name == dest.name):
                                #Check for loop
                                if(not (pot_dest in visited)):
                                    destinations.append(pot_dest)
                                    break; 


print(pyrtl.working_block())

    #Find netlists where dests are inputs

#Find a register
#Perform DFS from register to find loops
#Repeat for every register 

                

#Note difference between a register *operation* (copies argument to destination) and register *objects* (i.e. WireVector objects)
#For our purposes, every register operation should have a register destination, so we can search for registers by searching for register operations