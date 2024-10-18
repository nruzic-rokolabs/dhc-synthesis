# DHC Synthesis SOW

## Usage guide

### Run infrastructure
```shell
docker compose up -d
```

### Setup virtual environment
You need to have python 3.11[.7] installed on your environment.
```shell
pip install pipenv
pipenv install --dev
pipenv shell
```

### Start application from virtual environment
Uvicorn process working dir should be project root dir to allow pydantic to pick up application settings from settings.yml file:
```bash
fastapi run
```

### Start application in dev mode from virtual environment
To watch and auto reload changes run following command:
```bash
fastapi dev
```

### Start application using docker
Build docker image if not already built and run it using following command.\
Note that you should have valid .env file in your project root folder. Consult [example.env](example.env) to see what information is needed in the environment.
```shell
docker run --rm -d -P --name dhc-synthesis-api --network dhc-synthesis-api-network-1 --env-file .env dhc-synthesis-api
```

## Developer Guide
Build docker image using following command from project root folder.
### Build
```shell
docker build -t dhc-synthesis-api .
```

### Tag
```shell
docker tag dhc-synthesis-api 891377205247.dkr.ecr.us-east-1.amazonaws.com/dhc-synthesis-api
```

### Push
```shell
docker push 891377205247.dkr.ecr.us-east-1.amazonaws.com/dhc-synthesis-api
```

If you need to login to docker repo run following commands
```shell
aws sso login --profile rokolabs

aws ecr get-login-password --profile rokolabs --no-cli-auto-prompt | docker login -u AWS --password-stdin 891377205247.dkr.ecr.us-east-1.amazonaws.com/dhc-synthesis-api
```

### Architecture

#### Static organization
This part shows the project source code organization.

The root of the project organized in source code, test, documentation folders.
The root folder can contain other supporting files, like the ones for development or production environment setup.
```shell
dhc-synthesis-api/
├── alembic/                # Folder containing database migration files
├── app/                    # Folder containing application source code
├── doc/                    # Folder containing project documentation
├── docker-compose.yml
├── Dockerfile
├── notebooks/              # Folder containing useful and sharable jupyter notebook files
├── Pipfile                 # Project dependencies definition for pipenv tool
├── Pipfile.lock            # Project dependencies definition for pipenv tool
├── README.md
├── requirements.txt        # Project dependencies for pip tool
└── tests                   # Folder containing tests source code
```

The project source code is organized into top level packages that are split by functionality.
For general guide on Fastapi application source code organization see following [article](https://medium.com/@amirm.lavasani/how-to-structure-your-fastapi-projects-0219a6600a8f).
```shell
dhc-synthesis-api/app/
├── ...                     # root package containing main application files
├── ind/                    # ind package IND feature related application files
└── sow/                    # sow package SOW feature related application files
```
As a rule of thumb, code in any package can use code from packages on same level or higher packages.
For example, code in ind package can use code from sow or root packages, but root package code should not use code from idn or sow packages.

Static organization of source code in packages follows Domain Driven Design onion architecture.
For general guide on onion architecture and responsibilities of each onion layer see following [article](https://blog.itsjavi.com/target-software-architectures-the-onion-architecture).
```shell
dhc-synthesis-api/app/
├── cli.py                  # connector module containing cli adapter to the application
├── controller.py           # connector module containing HTTP REST adapter to the application
├── domain.py               # domain module containing core business domain classes and api
├── main.py                 # application module containing fastapi http server setup
├── rdbs.py                 # connector module containing relational database adapter for the application
├── service.py              # application module containing application level services adding extra logic or conditions specific to the use case.
├── settings.py             # application module providing configuration functionality
```

Diagram below depicts 3 key source code layers:
1. Domain
2. Application
3. Connectors

![alt text](doc/diag-plantuml-md5-45e11336f4bef9755c450de6a964edff.png)
