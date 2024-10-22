############################################################################
# Makefile to build and deploy the Free&Fair NLP Docker image, © Free&Fair #
# Daniel M. Zimmerman, October 2024                                        #
############################################################################
# Possible commands are: make [all|image|save|remove]

# URL for the docker repository to push the image to.
DOCKER_REPOSITORY := registry-1.docker.io

# Organization within the docker repository to push to.
DOCKER_ORGANIZATON := freeandfair

# Name of the docker image to be created.
IMAGE=nlp

# Build image for linux/amd64 and linux/arm64 platforms by default.
DOCKER_DEFAULT_PLATFORM=linux/amd64,linux/arm64

# Default target: clone and rebuild lando, and create docker image.
all: image save

# Display a brief help page listing possible commands/targets.
help:
	@echo "Possible commands/targets are:"
	@echo "make [all]  - clone and rebuild lando and create $(IMAGE) image"
	@echo "make login  - log user into dockehub repository"
	@echo "make logout - log user out of dockerhub repository"
	@echo "make image  - create $(IMAGE) image (in local store)"
	@echo "make save   - save $(IMAGE) image to a tar file"
	@echo "make pull   - pull nlp image from dockerhub repository"
	@echo "make push   - push nlp image to dockerhub repository"
	@echo "make remove - remove $(IMAGE) image from local store"
	@echo "make clean  - remove all dynamically created files"
	@echo "make help   - display this help page"

# Log into dockerhub docker repository.
login:
	$(info [info] logging into dockerhub repository)
	docker login $(DOCKER_REPOSITORY)

# Log out of dockerhub docker repository.
logout:
	$(info [info] Logging out of dockerhub repository)
	docker logout $(DOCKER_REPOSITORY)

# Create docker image.
image:
	$(info [info] rebuilding $(IMAGE) docker image ...)
	docker build -t $(IMAGE) .  --platform="$(DOCKER_DEFAULT_PLATFORM)"

# Save docker image locally to a .tar file.
save:
	$(info [info] saving docker image to $(IMAGE).tar ...)
	docker save -o $(IMAGE).tar $(IMAGE)

# Pull docker image from dockerhub private repository.
pull: login
	docker pull $(DOCKER_ORGANIZATON)/$(IMAGE):latest

# Push docker image to dockerhub private repository.
push: login
	docker image tag $(IMAGE) $(DOCKER_ORGANIZATON)/$(IMAGE):latest
	docker push $(DOCKER_ORGANIZATON)/$(IMAGE):latest

# Push docker image from local image cache / store.
remove:
	$(info [info] removing $(IMAGE) image locally ...)
	docker rmi $(IMAGE)

# Clean up all dynamically generated files, including lando clone.
clean:
	$(info [info] cleaning up all dynamically generated files ...)
	rm -f $(IMAGE).tar

PHONY: all help login logout image save pull push remove clean
