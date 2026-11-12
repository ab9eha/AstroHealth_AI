def generate_recommendations(alerts):
    recommendations = []

    for alert in alerts:
        indicator = alert["indicator"]

        if indicator == "Heart rate":
            recommendations.append(
                "Review the heart-rate trend and verify the sensor measurement."
            )

        elif indicator == "Blood oxygen":
            recommendations.append(
                "Verify sensor placement and repeat the oxygen measurement."
            )

        elif indicator == "Body temperature":
            recommendations.append(
                "Verify the temperature sensor and review the measurement trend."
            )

        elif indicator == "Respiration rate":
            recommendations.append(
                "Review the respiration trend and check sensor signal quality."
            )

        elif indicator in [
            "Systolic pressure",
            "Diastolic pressure"
        ]:
            recommendations.append(
                "Repeat the blood-pressure measurement using a validated device."
            )

        else:
            recommendations.append(
                "Review the unusual pattern and consult the mission medical officer."
            )

    if not recommendations:
        recommendations.append(
            "No configured reference-range deviations detected. Continue routine monitoring."
        )

    return list(dict.fromkeys(recommendations))