from fastapi import APIRouter


router = APIRouter()


@router.get("/reports")
def get_reports():

    return {
        "reports": [],
        "total": 0
    }


@router.get("/reports/{report_id}")
def get_report(report_id: str):

    return {
        "case_id": report_id,
        "message": "Report endpoint is working"
    }