import pyrtl

with open("example.blif", "r") as f:
    blif = f.read()

pyrtl.importexport.input_from_blif(blif, merge_io_vectors=False, clock_name='clk')

# print all of the nets
print(pyrtl.working_block())

# output to svg
with open ('example.svg', 'w') as svg:
    pyrtl.visualization.output_to_svg(svg)
