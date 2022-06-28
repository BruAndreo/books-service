from books.config import settings
from sqlalchemy import create_engine

host = settings.db.host
port = settings.db.port
base = settings.db.base
user = settings.db.user
password = settings.db["pass"]

db_connection_str = f"postgresql://{user}:{password}@{host}:{port}/{base}"

engine = create_engine(db_connection_str, echo=True)

result = engine.execute("select now()")

print(result.fetchone())
