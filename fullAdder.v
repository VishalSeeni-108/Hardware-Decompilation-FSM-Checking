//Full adder
//Takes two input bits and one carry-in bit
//Computes and returns sum

module fullAdder(a, b, cin, s, cout); 
	input wire a, b, cin; 
	output wire s, cout; 

	//Sum
	wire term1, term2, term3, term4; 
	assign term1 = ~a & ~b & cin; 
	assign term2 = ~a & b & ~cin; 
	assign term3 = a & b & cin; 
	assign term4 = a & ~b & ~cin; 

	assign s = term1 | term2 | term3 | term4; 

	//Carry out
	wire term5, term6, term7; 
	assign term5 = a & b; 
	assign term6 = b & cin; 
	assign term7 = a & cin; 
	
	assign cout = term5 | term6 | term7; 

endmodule 
	
