# London Houses App
Backend app based on Python FastAPI Framework.

The application provides a backend for working with a dataset containing information about houses for sale in London.

## Content

- [Built with](#built-with)
- [App creation motivation](#app-creation-motivation)
- [Features](#features)
- [Tests](#tests)
- [How to use](#how-to-use)
- [How to run](#how-to-run)


## Built with

- [FastAPI](https://fastapi.tiangolo.com/) - framework for creating a web application


## App creation motivation

I created this application to:
- use FastAPI to create a backend for work with dataset
- learn how to work with database queries


## Features

In the application, responsibility is divided into modules, which are each responsible for individual functions:

1. main - the main application module for launching
![main.png](zaglushka)

2. controller - collecting and preparing data for the response
![controller.png](zaglushka)

3. models - describing a House model based on a dataclass
![models_model.png](zaglushka)

The model also contains a static method for turning the data obtained from the database into a model
![models_method.png](zaglushka)

4. request_parser - parsing data from the user's request and returning it as a defaultdict
![request_parser.png](zaglushka)

5. query_builder - preparing a query to the database
![query_builder.png](zaglushka)

The module also contains private functions for generating a query to the database for each field of the model:
![query_builder_example.png](zaglushka)

Also in the module there is a function for pagination:
![query_builder_pagination.png](zaglushka)

6. query_builder_utils - utilities for generating a query to the database, for example, the following method allows, if a range of values and an exact value are specified in the request at the same time, to form a query to the database only for the exact value:
![query_builder_utils_range.png](zaglushka)

There are also utilities for generating query strings to the database depending on the data type of the model:
![query_builder_utils_type.png](zaglushka)

7. connection - connects to the database
![connection.png](zaglushka)

8. repository - sends a request to the database and returns data in the form of models
![repository.png](zaglushka)


## Tests

Tests have been written for the application that check the correctness of database queries
![tests.png](zaglushka)

Example of a successful test:
![tests_successful.png](zaglushka)

Example of a failed test:
![tests_failed.png](zaglushka)

## How to run

You can deploy this application using docker on your local machine using the following command:
```
docker-compose up
```