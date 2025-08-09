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


  export "DPI-C" function get_clkxxPfBDHPcCNRi;
  export "DPI-C" function set_clkxxPfBDHPcCNRi;
  export "DPI-C" function get_rst_nxxPfBDHPcCNRi;
  export "DPI-C" function set_rst_nxxPfBDHPcCNRi;
  export "DPI-C" function get_we_ixxPfBDHPcCNRi;
  export "DPI-C" function set_we_ixxPfBDHPcCNRi;
  export "DPI-C" function get_re_ixxPfBDHPcCNRi;
  export "DPI-C" function set_re_ixxPfBDHPcCNRi;
  export "DPI-C" function get_data_ixxPfBDHPcCNRi;
  export "DPI-C" function set_data_ixxPfBDHPcCNRi;
  export "DPI-C" function get_data_oxxPfBDHPcCNRi;
  export "DPI-C" function get_full_oxxPfBDHPcCNRi;
  export "DPI-C" function get_empty_oxxPfBDHPcCNRi;


  function void get_clkxxPfBDHPcCNRi;
    output logic  value;
    value=clk;
  endfunction

  function void set_clkxxPfBDHPcCNRi;
    input logic  value;
    clk=value;
  endfunction

  function void get_rst_nxxPfBDHPcCNRi;
    output logic  value;
    value=rst_n;
  endfunction

  function void set_rst_nxxPfBDHPcCNRi;
    input logic  value;
    rst_n=value;
  endfunction

  function void get_we_ixxPfBDHPcCNRi;
    output logic  value;
    value=we_i;
  endfunction

  function void set_we_ixxPfBDHPcCNRi;
    input logic  value;
    we_i=value;
  endfunction

  function void get_re_ixxPfBDHPcCNRi;
    output logic  value;
    value=re_i;
  endfunction

  function void set_re_ixxPfBDHPcCNRi;
    input logic  value;
    re_i=value;
  endfunction

  function void get_data_ixxPfBDHPcCNRi;
    output logic [31:0] value;
    value=data_i;
  endfunction

  function void set_data_ixxPfBDHPcCNRi;
    input logic [31:0] value;
    data_i=value;
  endfunction

  function void get_data_oxxPfBDHPcCNRi;
    output logic [31:0] value;
    value=data_o;
  endfunction

  function void get_full_oxxPfBDHPcCNRi;
    output logic  value;
    value=full_o;
  endfunction

  function void get_empty_oxxPfBDHPcCNRi;
    output logic  value;
    value=empty_o;
  endfunction



  initial begin
    $dumpfile("SyncFIFO.fst");
    $dumpvars(0, SyncFIFO_top);
  end

  export "DPI-C" function finish_PfBDHPcCNRi;
  function void finish_PfBDHPcCNRi;
    $finish;
  endfunction


endmodule
