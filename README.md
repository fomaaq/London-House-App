# London Houses App
Backend app based on Python FastAPI Framework.

The application provides a backend for working with a dataset containing information about houses for sale in London.

## Content

- [Built with](#built-with)
- [App creation motivation](#app-creation-motivation)
- [Features](#features)
- [How to run](#how-to-run)
- [How to use](#how-to-use)
- [Tests](#tests)


## Built with

- [FastAPI](https://fastapi.tiangolo.com/) - framework for creating a web application


## App creation motivation

I created this application to:
- use FastAPI to create a backend for work with dataset
- learn how to work with database queries


## Features

In the application, responsibility is divided into modules, which are each responsible for individual functions:

1. [main](https://github.com/fomaaq/London-House-App/blob/main/main.py) - the main application module for launching

![main.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/main.png)

2. [controller](https://github.com/fomaaq/London-House-App/blob/main/controller.py) - collecting and preparing data for the response

![controller.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/controller.png)

3. [models](https://github.com/fomaaq/London-House-App/blob/main/models.py) - describing a House model based on a dataclass

![models_model.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/models_model.png)

The model also contains a static method for turning the data obtained from the database into a model

![models_method.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/models_method.png)

4. [request_parser](https://github.com/fomaaq/London-House-App/blob/main/request_parser.py) - parsing data from the user's request and returning it as a defaultdict

![request_parser.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/request_parser.png)

5. [query_builder](https://github.com/fomaaq/London-House-App/blob/main/query_builder.py) - preparing a query to the database

![query_builder.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/query_builder.png)

The module also contains private functions for generating a query to the database for each field of the model:

![query_builder_example.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/query_builder_example.png)

Also in the module there is a function for pagination:

![query_builder_pagination.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/query_builder_pagination.png)

6. [query_builder_utils](https://github.com/fomaaq/London-House-App/blob/main/query_builder_utils.py) - utilities for generating a query to the database, for example, the following method allows, if a range of values and an exact value are specified in the request at the same time, to form a query to the database only for the exact value:

![query_builder_utils_range.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/query_builder_utils_range.png)

There are also utilities for generating query strings to the database depending on the data type of the model:

![query_builder_utils_type.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/query_builder_utils_type.png)

7. [connection](https://github.com/fomaaq/London-House-App/blob/main/connection.py) - connects to the database

![connection.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/connection.png)

8. [repository](https://github.com/fomaaq/London-House-App/blob/main/repository.py) - sends a request to the database and returns data in the form of models

![repository.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/repository.png)


## How to run

You can deploy this application using docker on your local machine using the following command:
```
docker-compose up
```

## How to use

Go to the following address: http://localhost:8080/london_houses

![full_json.png](zaglushka)

Now you can try to make a query based on fields from the database, for example: http://localhost:8080/london_houses?page=7

![page_7.png](zaglushka)

You can make requests using the following fields:

- bedrooms - range or exact int type

- bathrooms - range or exact int type

- tenure - exact str type

- garden - range or exact int type

- street - similiar str type

- size_sqft - range or exact float type

- price_pounds - range or exact float type

- nearest_station_name - similiar str type

- nearest_station_miles - range or exact float type

- postcode_outer - exact str type

- pagination - exact int type

Here are example of query result:

http://localhost:8080/london_houses?max_bedrooms=2&street=street&garden=1:

![example_query.png](zaglushka)


## Tests

[Tests](https://github.com/fomaaq/London-House-App/blob/main/tests.py) have been written for the application that check the correctness of database queries

![tests.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/tests.png)

Example of a successful test:

![tests_successful.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/test_successful.png)

Example of a failed test:

![tests_failed.png](https://github.com/fomaaq/London-House-App/blob/main/imgs/test_failed.png)