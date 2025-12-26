# KarmaFlow AI – Gemini-Powered Marathon Agent

KarmaFlow AI is an autonomous Marathon Agent built using the Gemini 3 family. 
It plans, executes, verifies, and self-corrects multi-day goals with persistent memory 
and graceful handling of real-world constraints like API rate limits.

## 🚀 Features
- Long-horizon planning with Gemini
- Autonomous execution with retries
- Independent verification & self-correction
- Persistent memory across runs
- Rate-limit aware reasoning
- Lightweight dashboard UI for observability

## 🧠 Architecture
Plan → Execute → Verify → Self-Correct → Persist Memory

## 🖥️ Demo
The demo showcases an autonomous job-hunt workflow executed over multiple days.

## 🛠 Tech Stack
- Python
- Google Gemini 3 (Flash / Pro Preview)
- Google AI Studio
- Flask
- HTML/CSS

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python agent.py
python ui.py
