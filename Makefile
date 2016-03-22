.PHONY: test

help:
	@echo 'Makefile for uatu project                      '
	@echo '                                               '
	@echo 'Usage:                                         '
	@echo '   run                            Run project  '
	@echo '   test                           Run all tests'

run:
	python -m uatu.http_server

test:
	python -m unittest discover
