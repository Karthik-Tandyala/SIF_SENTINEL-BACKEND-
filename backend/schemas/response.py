from typing import List

from pydantic import BaseModel


class Prediction(BaseModel):

    sif_detected: bool

    confidence: float


class Hazard(BaseModel):

    energy_source: str

    energy_level: str

    exposure_type: str


class Barrier(BaseModel):

    status: str

    life_saving_rule: str


class Counterfactual(BaseModel):

    could_be_fatal_or_permanent: bool

    reasoning: str


class SPS(BaseModel):

    score: float

    risk_level: str


class AnalyzeResponse(BaseModel):

    case_id: str

    narrative: str

    prediction: Prediction

    hazard: Hazard

    barrier: Barrier

    counterfactual: Counterfactual

    evidence: List[str]

    sps: SPS

    recommendation: List[str]

    model_source: str