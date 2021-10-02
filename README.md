# Petal Technical Test
Petal technical test. The challenge was developed using Flask and python.

## Instructions

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
| pokemon |Retrieves all data from the DB |[http://127.0.0.1:5000/api/pokemon][PlDb] |
| pokemon | Can receive parameters for retrieve data filtered by ID  |[http://127.0.0.1:5000/api/pokemon?filter=1][PlGh] |
| pokemon | Can receive parameters for get response, sorted by indicated column and  ASC (by default) or DESC criteria |[http://127.0.0esting
.1:5000/api/pokemon?sort_ord=asc&sort_col=id][PlGh] |
| pokemon | In addition api was built for receive the combination for sorting and filtering |[http://127.0.0.1:5000/api/pokemon?sort_ord=asc&sort_col=id&filter=1][PlGh] |

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

