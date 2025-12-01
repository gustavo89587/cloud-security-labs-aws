import boto3

def get_cloudtrail_events(limit=20):
    client = boto3.client("cloudtrail")
    events = client.lookup_events(MaxResults=limit)
    return events["Events"]

if __name__ == "__main__":
    for e in get_cloudtrail_events():
        print(e["EventName"], e["EventTime"])
