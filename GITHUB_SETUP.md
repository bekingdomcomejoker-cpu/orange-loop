# GitHub Setup Guide

Follow these steps to push your Orange Loop repository to GitHub.

## Prerequisites

1. A GitHub account.
2. GitHub CLI (`gh`) installed in Termux:
   ```bash
   pkg install gh
   ```

## Steps to Push

1. **Login to GitHub**:
   ```bash
   gh auth login
   ```

2. **Initialize Git**:
   ```bash
   git init
   ```

3. **Add Files**:
   ```bash
   git add .
   ```

4. **Commit**:
   ```bash
   git commit -m "Initial commit: Orange Loop v1.1 - Canonical Architecture"
   ```

5. **Create Repository and Push**:
   ```bash
   gh repo create orange-loop --public --source=. --remote=origin --push
   ```

Your repository will be live at `github.com/YOUR_USERNAME/orange-loop`.
