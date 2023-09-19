from flask_restx import Api
from routing.api_routes import api_routes


class RouteHandler:
    def __init__(self, controller):
        self.controller = controller


def add_routes(api: Api) -> Api:
    routes_dictionary = {route: RouteHandler(controller=handler) for route, handler in api_routes.items()}

    for url, route_handler in routes_dictionary.items():
        api.add_resource(route_handler.controller, url)

    return api
