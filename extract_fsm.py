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
    #Perform DFS to find loops
            #Queue destinations
            destinations = deque()
            for dest in log_net.dests:
                for pot_dest in pyrtl.visualization.net_graph():
                    if(hasattr(pot_dest, 'op') and hasattr(pot_dest, 'args')):
                        for inputs in pot_dest.args:
                            if(inputs.name == dest.name):
                                 destinations.append(pot_dest)
                                 break; 

            for destination in destinations: 
                 print("Destination: ", destination)

    #Find netlists where dests are inputs

#Find a register
#Perform DFS from register to find loops
#Repeat for every register 

                

#Note difference between a register *operation* (copies argument to destination) and register *objects* (i.e. WireVector objects)
#For our purposes, every register operation should have a register destination, so we can search for registers by searching for register operations