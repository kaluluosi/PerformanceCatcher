from typing import Callable
from nicegui import Client,ui

def resolve(page:Callable):
    """
    Resolve a path to a file, expanding any environment variables and
    relative paths.
    """
    return Client.page_routes.get(page,None)


def is_active_page(path:str):
    """
    Check if current page is the same as the given path
    """
    return ui.context.client.page.path == path