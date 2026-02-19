REDOCROOT=$(shell pwd)

DEFINITION_FILE='openapi/openapi.yaml'

PREVIEW_HTML='preview/index.html'
PREVIEW_URL='file://'$(abspath ${PREVIEW_HTML})

BUNDLE_YAML='preview/dist.yaml'

ASSETS_DIR=$(shell dirname ${REDOCROOT})'/echeapi/interface/static/redoc'
ASSETS_YAML=${ASSETS_DIR}'/dist.yaml'

build-docs:
		@docker run --rm \
				-v ${REDOCROOT}:/spec \
				redocly/cli build-docs ${DEFINITION} \
				--output=${PREVIEW_HTML} && \
				echo ${PREVIEW_URL}

bundle:
		@docker run --rm \
				--user $(shell id -u):$(shell id -g) \
				-v ${REDOCROOT}:/spec \
				redocly/cli bundle --dereferenced ${DEFINITION} && \
				cp $(abspath ${BUNDLE_YAML}) ${ASSETS_YAML} && \
				echo 'Copied to '${ASSETS_YAML}

lint:
		@docker run --rm \
				-v $(shell pwd):/spec \
				redocly/cli lint ${DEFINITION}
