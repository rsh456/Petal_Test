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
![](https://github.com/rsh456/Petal_Test/blob/main/images/init.jpg)
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

Create a new pokemon:

![](https://github.com/rsh456/Petal_Test/blob/main/images/add.jpg)
![](https://github.com/rsh456/Petal_Test/blob/main/images/add_file.jpg)

Read list of Pokemon
![](https://github.com/rsh456/Petal_Test/blob/main/images/read_all.jpg)

Update Pokemon
![](https://github.com/rsh456/Petal_Test/blob/main/images/update.jpg)
![](https://github.com/rsh456/Petal_Test/blob/main/images/update_file.jpg)

Delete Pokemon
![](https://github.com/rsh456/Petal_Test/blob/main/images/delete.jpg)

## Test
Test were built using pytest, they could be run with the script:
```sh
$ pytest
```
![](https://github.com/rsh456/Petal_Test/blob/main/images/test.jpg)

