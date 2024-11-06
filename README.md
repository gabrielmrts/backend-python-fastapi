## REST API with FastAPI

### Requirements
```
Python >= 3.13
Docker >= 27.1.1
```

### How to run on UNIX
```
Give ./run.sh execution permission (chmod +x run.sh)
Run ./run.sh start

Docs will be available at: http://127.0.0.1:8000/docs
Redoc will be available at: http://127.0.0.1:8000/redoc 
```

### Testing
```
To run automated tests: ./run.sh tests

Test User:
CPF: 26323445220
Password: testpassword123
```

### Deploying
```
1 - Create a pipeline that:
    - Build the Dockerfile
    - Do a push on some image registry
    - Connect on the server
    - Do a pull to get the latest container image
    - Put to run
```

### Contributing
```
Before contributing to this project, check the [CONTRIBUTING.md](CONTRIBUTING.md) file for the patterns and code style used in this project.
```