#!/bin/bash

# GitHub Setup Script for Student API Testing Project
# Usage: ./setup_github.sh <your-github-username> <repository-name>

if [ $# -eq 0 ]; then
    echo "Usage: $0 <github-username> [repository-name]"
    echo "Example: $0 johndoe student-api-testing"
    exit 1
fi

GITHUB_USERNAME=$1
REPO_NAME=${2:-"student-api-testing"}

echo "Setting up GitHub repository..."
echo "Username: $GITHUB_USERNAME"
echo "Repository: $REPO_NAME"
echo

# Add GitHub remote
git remote add origin https://github.com/YoussefElHodaiby/Student-Project.git

# Set upstream for main branch
git branch -M main

echo "GitHub remote added successfully!"
echo "Repository URL: https://github.com/YoussefElHodaiby/Student-Project"
echo
echo "Next steps:"
echo "1. Create a new repository on GitHub with the name: Student-Project"
echo "2. Run: git push -u origin main"
echo
echo "Or create and push in one go:"
echo "gh repo create $REPO_NAME --public --source=. --remote=origin --push"
