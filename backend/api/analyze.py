from fastapi import APIRouter

from schemas.request import AnalyzeRequest
from schemas.response import AnalyzeResponse

from services.model_service import analyze_report


router = APIRouter()


@router.post(
    "/analyze",
    response_model=AnalyzeResponse
)
def analyze_report_endpoint(
    request: AnalyzeRequest
):

    result = analyze_report(
        narrative=request.narrative,
        title=request.title
    )

    return result