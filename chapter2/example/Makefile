example:
	picker export RandomGenerator.v --sname RandomGenerator -w RandomGenerator.fst --lang python --sim verilator --internal ./internal.yaml -c
clean:
	rm -rf ./RandomGenerator RandomGenerator.fst
toffee:
	pytest . -sv --toffee-report

.PHONY: example rm
