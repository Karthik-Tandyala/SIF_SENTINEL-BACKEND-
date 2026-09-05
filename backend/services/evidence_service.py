def extract_evidence(text):

    evidence = []


    phrases = [

        (
            "energized electrical",
            "energized electrical"
        ),

        (
            "electrical panel",
            "electrical panel"
        ),

        (
            "loto was not applied",
            "LOTO was not applied"
        ),

        (
            "lockout was not applied",
            "Lockout was not applied"
        ),

        (
            "without safety harness",
            "without safety harness"
        ),

        (
            "suspended load",
            "suspended load"
        ),

        (
            "line of fire",
            "line of fire"
        ),

        (
            "h2s",
            "H2S"
        ),

        (
            "hydrogen sulfide",
            "hydrogen sulfide"
        ),

        (
            "pressurized",
            "pressurized"
        ),

        (
            "confined space",
            "confined space"
        ),

        (
            "near miss",
            "near miss"
        )
    ]


    for keyword, display in phrases:

        if keyword in text:

            if display not in evidence:

                evidence.append(display)


    return evidence