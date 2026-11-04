# MADARA AI Studio
Mobile-first Flask + HTML/CSS/JS AI studio starter.

## Features
- iOS-inspired 3D glass and OLED dark responsive UI
- AI chat interface with browser-local chat history (demo responses)
- Image prompt studio interface
- File upload/download for TXT, MD, PDF, images, code and ZIP (20 MB max)
- Render Blueprint (`render.yaml`)

## Run locally
```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Open http://127.0.0.1:5000.

## Deploy on Render
Push this folder to GitHub, then Render → New + → Blueprint → select repository → keep `render.yaml` → Deploy.

## Note
Chat replies and image generation are demo UI only until a server-side AI provider is connected. Never place private API keys in frontend JavaScript or commit them to GitHub. Render free service local uploads may not persist after restarts/redeploys.
