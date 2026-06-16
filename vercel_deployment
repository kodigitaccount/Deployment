# 🚀 INSTANT GRATIFICATION!

## Deploy a FastAPI Application to Production in Under 10 Minutes

This guide walks you through creating and deploying a simple FastAPI application to Vercel. By the end, you'll have a live API accessible from anywhere in the world.

---

# Prerequisites

Before starting, ensure you have:

* A computer running Windows, macOS, or Linux
* Internet access
* A GitHub account (recommended)
* Basic familiarity with using a terminal

---

# Step 1: Create a Vercel Account

1. Visit https://vercel.com
2. Click **Sign Up**
3. Select the **Hobby** plan
4. Sign up using:

   * GitHub (Recommended)
   * GitLab
   * Bitbucket
   * Email
5. Complete the onboarding process

---

# Step 2: Install Cursor IDE

Although any code editor can be used, this guide uses Cursor.

### Download Cursor

Visit:

https://cursor.com

Choose the installer for your operating system and complete the installation.

### Create a Project Folder

1. Open Cursor
2. Create a folder named:

```text
instant
```

3. Open the folder in Cursor

---

# Step 3: Create the FastAPI Application

Create a file named:

```text
instant.py
```

Add the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def instant():
    return "Live from production!"
```

Save the file.

---

# Step 4: Create requirements.txt

Create:

```text
requirements.txt
```

Add:

```text
fastapi
uvicorn
```

Save the file.

---

# Step 5: Configure Vercel

Create:

```text
vercel.json
```

Add:

```json
{
  "builds": [
    {
      "src": "instant.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "instant.py"
    }
  ]
}
```

Save the file.

---

# Step 6: Install Node.js

The Vercel CLI requires Node.js.

Download Node.js from:

https://nodejs.org

Verify installation:

```bash
node --version
npm --version
```

You should see version numbers for both commands.

---

# Step 7: Deploy to Vercel

Open a terminal in your project directory.

### Install Vercel CLI

```bash
npm install -g vercel
```

### Login

```bash
vercel login
```

Follow the authentication instructions.

### Deploy

```bash
vercel .
```

When prompted:

| Question                  | Answer            |
| ------------------------- | ----------------- |
| Set up and deploy?        | Yes               |
| Which scope?              | Personal Account  |
| Link to existing project? | No                |
| Project Name              | instant           |
| Code Directory            | Current Directory |

Wait for deployment to complete.

You will receive a URL similar to:

```text
https://instant-xxxx.vercel.app
```

Open the URL in your browser.

Expected output:

```text
Live from production!
```

---

# Project Structure

```text
instant/
├── instant.py
├── requirements.txt
├── vercel.json
└── README.md
```

---

# What You Learned

✅ Building a FastAPI application

✅ Configuring Python projects for Vercel

✅ Installing and using the Vercel CLI

✅ Deploying a production-ready API

✅ Hosting serverless applications

---

# Next Steps

Try extending the project by:

* Adding additional API endpoints
* Returning JSON responses
* Connecting a database
* Integrating with external APIs
* Setting up automatic GitHub deployments

---

# Troubleshooting

## "vercel: command not found"

Reinstall the CLI:

```bash
npm install -g vercel
```

Then restart your terminal.

---

## Deployment Fails

Verify that your project contains:

```text
instant.py
requirements.txt
vercel.json
```

and that you are deploying from the correct directory.

---

## Python Version Issues

Create:

```text
runtime.txt
```

Add:

```text
python-3.12
```

Redeploy the application.

---

# Resources

Vercel Documentation:
https://vercel.com/docs

FastAPI Documentation:
https://fastapi.tiangolo.com

Cursor:
https://cursor.com

Node.js:
https://nodejs.org

---

## Congratulations 🎉

You have successfully deployed a FastAPI application to production.

Your API is now:

* Live on the Internet
* Secured with HTTPS
* Automatically Scaled
* Ready for Real-World Use
