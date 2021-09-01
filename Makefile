# Makefile for MCDR pack plugin

MODULE = mcdreforged
OUTDIR = out

ifdef SystemRoot
	PYTHON = python
else
	PYTHON = python3
endif

.PHONY: pack

pack:
	$(PYTHON) -m $(MODULE) pack -o $(OUTDIR)
