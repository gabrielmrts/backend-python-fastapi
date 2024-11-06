#!/bin/bash

install_dependencies () {
	echo "Installing dependencies ... "
	pip install -r requirements.txt -q
	echo "Installing Dev depencies ... "
	pip install -r requirements_dev.txt -q
}

run_docker() {
	docker compose up -d --force-recreate
}

run() {
	uvicorn app.main:app --reload
}

start() {
    install_dependencies
	run_docker
	sleep 5
    run
}

tests() {
    coverage run -m pytest
}

if [ "$1" == "start" ]; then
    start
elif [ "$1" == "env_down" ]; then
	environment_down
elif [ "$1" == "run" ]; then
	run
elif [ "$1" == "tests" ]; then
	tests
fi