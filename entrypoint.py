import uvicorn


from books.app import app
from books.config import settings
from books.data import db


if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app",
        port=settings.app.port,
        log_level=settings.app.log_level,
        reload=settings.app.reload
    )
