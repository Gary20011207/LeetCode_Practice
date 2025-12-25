#!/bin/bash

# LeetCode Practice Git Push Script

current_date=$(date +"%Y/%m/%d")

# Initialize git repo if not exists
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
fi

# Ensure branch is named main
git branch -M main

# Create .gitignore if not exists
if [ ! -f ".gitignore" ]; then
    echo "Creating .gitignore..."
    cat > .gitignore << EOF
.DS_Store
*.pyc
__pycache__/
.venv/
.env
EOF
fi

# Remove .DS_Store from git cache (if previously tracked)
git rm -r --cached .DS_Store 2>/dev/null
find . -name ".DS_Store" -exec git rm -r --cached {} + 2>/dev/null

# Check if remote exists
if ! git remote | grep -q "origin"; then
    echo "No remote found."
    echo "Please add your GitHub repo first:"
    echo "  git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git"
    exit 1
fi

# Add, commit, push
git add .
git commit -m "Upload on $current_date"
git push -u origin main

echo "Done!"
