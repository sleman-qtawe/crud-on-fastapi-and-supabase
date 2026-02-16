from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.routes.appointments import router as appointment_router

app = FastAPI()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

app.include_router(
    appointment_router,
    prefix="/appointments",
    tags=["Appointments"]
)