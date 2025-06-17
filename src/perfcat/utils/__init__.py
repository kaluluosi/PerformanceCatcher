from typing import Callable
from nicegui import Client

def resolve(page:Callable):
    """
    Resolve a path to a file, expanding any environment variables and
    relative paths.
    """
    return Client.page_routes.get(page,None)