from loguru import logger

import uvicorn

from app.config import settings

def main():
    logger.info("Starting in developer entrypoint.")
    uvicorn.run(
        app="wsgi:app",
        host=settings.get_host(),
        port=int(settings.get_port()),
        reload=settings.get_reload(),
        workers=int(settings.get_uvicorn_workers()),
    )
    
    
if __name__ == "__main__":
    main()
