import pyrtl
import pyparsing

with open("fullAdder.blif", "r") as f:
    blif = f.read()

print(blif)

pyrtl.importexport.input_from_blif(blif, merge_io_vectors=False, clock_name='clk')

#Issue reading in BLIF file - recieiving error 'pyparsing.exceptions.ParseException: Expected Keyword '.end', found '.'  (at char 275), (line:11, col:1)'