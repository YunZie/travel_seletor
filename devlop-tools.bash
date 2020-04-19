#!/bin/bash

export DEVELOPMENT_IMAGE='python:travel-selector'

py-shell() {
  network_command=""
  if [ -n "${DOCKER_NETWORK}" ]; then
    network_command="--network"
  fi
  docker run -it --rm ${network_command} ${DOCKER_NETWORK} --name python-dev-`date "+%s"` ${@} \
    -v ${PWD}:/var/task \
    -v ${HOME}/Documents/storage:/storage \
    -v /tmp:/tmp \
    -e LOCAL_SALEOR_NETWORK=${DOCKER_NETWORK} \
    ${DEVELOPMENT_IMAGE} \
    bash
}

case $1 in
init)
    docker build -t ${DEVELOPMENT_IMAGE} . -f-<<EOF
FROM python:3.7

# Set the same WORKDIR as default image
RUN mkdir /var/task
WORKDIR /var/task

ENTRYPOINT ["./entrypoint.sh"]
CMD ["bash"]
EOF
    ;;
*)
    export local_dir=${1:-$(pwd)}
    # Do nothing, loading as build tool
    ;;
esac
