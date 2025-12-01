import boto3

def find_public_buckets():
    s3 = boto3.client("s3")
    buckets = s3.list_buckets()["Buckets"]
    findings = []
    for b in buckets:
        acl = s3.get_bucket_acl(Bucket=b["Name"])
        grants = acl["Grants"]
        for g in grants:
            if g["Grantee"].get("URI") == "http://acs.amazonaws.com/groups/global/AllUsers":
                findings.append(b["Name"])
    return findings

if __name__ == "__main__":
    print(find_public_buckets())
