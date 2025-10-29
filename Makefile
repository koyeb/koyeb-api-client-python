KOYEB_API ?= $(shell echo $${KOYEB_API:-https://developer.koyeb.com})
TEST_OPTS=-v -test.timeout 300s
GIT_USER_ID?=koyeb
GIT_REPO_ID?=koyeb-api-client-python
OPENAPI_GENERATOR_VERSION?=latest
PACKAGE_VERSION?=1.0.0


.PHONY: gen
gen: clean spec/openapi.json
	docker run --rm -v `pwd`:/builder openapitools/openapi-generator-cli:${OPENAPI_GENERATOR_VERSION} generate --git-user-id ${GIT_USER_ID} --git-repo-id ${GIT_REPO_ID} -i /builder/spec/openapi.json -g python -o /builder --package-name koyeb --additional-properties packageVersion=${PACKAGE_VERSION} --additional-properties licenseInfo="Apache-2.0" --additional-properties generateSourceCodeOnly=true

.PHONY: clean
clean:
	rm -rf koyeb

.PHONY: format
format:
	black koyeb test

.PHONY: spec/openapi.json
spec/openapi.json:
	mkdir -p api/v1/koyeb
	#curl -s $(KOYEB_API)/public.swagger.json > spec/openapi.json

test:
	python -m unitest
