from fastapi import FastAPI
from routes import user_routes, event_routes, speaker_routes, registration_routes

app = FastAPI(
    title="Event Management System API",
    description="API for managing events, users, speakers, and registrations",
    version="1.0.0"
)

# Include routers
app.include_router(user_routes.router)
app.include_router(event_routes.router)
app.include_router(speaker_routes.router)
app.include_router(registration_routes.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Event Management System API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    } 