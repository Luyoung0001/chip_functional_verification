module RandomGenerator_top;

  wire  clk;
  wire  reset;
  wire [15:0] seed;
  wire [15:0] random_number;


 RandomGenerator RandomGenerator(
    .clk(clk),
    .reset(reset),
    .seed(seed),
    .random_number(random_number)
 );


endmodule
