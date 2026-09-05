from fastapi import APIRouter


router = APIRouter()


@router.get("/dashboard")
def dashboard():

    return {

        "total_reports": 0,

        "sif_reports": 0,

        "risk_distribution": {

            "critical": 0,
            "high": 0,
            "medium": 0,
            "low": 0
        },

        "energy_sources": {},

        "life_saving_rules": {},

        "barrier_status": {}
    }