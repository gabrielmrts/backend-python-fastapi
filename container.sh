#! /bin/bash

cd /var/www/app

start() {
    uvicorn app.main:app --host 0.0.0.0 --port 80 --limit-concurrency 1000 --timeout-keep-alive 300 --workers 3
}

start