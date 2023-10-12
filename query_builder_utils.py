def _make_range_query(
        request_name: str,
        column_name: str,
        min_name: str,
        max_name: str,
        parameters: dict,
) -> str:
    if parameters[request_name]:
        return _make_numeric_query(
            name=column_name,
            param=parameters[request_name],
        )

    elif parameters[min_name] or parameters[max_name]:
        query = ''
        if parameters[min_name]:
            query += _make_numeric_min_query(
                name=column_name,
                param=parameters[min_name],
            )

        if parameters[max_name]:
            query += _make_numeric_max_query(
                name=column_name,
                param=parameters[max_name],
            )

        return query

    else:
        return ''


def _make_exact_query(
        request_name: str,
        column_name: str,
        parameters: dict,
) -> str:
    if parameters[request_name]:
        return _make_string_query(
            name=column_name,
            param=parameters[request_name],
        )

    else:
        return ''


def _make_similar_query(
        request_name: str,
        column_name: str,
        parameters: dict,
) -> str:
    if parameters[request_name]:
        return _make_string_like_query(
            name=column_name,
            param=parameters[request_name]
        )

    else:
        return ''


def _make_string_like_query(name: str, param: str) -> str:
    return f' AND {name} LIKE "%{param}%"'


def _make_string_query(name: str, param: str) -> str:
    return f' AND {name} = "{param}"'


def _make_numeric_query(name: str, param: int) -> str:
    return f' AND {name} = {param}'


def _make_numeric_min_query(name: str, param: int) -> str:
    return f' AND {name} >= {param}'


def _make_numeric_max_query(name: str, param: int) -> str:
    return f' AND {name} <= {param}'


def _make_page_number(parameters: dict) -> int:
    if parameters['page']:
        try:
            return int(parameters['page'])
        except ValueError:
            return 1
