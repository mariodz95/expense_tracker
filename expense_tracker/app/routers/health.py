from fastapi import APIRouter

router = APIRouter()


@router.get("/", response_model=dict)
async def service_health_status():

    return {}
