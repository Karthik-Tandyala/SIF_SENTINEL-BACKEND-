from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="SIF-Sentinel API",
    description="AI-powered Serious Injury & Fatality precursor detection system",
    version="1.0.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "SIF-Sentinel Backend is running",
        "status": "success"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/api/v1/analyze")
def analyze_report(data: dict):
    narrative = data.get("narrative", "")
    title = data.get("title", "")

    return {
        "case_id": "TEST-001",
        "narrative": narrative,
        "title": title,
        "prediction": {
            "sif_detected": True,
            "confidence": 0.90
        },
        "hazard": {
            "energy_source": "electrical",
            "energy_level": "high",
            "exposure_type": "direct_contact"
        },
        "barrier": {
            "status": "absent",
            "life_saving_rule": "energy_isolation"
        },
        "counterfactual": {
            "could_be_fatal_or_permanent": True,
            "reasoning": "Exposure to energized equipment with failed energy isolation could result in fatal injury."
        },
        "evidence": [
            "energized equipment",
            "LOTO was not applied"
        ],
        "sps": {
            "score": 90,
            "risk_level": "critical"
        },
        "recommendation": [
            "Stop work",
            "Establish verified isolation",
            "Apply and verify LOTO"
        ]
    }