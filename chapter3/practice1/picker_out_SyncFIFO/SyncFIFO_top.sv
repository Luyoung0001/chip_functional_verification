module SyncFIFO_top();

  logic  clk;
  logic  rst_n;
  logic  we_i;
  logic  re_i;
  logic [31:0] data_i;
  logic [31:0] data_o;
  logic  full_o;
  logic  empty_o;


 SyncFIFO SyncFIFO(
    .clk(clk),
    .rst_n(rst_n),
    .we_i(we_i),
    .re_i(re_i),
    .data_i(data_i),
    .data_o(data_o),
    .full_o(full_o),
    .empty_o(empty_o)
 );


  export "DPI-C" function get_clkxxPfBDHOMXaxQ;
  export "DPI-C" function set_clkxxPfBDHOMXaxQ;
  export "DPI-C" function get_rst_nxxPfBDHOMXaxQ;
  export "DPI-C" function set_rst_nxxPfBDHOMXaxQ;
  export "DPI-C" function get_we_ixxPfBDHOMXaxQ;
  export "DPI-C" function set_we_ixxPfBDHOMXaxQ;
  export "DPI-C" function get_re_ixxPfBDHOMXaxQ;
  export "DPI-C" function set_re_ixxPfBDHOMXaxQ;
  export "DPI-C" function get_data_ixxPfBDHOMXaxQ;
  export "DPI-C" function set_data_ixxPfBDHOMXaxQ;
  export "DPI-C" function get_data_oxxPfBDHOMXaxQ;
  export "DPI-C" function get_full_oxxPfBDHOMXaxQ;
  export "DPI-C" function get_empty_oxxPfBDHOMXaxQ;


  function void get_clkxxPfBDHOMXaxQ;
    output logic  value;
    value=clk;
  endfunction

  function void set_clkxxPfBDHOMXaxQ;
    input logic  value;
    clk=value;
  endfunction

  function void get_rst_nxxPfBDHOMXaxQ;
    output logic  value;
    value=rst_n;
  endfunction

  function void set_rst_nxxPfBDHOMXaxQ;
    input logic  value;
    rst_n=value;
  endfunction

  function void get_we_ixxPfBDHOMXaxQ;
    output logic  value;
    value=we_i;
  endfunction

  function void set_we_ixxPfBDHOMXaxQ;
    input logic  value;
    we_i=value;
  endfunction

  function void get_re_ixxPfBDHOMXaxQ;
    output logic  value;
    value=re_i;
  endfunction

  function void set_re_ixxPfBDHOMXaxQ;
    input logic  value;
    re_i=value;
  endfunction

  function void get_data_ixxPfBDHOMXaxQ;
    output logic [31:0] value;
    value=data_i;
  endfunction

  function void set_data_ixxPfBDHOMXaxQ;
    input logic [31:0] value;
    data_i=value;
  endfunction

  function void get_data_oxxPfBDHOMXaxQ;
    output logic [31:0] value;
    value=data_o;
  endfunction

  function void get_full_oxxPfBDHOMXaxQ;
    output logic  value;
    value=full_o;
  endfunction

  function void get_empty_oxxPfBDHOMXaxQ;
    output logic  value;
    value=empty_o;
  endfunction



  initial begin
    $dumpfile("SyncFIFO.fst");
    $dumpvars(0, SyncFIFO_top);
  end

  export "DPI-C" function finish_PfBDHOMXaxQ;
  function void finish_PfBDHOMXaxQ;
    $finish;
  endfunction


endmodule
