from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.utils.api_response import success_response
from app.schemas.api_response import ApiResponse

from app.routers.user import router as user_router

app = FastAPI(
    title="Issue & Sprint Management System API",
    description="Backend API for Issue & Sprint Management System",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)


@app.get("/", response_model=ApiResponse)
def root():
    return success_response(
        message="Welcome to Issue & Sprint Management System API"
    )


@app.get("/health", response_model=ApiResponse)
def health_check():
    return success_response(
        message="Health check successful",
        data={
            "application": "Issue & Sprint Management System",
            "version": "1.0.0",
        }
    )