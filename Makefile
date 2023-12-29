help:
	@echo "USAGE: make DIRNAME"

%:
	python generate.py $@
	nvim $@/*

clean:
	git clean -Xdf

.PHONY: help clean
