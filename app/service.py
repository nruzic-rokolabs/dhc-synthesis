from .domain import Greeting


def get_greeting(name: str) -> Greeting:
    greeting = Greeting(name=name)
    return greeting
