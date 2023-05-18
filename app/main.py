import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.endpoints import student_route


def create_app() -> FastAPI():
    app = FastAPI()

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=["*"],
        allow_methods=["*"],
        allow_headers=["*"]
    )
    app.include_router(student_route)
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, port=8080)
