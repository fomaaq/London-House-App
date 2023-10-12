import query_builder
from collections import defaultdict


def tests_report(title, expected, actual):
    if expected == actual:
        print(f'✅ {title}')
    else:
        print(f'❌ {title} - failed:\n \033[4mExpected\033[0m: {expected} \n \033[4mActual\033[0m: {actual}')


def test_london_houses_query_builder_empty() -> bool:
    params = defaultdict(lambda: None)
    expected = 'SELECT * FROM london_prices WHERE 1=1'
    actual = query_builder.london_houses_query_builder(parameters=params)
    tests_report(
        title='Empty',
        expected=expected,
        actual=actual,
    )


def test_london_houses_query_builder_case_1() -> bool:
    params_dict = {'bedrooms': 2}
    params = defaultdict(lambda: None, params_dict)
    expected = 'SELECT * FROM london_prices WHERE 1=1 AND bedrooms = 2'
    actual = query_builder.london_houses_query_builder(parameters=params)
    tests_report(
        title='Exact numeric',
        expected=expected,
        actual=actual,
    )


def test_london_houses_query_builder_case_2() -> bool:
    params_dict = {'bedrooms': 2, 'min_bedrooms': 1, 'max_bedrooms': 3}
    params = defaultdict(lambda: None, params_dict)
    expected = 'SELECT * FROM london_prices WHERE 1=1 AND bedrooms = 2'
    actual = query_builder.london_houses_query_builder(parameters=params)
    tests_report(
        title='Exact numeric and range',
        expected=expected,
        actual=actual,
    )


def test_london_houses_query_builder_case_3() -> bool:
    params_dict = {'min_bedrooms': 1, 'max_bedrooms': 3}
    params = defaultdict(lambda: None, params_dict)
    expected = 'SELECT * FROM london_prices WHERE 1=1 AND bedrooms >= 1 AND bedrooms <= 3'
    actual = query_builder.london_houses_query_builder(parameters=params)
    tests_report(
        title='Range',
        expected=expected,
        actual=actual,
    )


def test_london_houses_query_builder_case_4() -> bool:
    params_dict = {'postcode_outer': 'SW7'}
    params = defaultdict(lambda: None, params_dict)
    expected = 'SELECT * FROM london_prices WHERE 1=1 AND postcode_outer = "SW7"'
    actual = query_builder.london_houses_query_builder(parameters=params)
    tests_report(
        title='Exact string',
        expected=expected,
        actual=actual,
    )


def test_london_houses_query_builder_case_5() -> bool:
    params_dict = {'street': 'street'}
    params = defaultdict(lambda: None, params_dict)
    expected = 'SELECT * FROM london_prices WHERE 1=1 AND street LIKE "%street%"'
    actual = query_builder.london_houses_query_builder(parameters=params)
    tests_report(
        title='Similar string',
        expected=expected,
        actual=actual,
    )


def test_pagination() -> bool:
    params_dict = {'page': 3}
    params = defaultdict(lambda: None, params_dict)
    expected = 'SELECT * FROM london_prices WHERE 1=1 LIMIT 200,100'
    actual = query_builder.london_houses_query_builder(parameters=params)
    tests_report(
        title='Pagination normal',
        expected=expected,
        actual=actual,
    )


def test_pagination_wrong() -> bool:
    params_dict = {'page': '3sds'}
    params = defaultdict(lambda: None, params_dict)
    expected = 'SELECT * FROM london_prices WHERE 1=1 LIMIT 0,100'
    actual = query_builder.london_houses_query_builder(parameters=params)
    tests_report(
        title='Pagination wrong',
        expected=expected,
        actual=actual,
    )


if __name__ == "__main__":
    test_london_houses_query_builder_empty()
    test_london_houses_query_builder_case_1()
    test_london_houses_query_builder_case_2()
    test_london_houses_query_builder_case_3()
    test_london_houses_query_builder_case_4()
    test_london_houses_query_builder_case_5()
    test_pagination()
    test_pagination_wrong()
