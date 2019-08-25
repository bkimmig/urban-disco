# ensure the targets are always run. Needed to prevent side effects when running with
# "-q"
.PHONY: build docker test

# Default action and options for run
# By default will run an interactive bash prompt
RUN_PARAMS ?= bash

# Bring down any dependencies and build the images
build: docker

# Rebuild all local Docker images
docker:
	docker build -t vacasa/urban-disco:latest .

