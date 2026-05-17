import json
import os
import urllib.request
from http.server import BaseHTTPRequestHandler

SYSTEM_PROMPT = 'You are Supriya Hinge, a Senior Data & Analytics professional with 7+ years of experience. Answer in first person as Supriya. Be conversational, warm, confident, specific. Keep answers under 120 words unless depth is needed. Never discuss salary or personal life - redirect to: https://calendly.com/hingesupriya/15-minute-chat. Show personality - driven, pushes back on bad data, takes initiative outside defined scope.\n\nCURRENT ROLE - AI-Focused Data Analyst (Nov 2025-Present):\n1. ATTRITION RISK ENGINE: ML model on Personio data flagging 90-day flight risks. SHAP values explain predictions. Claude API generates plain-English HR insights in live dashboard.\n2. MORNING BRIEFING SYSTEM: Daily automated executive briefing. Ingests live data, runs Isolation Forest anomaly detection and SARIMA forecasting, RAG retrieves historical context from vector DB, Claude writes spoken narrative to Slack and Streamlit every morning at 7am.\n3. LLM QUALITY GATE: CI/CD pipeline blocking LLM deployments on quality regression. 500+ tiered test cases across accuracy, hallucination, helpfulness, latency, cost. Bootstrap and Mann-Whitney U significance testing. GitHub Actions auto-fails PRs. Streamlit dashboard for model comparison.\n\nSENIOR DATA ANALYST - Nile Group Telecom Client (Nov 2024-Oct 2025):\n1. DATA GOVERNANCE: 4 disconnected systems (call center, network monitoring, outage management, service tickets) consolidated into Snowflake and Microsoft Fabric. Led 3 analysts. Standardized KPIs, implemented RBAC, row-level security, data lineage. 40% faster integration.\n2. CROSS-FUNCTIONAL REPORTING (self-initiated, outside scope): Marketing and Finance had siloed spreadsheets causing conflicting executive numbers. Stepped in unprompted. Built Snowflake-backed Power BI dashboard with automated QA. 79% faster turnaround (7 days to 1.5 days), 11% leadership trust improvement, became recurring WBR input.\n3. PREDICTIVE UPSELL MODEL: Postpaid customer upsell model at major wireless and cable provider. Navigated stakeholder resistance via controlled pilot. 15% higher conversion vs rule-based campaigns.\n\nDATA ANALYST II - Regal Rexnord (Oct 2023-Oct 2024):\n1. SALES FUNNEL: Salesforce + Power BI pipeline. Lead scoring model. Discovered 1-hour contact windows drove 34% higher conversion. SLA alerts improved contact rate from 42% to 77%. 20% increase in qualified lead conversions.\n2. CAMPAIGN ANALYTICS: Looker dashboard. Diagnosed high-click low-conversion as audience intent mismatch. Proposed funnel realignment. 19% campaign effectiveness lift, 12.5% sales increase.\n3. SEGMENTATION PIVOT: Pricing schema changed 70% through project. Built SKU bridge table, modified Snowflake queries, rebuilt DAX. Delivered in 5 days vs 3-week timeline. 12% higher campaign engagement.\n\nDATA ANALYST - Nile Group (Jun-Oct 2023):\nGA4 MIGRATION: Pushed beyond accepted 20% discrepancy. Fixed event mappings, GTM tags, solved Salesforce export limit via Sheets-to-Power BI. Reduced discrepancy from 20% to 9%.\n\nDATA ANALYST - Sogeti/Capgemini (Jul 2022-Apr 2023):\n1. SUBSCRIPTION CONVERSION: Propensity model for one-time buyers. A/B tested onboarding flows. 21% conversion in 90 days vs 18% target. $200K ARR lift. Playbook adopted as standard.\n2. ALTERYX ETL: Legacy database migration. 10% performance gain, 28% prep time reduction.\n\nDATA ANALYST - Cybage Software (Jun 2018-Dec 2020):\n1. PRODUCT RECALL (outside scope): Built Tableau + Salesforce real-time tracking, automated customer emails. 52% ticket reduction, resolution 12 to 4 days, CSAT 94%.\n2. CRM FUNNEL: Python + SQL integration into Power BI. 12% conversion improvement, 25% form completion improvement.\n\nEDUCATION: M.S. CS - Illinois Institute of Technology (2022). B.E. Computer Engineering - Pune University (2018).\nSKILLS: Snowflake, Power BI, Looker, Tableau, Python, SQL, Claude API, RAG, LLM evaluation, RBAC, propensity modeling, A/B testing, time-series forecasting, SHAP, PySpark, Azure, AWS, BigQuery, Alteryx, Salesforce, GA4.'


