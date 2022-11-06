# Container's default name
NAME=restapi_testing_fwm

# Docker image default name
IMAGE=test/$(NAME)

# Mount localfile system for local development
LOCAL_OPTS=-v $(shell pwd):/PycharmProjects/restapi_testing_fwm -e PYTHONPATH="/PycharmProjects/restapi_testing_fwm"

# Build image
.PHONY: build
build:
	@echo "--> Building $(NAME)"
	docker build -t $(IMAGE) .

# Stop container
.PHONY: stop
stop:
	@echo "--> Stopping $(NAME)"
	docker kill $(NAME) || true

# Start container
.PHONY: start
start:
	@echo "--> Starting $(NAME)"
	docker start $(NAME)

# Remove container
.PHONY: rm
rm:
	@echo "--> Removing container $(NAME)"
	docker rm -f $(NAME) || true

# Tail container logs
.PHONY: logs
logs:
	docker logs -f $(NAME)

# Run container and provide a Shell terminal
.PHONY: local
local:
	@echo "--> Starting $(NAME)"
	winpty docker run $(LOCAL_OPTS) --name $(NAME) --env-file secrets.ini -ti $(IMAGE) bash


# Run the application
.PHONY: run
run: stop rm build local
