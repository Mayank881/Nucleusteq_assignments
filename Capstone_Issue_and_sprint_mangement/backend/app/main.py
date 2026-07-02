from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.user import router as user_router
from app.routers.admin import router as admin_router

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
app.include_router(admin_router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Issue & Sprint Management System API"
    }


@app.get("/health")
def health_check():
    return {
        "status": "success",
        "application": "Issue & Sprint Management System",
        "version": "1.0.0"
    }