help:
	@echo "USAGE: make DIRNAME"

%:
	python generate.py $@
	nvim $@/*

.PHONY: help
