"""
FastAPI application entry point.
"""

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from backend.config import AppConfig, DatabaseConfig
from backend.database.connection import DatabaseConnection
from backend.api import routes

# Create FastAPI application
app = FastAPI(
    title="Employee Management System",
    description="REST API for managing employee records",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=AppConfig.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(routes.router, prefix=AppConfig.API_PREFIX)


@app.on_event("startup")
async def startup_event():
    """Initialize database connection and create tables on startup."""
    try:
        DatabaseConnection.initialize_pool()
        DatabaseConnection.create_tables()
        print("Application started successfully")
    except Exception as e:
        print(f"Error during startup: {e}")


@app.get("/")
async def root():
    """Root endpoint."""
    return {
        "message": "Employee Management System API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    db_status = DatabaseConnection.test_connection()
    return {
        "status": "healthy" if db_status else "unhealthy",
        "database": "connected" if db_status else "disconnected"
    }


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Global exception handler for debugging."""
    if AppConfig.DEBUG:
        return JSONResponse(
            status_code=500,
            content={
                "detail": str(exc),
                "type": type(exc).__name__,
                "path": str(request.url)
            }
        )
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=AppConfig.DEBUG)
