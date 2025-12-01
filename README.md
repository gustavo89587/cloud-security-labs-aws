🛡️ Cloud Security – AWS (Detection Engineering + Hardening)
IAM • S3 Security • CloudTrail Analytics • Detection Engineering • Security Baseline

Este repositório reúne detecções práticas e recomendações de hardening para fortalecer a postura de segurança em ambientes AWS.
Ele combina:

Detection Engineering

Threat Analysis com CloudTrail

IAM Privilege Escalation Detection

S3 Public Bucket Detection

Hardening e boas práticas AWS Security Baseline

Ideal para quem atua em SOC, Cloud Security, DevSecOps, Blue Team e DFIR.

🎯 Objetivos do Repositório

✔ Detectar comportamentos suspeitos e configurações inseguras
✔ Fortalecer a postura de segurança (Zero Trust + Least Privilege)
✔ Automatizar análises com Python
✔ Ajudar em investigações SOC / Cloud DFIR
✔ Servir como portfólio técnico para recrutadores

📁 Estrutura do Repositório
cloud-security-aws/
│
├── iam/
│   └── iam_privilege_escalation.py
│
├── cloudtrail/
│   └── cloudtrail_analyzer.py
│
├── detections/
│   └── s3_public_buckets.py
│
├── hardening/
│   ├── iam_hardening.md
│   ├── s3_hardening.md
│   ├── vpc_zero_trust.md
│   └── cloudtrail_baseline.md
│
└── requirements.txt


Se a pasta hardening/ ainda não existir, pode criar: ela faz o recrutador ver maturidade real.

🔍 Detection Engineering (Parte 1)
1. IAM Privilege Escalation Detection

Script responsável por identificar políticas e permissões que podem resultar em escalonamento de privilégios, incluindo:

Permissões wildcard "*"

iam:PassRole + ec2:RunInstances

iam:CreatePolicyVersion

sts:AssumeRole mal configurado

Service accounts excessivamente permissivas

🧩 MITRE ATT&CK:

T1068 – Privilege Escalation

T1078 – Valid Accounts

T1098 – Account Manipulation

2. CloudTrail Analyzer

Analisa eventos críticos como:

Logins suspeitos

Criação/remoção de usuários

Alterações de roles/policies

Atividade fora de horário

API calls raras ou sensíveis

Este módulo ajuda a:

✔ priorizar alertas
✔ identificar anomalias
✔ apoiar investigações de incidentes
✔ gerar indicadores para SIEM

3. S3 Public Buckets Detection

Detecção automatizada de buckets expostos para:

AllUsers

AllAuthenticatedUsers

Inclui detecção de:

ACLs abertas

Policies permissivas

Falhas críticas de exposição de dados

🔐 Hardening & Security Baseline (Parte 2)

Além das detecções, este repositório inclui boas práticas de segurança para reforçar o ambiente AWS.

IAM Hardening

MFA obrigatório

Senha forte + rotação

Root sem access keys

Uso extensivo de Roles

Remoção de permissões wildcard

Políticas baseadas em princípio de menor privilégio

S3 Hardening

Bloqueio de acesso público

SSE-S3 ou SSE-KMS habilitado

Versionamento + MFA Delete

Lifecycle rules para retenção

Monitoramento de acessos suspeitos

VPC & Network Hardening

Segregação de subnets

Security Groups explícitos

NACLs restritivas

Flow Logs habilitados

Zero Trust nas comunicações internas

CloudTrail & Auditoria

CloudTrail habilitado em todas as regiões

Logs enviados para S3 privado

Retenção adequada

Integração com CloudWatch Logs + métricas

Alertas para eventos sensíveis

▶️ Como executar as detecções
pip install -r requirements.txt

python iam/iam_privilege_escalation.py
python cloudtrail/cloudtrail_analyzer.py
python detections/s3_public_buckets.py

🧠 Skills Demonstradas com Este Repositório

AWS Security

IAM Analysis

CloudTrail Threat Detection

S3 Exposure Detection

Hardening & Security Baseline

Python Automation

Security Best Practices

Zero Trust Architecture

SIEM-ready detections

Postura profissional SOC / Cloud

📬 Contato

Gustavo Okamoto
Cybersecurity Analyst — SOC | Threat Detection | Cloud Security
📧 gugaokamoto1@gmail.com

🔗 linkedin.com/in/gustavo-okamoto-de-carvalho-ti
🔗 github.com/gustavo89587
