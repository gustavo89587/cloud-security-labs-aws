def normalize_event(ev):
    return {
        "eventName": ev.get("EventName"),
        "user": ev.get("Username"),
        "time": str(ev.get("EventTime"))
    }
