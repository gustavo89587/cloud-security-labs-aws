import boto3

def find_priv_escalation():
    client = boto3.client("iam")
    policies = client.list_policies(Scope="Local")["Policies"]
    risky = []
    for p in policies:
        v = client.get_policy_version(PolicyArn=p["Arn"], VersionId="v1")
        doc = v["PolicyVersion"]["Document"]
        if "Action" in str(doc) and "*" in str(doc):
            risky.append(p["Arn"])
    return risky

if __name__ == "__main__":
    print(find_priv_escalation())
