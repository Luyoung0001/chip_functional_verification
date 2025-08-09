PICKER 	= picker
NAME	= SyncFIFO
run:
	pytest --toffee-report -sv .
dut:
	$(PICKER) export --autobuild=true $(NAME).v -w $(NAME).fst --sname $(NAME) --tdir picker_out_$(NAME) --lang python -e -c --sim verilator

clean:
	rm -rf $(NAME) picker_out_$(NAME) reports