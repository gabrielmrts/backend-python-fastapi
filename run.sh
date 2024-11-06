#!/bin/bash

install_deps () {
	echo "Installing dependencies ... "
	pip install -r requirements.txt -q
	echo "Installing Dev depencies ... "
	pip install -r requirements_dev.txt -q
}

run() {
	uvicorn app.main:app --reload
}

start() {
    install_deps
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