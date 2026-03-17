# CompositeLab — ML Property Predictor (Netlify)

Serverless ML prediction tool for composite material properties using Netlify Functions.

## Stack
- **Backend**: Flask (Netlify Functions)
- **Frontend**: Vanilla JS + Chart.js + CDN
- **Deploy**: Netlify

## Local Setup

```bash
# 1. Install
pip install -r requirements.txt
npm install -g netlify-cli

# 2. Environment
cp .env.example .env
# Add GROQ_API_KEY

# 3. Test locally
netlify dev
# Visit http://localhost:8888
```

## Deploy to Netlify

```bash
# 1. Push to GitHub
git init && git add . && git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/composite-webapp.git
git push -u origin main

# 2. Connect Netlify
# - Go to netlify.com
# - Click "Add new site → Import an existing project"
# - Select GitHub repo
# - Build command: pip install -r requirements.txt
# - Publish directory: netlify-dist
# - Functions directory: netlify/functions

# 3. Add environment
# - Site settings → Environment
# - Add: GROQ_API_KEY
```

## Features
- Forward prediction (input composition → get properties)
- Inverse prediction (input properties → get optimal composition)
- Real-time charts with uncertainty bands
- AI assistant with Groq integration
- Error landscape heatmap

## Notes
- Models train per session (Netlify ephemeral storage)
- Users upload Excel files each time
- Perfect for demos and prototypes
- Free tier: 125k invocations/month
