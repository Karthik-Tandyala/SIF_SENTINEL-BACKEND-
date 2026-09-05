ENERGY_POINTS = {

    "low": 10,

    "moderate": 30,

    "high": 60,

    "very_high": 75
}


EXPOSURE_POINTS = {

    "no_proximity": 0,

    "indirect": 10,

    "proximity_line_of_fire": 15,

    "direct_contact": 20
}


BARRIER_POINTS = {

    "functioning": 0,

    "partially_functioning": 5,

    "degraded": 10,

    "absent": 15,

    "not_applicable": 0,

    "none": 0
}


def calculate_sps(
    energy_level,
    exposure_type,
    barrier_status,
    counterfactual
):

    score = 0


    score += ENERGY_POINTS.get(
        energy_level,
        0
    )


    score += EXPOSURE_POINTS.get(
        exposure_type,
        0
    )


    score += BARRIER_POINTS.get(
        barrier_status,
        0
    )


    if counterfactual:

        score += 10


    return min(
        round(score),
        100
    )


def get_risk_level(score):

    if score >= 80:
        return "critical"

    if score >= 60:
        return "high"

    if score >= 30:
        return "medium"

    return "low"