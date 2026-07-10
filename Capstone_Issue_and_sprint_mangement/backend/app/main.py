from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Issue & Sprint Management System API",
    description="Backend API for Issue & Sprint Management System",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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