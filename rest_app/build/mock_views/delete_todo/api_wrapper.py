from dsu.dsu_gen.openapi.decorator.interface_decorator import \
    validate_decorator
from .validator_class import ValidatorClass


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    try:
        from rest_app.views.delete_todo.request_response_mocks \
            import REQUEST_BODY_JSON
        body = REQUEST_BODY_JSON
    except ImportError:
        body = {}

    test_case = {
        "path_params": {'id': 934},
        "query_params": {},
        "header_params": {},
        "body": body,
        "securities": [{'oauth': ['delete']}]
    }

    from dsu.dsu_gen.openapi.utils.mock_response import mock_response

    try:
        response = ''
        status_code = 200
        if '200' in ['200', '401', '403', '404']:
            from rest_app.views.delete_todo.request_response_mocks \
                import RESPONSE_200_JSON
            response = RESPONSE_200_JSON
            status_code = 200
        elif '201' in ['200', '401', '403', '404']:
            from rest_app.views.delete_todo.request_response_mocks \
                import RESPONSE_201_JSON
            response = RESPONSE_201_JSON
            status_code = 201
    except ImportError:
        response = ''
        status_code = 200
    response_tuple = mock_response(
        app_name="rest_app", test_case=test_case,
        operation_name="delete_todo",
        kwargs=kwargs, default_response_body=response,
        group_name="", status_code=status_code)
    return response_tuple