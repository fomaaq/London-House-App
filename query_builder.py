from collections import defaultdict
import query_builder_utils


def london_houses_query_builder(parameters: defaultdict) -> str:
    return 'SELECT * FROM london_prices WHERE 1=1' + \
        _make_bedrooms_query(parameters=parameters) + \
        _make_bathrooms_query(parameters=parameters) + \
        _make_tenure_query(parameters=parameters) + \
        _make_garden_query(parameters=parameters) + \
        _make_street_query(parameters=parameters) + \
        _make_size_sqft_query(parameters=parameters) + \
        _make_price_pounds(parameters=parameters) + \
        _make_nearest_station_name_query(parameters=parameters) + \
        _make_nearest_station_miles_query(parameters=parameters) + \
        _make_postcode_outer_query(parameters=parameters) + \
        _make_pagination(parameters=parameters)


def _make_bedrooms_query(parameters: dict) -> str:
    return query_builder_utils._make_range_query(
        request_name='bedrooms',
        column_name='bedrooms',
        min_name='min_bedrooms',
        max_name='max_bedrooms',
        parameters=parameters,
    )


def _make_bathrooms_query(parameters: dict) -> str:
    return query_builder_utils._make_range_query(
        request_name='bathrooms',
        column_name='bathrooms',
        min_name='min_bathrooms',
        max_name='max_bathrooms',
        parameters=parameters,
    )


def _make_tenure_query(parameters: dict) -> str:
    return query_builder_utils._make_exact_query(
        request_name='tenure',
        column_name='tenure',
        parameters=parameters,
    )


def _make_garden_query(parameters: dict) -> str:
    return query_builder_utils._make_range_query(
        request_name='garden',
        column_name='garden',
        min_name='min_garden',
        max_name='max_garden',
        parameters=parameters,
    )


def _make_street_query(parameters: dict) -> str:
    return query_builder_utils._make_similar_query(
        request_name='street',
        column_name='street',
        parameters=parameters,
    )


def _make_size_sqft_query(parameters: dict) -> str:
    return query_builder_utils._make_range_query(
        request_name='size_sqft',
        column_name='size_sqft',
        min_name='min_size_sqft',
        max_name='max_size_sqft',
        parameters=parameters,
    )


def _make_price_pounds(parameters: dict) -> str:
    return query_builder_utils._make_range_query(
        request_name='price_pounds',
        column_name='price_pounds',
        min_name='min_price_pounds',
        max_name='max_price_pounds',
        parameters=parameters,
    )


def _make_nearest_station_name_query(parameters: dict) -> str:
    return query_builder_utils._make_similar_query(
        request_name='nearest_station_name',
        column_name='nearest_station_name',
        parameters=parameters,
    )


def _make_nearest_station_miles_query(parameters: dict) -> str:
    return query_builder_utils._make_range_query(
        request_name='nearest_station_miles',
        column_name='nearest_station_miles',
        min_name='min_nearest_station_miles',
        max_name='max_nearest_station_miles',
        parameters=parameters,
    )


def _make_postcode_outer_query(parameters: dict) -> str:
    return query_builder_utils._make_exact_query(
        request_name='postcode_outer',
        column_name='postcode_outer',
        parameters=parameters,
    )


def _make_pagination(parameters: dict) -> str:
    if parameters['page']:
        page = query_builder_utils._make_page_number(parameters=parameters)
        result_quantity = 100
        return f' LIMIT {(page-1)*result_quantity},{result_quantity}'
    else:
        return ''
