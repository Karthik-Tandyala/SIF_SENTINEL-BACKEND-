from fastapi import APIRouter

from schemas.request import FeedbackRequest


router = APIRouter()


feedback_store = []


@router.post("/feedback")
def submit_feedback(
    feedback: FeedbackRequest
):

    feedback_store.append(
        feedback.model_dump()
    )

    return {

        "status": "success",

        "message":
            "HSE feedback recorded",

        "report_id":
            feedback.report_id,

        "feedback_count":
            len(feedback_store)
    }