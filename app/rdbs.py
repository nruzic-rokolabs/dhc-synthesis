"""
Connector module providing to application a relational database adapter
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.domain import Greeting
from settings import settings

# an Engine, which the Session will use for connection
# resources, typically in module scope
engine = create_engine(settings.database_settings.url())
# a sessionmaker(), also in the same scope as the engine
Session = sessionmaker(engine)


class AppRepository:

    def fetch_greeting(self, greeting_id: int) -> Greeting:
        return Greeting(name="Stranger")
