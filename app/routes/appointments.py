from fastapi import APIRouter
from app.models import Appointment
from app.database import supabase
from fastapi import HTTPException


router = APIRouter()

@router.post("/")
async def create_appointment(data: Appointment):
    print("Received data:", data)
    response = supabase.table("appointments").insert({
        "name": data.name,
        "id_number": data.id_number,
        "specialization": data.specialization,
        "appointment_time": data.datetime.isoformat()
    }).execute()
    return {
        "message": "Appointment saved successfully",
        "data": response.data
    }

@router.get("/")
async def get_appointments():
    response = supabase.table("appointments").select("*").execute()
    return {
        "message": "Appointments fetched successfully",
        "data": response.data
    }

@router.put("/{appointment_id}")
async def update_appointment(appointment_id: str, data: Appointment):
    check = supabase.table("appointments").select("*").eq("id", appointment_id).execute()
    if not check.data:
        raise HTTPException(status_code=404, detail="Appointment not found")

    response = supabase.table("appointments").update({
        "name": data.name,
        "id_number": data.id_number,
        "specialization": data.specialization,
        "appointment_time": data.datetime.isoformat()
    }).eq("id", appointment_id).execute()

    return {"message": "Appointment updated successfully", "data": response.data}

@router.delete("/{appointment_id}")
async def delete_appointment(appointment_id: str):
    check = supabase.table("appointments").select("*").eq("id", appointment_id).execute()
    if not check.data:
        raise HTTPException(status_code=404, detail="Appointment not found")

    supabase.table("appointments").delete().eq("id", appointment_id).execute()
    return {"message": f"Appointment with id {appointment_id} deleted successfully"}