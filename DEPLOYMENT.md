# Deployment Guide

This guide will help you deploy your AI Writing Assistant to GitHub and Streamlit Cloud.

## 🚀 GitHub Deployment

### Step 1: Initialize Git Repository

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AI Writing Assistant"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git

# Push to GitHub
git push -u origin main
```

### Step 2: Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click "New repository"
3. Name your repository (e.g., `ai-writing-assistant`)
4. Make it public or private (your choice)
5. **Don't** initialize with README (since you already have one)
6. Click "Create repository"

### Step 3: Push Your Code

After creating the repository, GitHub will show you the commands. Use the ones above or follow GitHub's instructions.

## ☁️ Streamlit Cloud Deployment

### Step 1: Prepare for Streamlit Cloud

Your app is already configured for Streamlit Cloud with:
- ✅ `requirements.txt` with all dependencies
- ✅ `.streamlit/config.toml` for deployment settings
- ✅ Proper file structure

### Step 2: Deploy to Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io/)
2. Sign in with your GitHub account
3. Click "New app"
4. Select your repository: `YOUR_USERNAME/YOUR_REPO_NAME`
5. Set the main file path: `app.py`
6. Click "Deploy!"

### Step 3: Configure Environment Variables

After deployment, you need to add your Google API key:

1. In your Streamlit Cloud dashboard, go to your app
2. Click "Settings" (gear icon)
3. Go to "Secrets"
4. Add your Google API key:
   ```toml
   GOOGLE_API_KEY = "your-google-api-key-here"
   ```
5. Click "Save"

## 🔧 Alternative Deployment Options

### Heroku Deployment

1. Create a `Procfile`:
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. Add Heroku buildpack:
   ```bash
   heroku create your-app-name
   heroku buildpacks:set heroku/python
   ```

3. Deploy:
   ```bash
   git push heroku main
   ```

### Railway Deployment

1. Connect your GitHub repository to Railway
2. Railway will automatically detect it's a Python app
3. Add environment variable: `GOOGLE_API_KEY`
4. Deploy!

## 📋 Pre-deployment Checklist

- [ ] All files are committed to Git
- [ ] `.env` file is in `.gitignore` (✅ already done)
- [ ] `requirements.txt` is complete (✅ already done)
- [ ] No hardcoded API keys in code (✅ already done)
- [ ] README.md is updated (✅ already done)
- [ ] App runs locally without errors

## 🔍 Post-deployment Verification

1. **Test the deployed app**:
   - Upload a document
   - Try the writing assistant
   - Test all features

2. **Check for errors**:
   - Monitor Streamlit Cloud logs
   - Verify API key is working
   - Test all functionality

3. **Update documentation**:
   - Add deployment URL to README
   - Update any local-specific instructions

## 🛠️ Troubleshooting

### Common Issues

1. **API Key Not Working**:
   - Verify the key is correct
   - Check environment variable name
   - Ensure the key has proper permissions

2. **Dependencies Missing**:
   - Check `requirements.txt` is complete
   - Verify all imports are listed

3. **File Upload Issues**:
   - Check file size limits
   - Verify supported file types

### Getting Help

- Check Streamlit Cloud logs for errors
- Verify your Google AI API key is active
- Test locally first before deploying

## 🎉 Success!

Once deployed, your AI Writing Assistant will be available at:
`https://YOUR_APP_NAME-YOUR_USERNAME.streamlit.app`

Share this URL with others to let them use your app! 