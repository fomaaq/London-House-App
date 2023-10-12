from fastapi import Request
import request_parser
import query_builder
import models
import repository


def get_london_houses(request: Request) -> [models.House]:
    parameters = request_parser.get_parameters(request=request)
    sql_query = query_builder.london_houses_query_builder(parameters=parameters)
    return repository.get_london_houses(query=sql_query)
