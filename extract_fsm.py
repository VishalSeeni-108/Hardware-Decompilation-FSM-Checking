import pyrtl
import pyparsing

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

for y in pyrtl.visualization.net_graph():
    print(y)

