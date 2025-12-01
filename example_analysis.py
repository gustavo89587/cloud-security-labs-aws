from cloudtrail.cloudtrail_analyzer import get_cloudtrail_events
from detections.s3_public_buckets import find_public_buckets

print("CloudTrail Events:")
print(get_cloudtrail_events())

print("\nPublic S3 Buckets:")
print(find_public_buckets())
