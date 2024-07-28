//Test verilog file with registers

//Simple d flip flop
module register_test(d, clk, enable, out); 
	input wire d;
    input wire clk; 
    input wire enable; 
    output reg out; 

    always @ (posedge clk) begin
        if(enable)begin 
            out <= d; 
        end
    end 
endmodule 

//Register is created, but is found only as an input to a wire - actual register is not found
	
