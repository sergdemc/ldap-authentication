# Flask LDAP auth demo

---

## Installation

### Prerequisites

#### Python

Before installing the package make sure you have Python version 3.8 or higher installed:

```bash
>> python --version
Python 3.10+
```

#### Poetry

The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installation).


#### Docker

The project uses Docker to run the LDAP server. To install Docker use its [official instruction](https://docs.docker.com/get-docker/).

### Application

To use the application, you need to clone the repository to your computer. This is done using the `git clone` command. Clone the project:

```bash
>> git clone https://github.com/sergdemc/python-project-52.git && cd python-project-52
```

Then you have to install all necessary dependencies:

```bash
>> make install
```

---

## Usage

Start the LDAP server in the Docker container by running: 
```bash
make ldap-start
```

Start the application by running:
```bash
make start
```
_By default, the server will be available at http://127.0.0.1:5000._

To add a new user to LDAP server use new_user.ldif file and the run command:
```bash
make add-user
```

___