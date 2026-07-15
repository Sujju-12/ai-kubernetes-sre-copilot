def classify_incident(snapshot):
    """
    Determine what kind of Kubernetes incident
    is occurring based on cluster state.
    """

    for pod in snapshot["pods"]:

        status = pod["status"]

        if status == "ImagePullBackOff":
            return "IMAGE_PULL"

        if status == "CrashLoopBackOff":
            return "CRASH_LOOP"

        if status == "Pending":
            return "PENDING"

    return "HEALTHY"
