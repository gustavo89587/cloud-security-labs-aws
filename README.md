🛡️ Cloud Security-AWS (Detection Engineering + Hardening)
IAM • S3 Security • CloudTrail Analytics • Detection Engineering • Security Baseline

This repository brings together practical detections and hardening recommendations to strengthen the security posture in AWS environments.
It combines:

Detection Engineering

Threat Analysis with CloudTrail

IAM Privilege Escalation Detection

S3 Public Bucket Detection

Hardening and AWS Security Baseline best practices

Ideal for those working in SOC, Cloud Security, DevSecOps, Blue Team and DFIR.

🎯 Objectives of the repository

✔ Detect suspicious behavior and unsafe settings
✔ Strengthen security posture (Zero Trust + Least Privilege)
✔ Automate analytics with Python
✔ Assist in SOC / Cloud DFIR investigations
✔ Serve as a technical portfolio for recruiters

📁 Repository structure
cloud-security-aws/
│
├── iam/
│ └ ─ ─ iam_privilege_escalation.py
│
├── cloudtrail/
│ └ ─ ─ cloudtrail_analyzer.py
│
├── detections/
│ └ ─ ─ s3_public_buckets.py
│
hard── hardening/
│ ├ ─ ─ iam_hardening.md
│ ├ ─ ─ s3_hardening.md
│ ├ ─ ─ vpc_zero_trust.md
│ └ ─ ─ cloudtrail_baseline.md
│
└── requirements.txt


If the hardening/ folder doesn't already exist, you can create it: it makes the recruiter see real maturity.

🔍 Detection Engineering (Part 1)
1. IAM Privilege Escalation Detection

Script responsible for identifying policies and permissions that may result in privilege escalation, including:

Wildcard permissions"*"

iam: PassRole + ec2: RunInstances

IAM: Createpolicy version

Sts: misconfigured AssumeRole

Overly permissive Service accounts

MIT MITRE ATT&CK:

T1068-Privilege Escalation

T1078-Valid Accounts

T1098-Account Manipulation

2. CloudTrail Analyzer

Analyzes critical events such as:

Suspicious Logins

Creation / removal of users

Changes to roles / policies

Out-of-hours activity

Rare or sensitive API calls

This module helps:

✔ prioritize alerts
✔ identify anomalies
✔ support incident investigations
✔ generate indicators for SIEM

3. S3 Public Buckets Detection

Automated detection of exposed buckets for:

AllUsers

AllAuthenticatedUsers

Includes detection of:

Open ACLs

Permissive Policies

Critical data exposure failures

🔐 Hardening & Security Baseline (Part 2)

In addition to detections, this repository includes security best practices to strengthen the AWS environment.

IAM Hardening

MFA required

Strong password + rotation

Root without access keys

Extensive use of Roles

Removal of wildcard permissions

Policies based on the principle of Least Privilege

S3 Hardening

Blocking public access

SSE-S3 or SSE-KMS enabled

Versioning + MFA Delete

Lifecycle rules for retention

Monitoring suspicious accesses

VPC & Network Hardening

Segregation of subnets

Explicit Security Groups

Restrictive NACLs

Flow Logs enabled

Zero Trust in internal communications

CloudTrail & Audit

CloudTrail enabled in all regions

Logs sent to S3 private

Proper retention

Integration with CloudWatch Logs + metrics

Alerts for sensitive events

▶️ How to perform detections
pip install-r requirements.txt

python iam/iam_privilege_escalation.py
python cloudtrail/cloudtrail_analyzer.py
python detections/s3_public_buckets.py

🧠 Skills demonstrated with this repository

AWS Security

IAM Analysis

CloudTrail Threat Detection

S3 Exposure Detection

Hardening & Security Baseline

Python Automation

Security Best Practices

Zero Trust Architecture

SIEM-ready detection

Professional SoC / Cloud posture

📬 Contact

Gustavo Okamoto
Cybersecurity Analyst — SOC / Threat Detection / Cloud Security
📧 gugaokamoto1@gmail.com

🔗 linkedin.com/in/gustavo-okamoto-de-carvalho-ti
🔗 github.com/gustavo89587
