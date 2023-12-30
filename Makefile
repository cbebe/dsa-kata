help:
	@echo "USAGE: make DIRNAME"

%:
	python generate.py $@
	nvim $@/*

test-%:
	@python test.py $@

clean:
	git clean -Xdf

.PHONY: help clean
