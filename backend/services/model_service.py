from services.sps_service import (
    calculate_sps,
    get_risk_level
)

from services.evidence_service import (
    extract_evidence
)


def analyze_report(
    narrative: str,
    title: str | None = None
):

    text = (
        f"{title or ''}. {narrative}"
    ).lower()


    # ---------------------------------------------
    # TEMPORARY MODEL
    # ---------------------------------------------

    sif_detected = False

    confidence = 0.50

    energy_source = "other"

    energy_level = "low"

    exposure_type = "no_proximity"

    barrier_status = "not_applicable"

    life_saving_rule = "none"

    counterfactual = False


    # ---------------------------------------------
    # ELECTRICAL
    # ---------------------------------------------

    if (
        "electrical" in text
        or "energized" in text
        or "electric shock" in text
    ):

        sif_detected = True

        confidence = 0.94

        energy_source = "electrical"

        energy_level = "very_high"

        exposure_type = "direct_contact"


    # ---------------------------------------------
    # LOTO
    # ---------------------------------------------

    if (
        "loto" in text
        or "lockout" in text
        or "tagout" in text
    ):

        life_saving_rule = (
            "lockout_tagout"
        )


        if (
            "not applied" in text
            or "not used" in text
            or "not performed" in text
            or "no loto" in text
        ):

            barrier_status = "absent"

            counterfactual = True


    # ---------------------------------------------
    # WORKING AT HEIGHT
    # ---------------------------------------------

    if (
        "working at height" in text
        or "scaffold" in text
        or "fell" in text
        or "fall" in text
        or "height" in text
    ):

        sif_detected = True

        confidence = max(
            confidence,
            0.90
        )

        energy_source = "gravity_fall"

        energy_level = "high"

        exposure_type = (
            "proximity_line_of_fire"
        )

        life_saving_rule = (
            "working_at_height"
        )

        counterfactual = True


    # ---------------------------------------------
    # LINE OF FIRE
    # ---------------------------------------------

    if (
        "suspended load" in text
        or "line of fire" in text
        or "struck by" in text
    ):

        sif_detected = True

        confidence = max(
            confidence,
            0.91
        )

        energy_source = (
            "mechanical_lifting_operations"
        )

        energy_level = "high"

        exposure_type = (
            "proximity_line_of_fire"
        )

        life_saving_rule = (
            "line_of_fire"
        )

        counterfactual = True


    # ---------------------------------------------
    # CONFINED SPACE
    # ---------------------------------------------

    if "confined space" in text:

        sif_detected = True

        confidence = max(
            confidence,
            0.90
        )

        energy_source = "gas"

        energy_level = "high"

        exposure_type = "direct_contact"

        life_saving_rule = (
            "confined_space"
        )

        counterfactual = True


    # ---------------------------------------------
    # H2S
    # ---------------------------------------------

    if (
        "h2s" in text
        or "hydrogen sulfide" in text
    ):

        sif_detected = True

        confidence = max(
            confidence,
            0.92
        )

        energy_source = "gas"

        energy_level = "very_high"

        exposure_type = "direct_contact"

        counterfactual = True


    # ---------------------------------------------
    # EVIDENCE
    # ---------------------------------------------

    evidence = extract_evidence(text)


    # ---------------------------------------------
    # SPS
    # ---------------------------------------------

    score = calculate_sps(

        energy_level,

        exposure_type,

        barrier_status,

        counterfactual
    )


    risk_level = get_risk_level(
        score
    )


    # ---------------------------------------------
    # REASONING
    # ---------------------------------------------

    reasoning_parts = []


    if energy_source != "other":

        reasoning_parts.append(
            f"Energy source identified: "
            f"{energy_source}"
        )


    if exposure_type != "no_proximity":

        reasoning_parts.append(
            f"Human exposure identified: "
            f"{exposure_type}"
        )


    if barrier_status == "absent":

        reasoning_parts.append(
            "Critical safety barrier appears absent"
        )


    if counterfactual:

        reasoning_parts.append(
            "Potential for fatal or permanent "
            "injury identified"
        )


    reasoning = (
        ". ".join(reasoning_parts)
        if reasoning_parts
        else
        "No strong SIF precursor identified."
    )


    # ---------------------------------------------
    # RECOMMENDATIONS
    # ---------------------------------------------

    recommendations = []


    if sif_detected:

        recommendations.append(
            "Prioritize HSE review."
        )


    if barrier_status == "absent":

        recommendations.append(
            "Hold the activity until the "
            "critical barrier is restored and verified."
        )


    if life_saving_rule == (
        "lockout_tagout"
    ):

        recommendations.append(
            "Apply and verify energy isolation/LOTO."
        )


    if life_saving_rule == (
        "working_at_height"
    ):

        recommendations.append(
            "Verify fall-protection and safe-access controls."
        )


    if not recommendations:

        recommendations.append(
            "Continue normal controls and document the assessment."
        )


    # ---------------------------------------------
    # FINAL API RESPONSE
    # ---------------------------------------------

    return {

        "case_id":
            "NEW-REPORT",

        "narrative":
            narrative,

        "prediction": {

            "sif_detected":
                sif_detected,

            "confidence":
                round(
                    confidence,
                    3
                )
        },

        "hazard": {

            "energy_source":
                energy_source,

            "energy_level":
                energy_level,

            "exposure_type":
                exposure_type
        },

        "barrier": {

            "status":
                barrier_status,

            "life_saving_rule":
                life_saving_rule
        },

        "counterfactual": {

            "could_be_fatal_or_permanent":
                counterfactual,

            "reasoning":
                reasoning
        },

        "evidence":
            evidence,

        "sps": {

            "score":
                score,

            "risk_level":
                risk_level
        },

        "recommendation":
            recommendations,

        "model_source":
            "temporary prototype logic"
    }