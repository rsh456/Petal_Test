# Petal Technical Test
Petal technical test. The challenge was developed using Flask and python.

## Instructions using Docker
Form the Dockerfile, execute:
```sh
docker build -t petal_pokemon .
```
```sh
docker run -it -p 7001:5000 petal_pokemon
```

## Instructions without Docker

First install all of the Python requirements (via pip):

```sh
$ pip install -r requirements.txt
```

For running the application, use the command below:
```sh
$ python app.py
```

## Directories

- api : Have the endpoints definition code
    The endpoint have the following structure:

| Name |  |Url |
| ------ | ---|------ |
| pokemon |Retrieves all data from the DB |[http://127.0.0.1:5000/api/pokemon] |
| pokemon |Retrieves data given the Pokemon id as parameter |[http://127.0.0.1:5000/api/pokemon?id=3] |
| pokemon_paginated | Returns all data in list gropued by page. A parameter for  |[http://127.0.0.1:5000/api/pokemon?filter=1] |


| pokemon | In addition api was built for receive the combination for sorting and filtering |[http://127.0.0.1:5000/api/pokemon?sort_ord=asc&sort_col=id&filter=1] |

It will ask for a valid authentication:
password is: superuser 
![](https://github.com/rsh456/autolab/blob/main/api_auth.jpg)

Will get all the data if no params are attached to the request
![](https://github.com/rsh456/autolab/blob/main/api_noparams.jpg)

Otherwise it will show data according to sent paramaters.
![](https://github.com/rsh456/autolab/blob/main/api_filter.jpg)


## Test
Test were built using pytest, they could be run with the script:
```sh
$ pytest
```
![](https://github.com/rsh456/autolab/blob/main/pytest.jpg)

