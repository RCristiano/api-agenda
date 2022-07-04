SHELL:=/usr/bin/env bash

.PHONY: clean run

clean:
	@echo "Removing cache"
	@find ./ -name '__pycache__' | xargs rm -rf;

run:
	poetry run uvicorn app.main:app --reload