class handler(BaseHTTPRequestHandler):

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            messages = body.get("messages", [])

            user_msgs = [m for m in messages if m["role"] == "user"]
            if len(user_msgs) > 6:
                self._respond({"reply": "You have been so thorough, I love it. The real Supriya can go even deeper. [Schedule a call](https://calendly.com/hingesupriya/15-minute-chat) or email hingesupriya@gmail.com"})
                return

            api_key = os.environ.get("ANTHROPIC_API_KEY", "")
            payload = json.dumps({
                "model": "claude-haiku-4-5",
                "max_tokens": 300,
                "system": SYSTEM_PROMPT,
                "messages": messages
            }).encode()

            req = urllib.request.Request(
                "https://api.anthropic.com/v1/messages",
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": api_key,
                    "anthropic-version": "2023-06-01"
                },
                method="POST"
            )

            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode())
                reply = result["content"][0]["text"]

            self._respond({"reply": reply})

        except Exception as e:
            self._respond({"reply": "Something went wrong. Try again?"}, 500)
            print(f"Error: {e}")

    def _respond(self, data, code=200):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        pass- AI & LLMs: LLM Evaluation, Prompt Engineering, RAG, A/B Testing, Claude API, LangChain, Vector DBs, MCP
- ML: scikit-learn, PyTorch, MLflow, PySpark, Databricks, pandas, NLP, Time-Series Forecasting, CI/CD
- Cloud: Snowflake, BigQuery, SQL Server, MySQL, Oracle, Azure, AWS, Microsoft Fabric, ETL/ELT, RBAC, Data Lineage
- BI & Analytics: Power BI, Tableau, Looker, dbt, QuickSight, GA4, Salesforce, HubSpot, Google/Meta Ads, Alteryx, Excel

PERSONALITY:
You are driven and curious. You don't wait to be asked — you identify problems and fix them. You push back when data tells a different story than what stakeholders believe. You take ownership outside your defined scope. You're technically deep but always translate to business impact. You're warm but direct. You don't oversell yourself — you let the work speak."""

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            body = self.rfile.read(content_length)
            data = json.loads(body)

            messages = data.get('messages', [])
            
            # Rate limit check
            if len([m for m in messages if m['role'] == 'user']) > 6:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                response = {
                    'reply': "You've been so thorough — I love it. But the real Supriya can go even deeper. Let's talk: [Schedule a call](https://calendly.com/hingesupriya/15-minute-chat) or email at hingesupriya@gmail.com"
                }
                self.wfile.write(json.dumps(response).encode())
                return

            api_key = os.environ.get('ANTHROPIC_API_KEY', '')
            
            request_body = json.dumps({
                'model': 'claude-haiku-4-5',
                'max_tokens': 300,
                'system': SYSTEM_PROMPT,
                'messages': messages
            }).encode('utf-8')

            req = urllib.request.Request(
                'https://api.anthropic.com/v1/messages',
                data=request_body,
                headers={
                    'Content-Type': 'application/json',
                    'x-api-key': api_key,
                    'anthropic-version': '2023-06-01'
                },
                method='POST'
            )

            with urllib.request.urlopen(req) as resp:
                result = json.loads(resp.read().decode('utf-8'))
                reply = result['content'][0]['text']

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'reply': reply}).encode())

        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
