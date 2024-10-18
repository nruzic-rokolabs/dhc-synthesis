"""
Connector module providing cli adapter to the application

run following command from project root path:

$> PYTHONPATH=. python app/cli.py
"""

import argparse

from . import service
from .domain import Greeting

parser = argparse.ArgumentParser(description="Simple hello world command")

parser.add_argument("name", type=str, help="Name to say hello to")

args = parser.parse_args()

greeting: Greeting = service.get_greeting(args.name)
print(greeting.hello())
