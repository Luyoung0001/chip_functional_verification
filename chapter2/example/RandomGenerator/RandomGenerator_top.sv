module RandomGenerator_top();

  logic  clk;
  logic  reset;
  logic [15:0] seed;
  logic [15:0] random_number;


 RandomGenerator RandomGenerator(
    .clk(clk),
    .reset(reset),
    .seed(seed),
    .random_number(random_number)
 );


  export "DPI-C" function get_clkxxJUfMV2Y7Esm;
  export "DPI-C" function set_clkxxJUfMV2Y7Esm;
  export "DPI-C" function get_resetxxJUfMV2Y7Esm;
  export "DPI-C" function set_resetxxJUfMV2Y7Esm;
  export "DPI-C" function get_seedxxJUfMV2Y7Esm;
  export "DPI-C" function set_seedxxJUfMV2Y7Esm;
  export "DPI-C" function get_random_numberxxJUfMV2Y7Esm;
  export "DPI-C" function get_RandomGenerator_lfsrxxJUfMV2Y7Esm;


  function void get_clkxxJUfMV2Y7Esm;
    output logic  value;
    value=clk;
  endfunction

  function void set_clkxxJUfMV2Y7Esm;
    input logic  value;
    clk=value;
  endfunction

  function void get_resetxxJUfMV2Y7Esm;
    output logic  value;
    value=reset;
  endfunction

  function void set_resetxxJUfMV2Y7Esm;
    input logic  value;
    reset=value;
  endfunction

  function void get_seedxxJUfMV2Y7Esm;
    output logic [15:0] value;
    value=seed;
  endfunction

  function void set_seedxxJUfMV2Y7Esm;
    input logic [15:0] value;
    seed=value;
  endfunction

  function void get_random_numberxxJUfMV2Y7Esm;
    output logic [15:0] value;
    value=random_number;
  endfunction

  function void get_RandomGenerator_lfsrxxJUfMV2Y7Esm;
    output logic [15:0] value;
    value=RandomGenerator.lfsr;
  endfunction



  initial begin
    $dumpfile("RandomGenerator.fst");
    $dumpvars(0, RandomGenerator_top);
  end

  export "DPI-C" function finish_JUfMV2Y7Esm;
  function void finish_JUfMV2Y7Esm;
    $finish;
  endfunction


endmodule
