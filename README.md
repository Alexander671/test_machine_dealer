
# TEST_DEALER_MACHINE

A simple REST API python test backend service "dealer_machine".

Tested on Ubuntu 20.04 and
```Python==3.8.10       
asgiref==3.5.0          
Django==4.0.4
django-environ==0.8.1
djangorestframework==3.13.1
environ==1.0
pytz==2022.1
sqlparse==0.4.2
pip==22.0.4
```
# CONTENTS:
[Description](#description) </br>
[Deploy](#deploy)           </br>
[Test](#test)               </br>

## Description <a name="description"></a>
**The system has API methods that provide:**
- ✓ GET
- ✓ POST
- ✓ DELETE
- ✓ PUT

**The system has 2 main path:**
- ✓ api/machine
- ✓ api/dealer

**Endpoints example:**

*Request:* 
```
GET http://127.0.0.1:8000/api/machine
```
*Response:* 
```
[{
        "id": 1, 
        "machine_model": "Machine 1",
        "date_of_create": "2001-04-23",
        "price": 50000,
        "dealer": 1
}]
```

*Request:*
```
PUT http://127.0.0.1:8000/api/dealer2/

Content type: application/json
{
       "address": "Lenina 5"
}
```
*Response:*
```
{
    "id": 2,
    "name": "Dealer 2",
    "official": true,
    "address": "Lenina 5"
}
```
for more info look [Test](#test)               </br>

## Getting Started <a name="deploy"></a>
These instructions will get you a copy of the project up and running on your local machine. There are **two** ways to run a project.

1. run without Docker
2. run with Docker 

### Build Without Docker

#### Git

Clone the repository
```
git clone https:https://github.com/Alexander671/test_machine_dealer/
```

Navigate into the `test_news` directory
```
cd test_machine_dealer/test_machine_dealer
```

#### .env file

For correct work you need to create .env file in ~/PROJECT_DIR/test_news/test_news/.env
with the following content:

```
nano .env 
```

```
SECRET_KEY = <your_secret_key>
DEBUG = <True/False>
ALLOWED_HOSTS = <list_hosts>

```

#### Dependencies

Install, using `pip`:

```
pip install -r requirements.txt
```


#### Usage
```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

### Build Using Docker

#### Git

Clone the repository
```
git clone https://github.com/Alexander671/test_machine_dealer/
```

Navigate into the `test_news` directory
```
cd test_machine_dealer/test_machine_dealer
```

#### .env file

For correct work you need to create .env file in ~/PROJECT_DIR/test_machine_dealer/test_machine_dealer/.env
with the following content:

```
nano .env 
```

```
SECRET_KEY = <your_secret_key>
DEBUG = <True/False>
ALLOWED_HOSTS = <list_hosts>

```

#### Usage

1. Build the image

`docker build .`

2. Сompiling the image with the team

`docker-compose build`

3. Run container:

`docker-compose up -d`

## Some examples and test <a name="test"></a>

Some edge-cases examples are available on the [test_postman](https://github.com/Alexander671/test_machine_dealer/tree/main/test_postman)

## Authors

* **Alexander Matveev** - *Initial work* - [Alexander671](https://github.com/Alexander671)

