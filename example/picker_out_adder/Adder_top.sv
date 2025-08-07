module Adder_top();

  logic [63:0] io_a;
  logic [63:0] io_b;
  logic  io_cin;
  logic [63:0] io_sum;
  logic  io_cout;


 Adder Adder(
    .io_a(io_a),
    .io_b(io_b),
    .io_cin(io_cin),
    .io_sum(io_sum),
    .io_cout(io_cout)
 );


  export "DPI-C" function get_io_axxH4jkcuxBJZy;
  export "DPI-C" function set_io_axxH4jkcuxBJZy;
  export "DPI-C" function get_io_bxxH4jkcuxBJZy;
  export "DPI-C" function set_io_bxxH4jkcuxBJZy;
  export "DPI-C" function get_io_cinxxH4jkcuxBJZy;
  export "DPI-C" function set_io_cinxxH4jkcuxBJZy;
  export "DPI-C" function get_io_sumxxH4jkcuxBJZy;
  export "DPI-C" function get_io_coutxxH4jkcuxBJZy;


  function void get_io_axxH4jkcuxBJZy;
    output logic [63:0] value;
    value=io_a;
  endfunction

  function void set_io_axxH4jkcuxBJZy;
    input logic [63:0] value;
    io_a=value;
  endfunction

  function void get_io_bxxH4jkcuxBJZy;
    output logic [63:0] value;
    value=io_b;
  endfunction

  function void set_io_bxxH4jkcuxBJZy;
    input logic [63:0] value;
    io_b=value;
  endfunction

  function void get_io_cinxxH4jkcuxBJZy;
    output logic  value;
    value=io_cin;
  endfunction

  function void set_io_cinxxH4jkcuxBJZy;
    input logic  value;
    io_cin=value;
  endfunction

  function void get_io_sumxxH4jkcuxBJZy;
    output logic [63:0] value;
    value=io_sum;
  endfunction

  function void get_io_coutxxH4jkcuxBJZy;
    output logic  value;
    value=io_cout;
  endfunction



  initial begin
    $dumpfile("Adder.fst");
    $dumpvars(0, Adder_top);
  end

  export "DPI-C" function finish_H4jkcuxBJZy;
  function void finish_H4jkcuxBJZy;
    $finish;
  endfunction


endmodule
