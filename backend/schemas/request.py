from typing import Optional

from pydantic import BaseModel, Field


class AnalyzeRequest(BaseModel):

    narrative: str = Field(
        ...,
        min_length=1
    )

    title: Optional[str] = None


class FeedbackRequest(BaseModel):

    report_id: str

    human_exposure: bool

    barrier_missing: bool

    high_energy: bool

    near_miss: bool

    ai_agreement: bool

    comment: Optional[str] = None


class ChatRequest(BaseModel):

    message: str = Field(
        ...,
        min_length=1
    )

    report_id: Optional[str] = None