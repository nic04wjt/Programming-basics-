# PracticeGit

## Overview
This folder is a practice repository designed to help learners understand and master the fundamentals of Git version control. It serves as a sandbox environment where you can safely experiment with various Git commands and workflows without affecting a production codebase.

## Contents
This repository contains resources and exercises related to Git basics, including:
- Practice scenarios for common Git operations
- Example workflows and branching strategies
- Documentation and guides for Git commands

## Purpose
This is a **practice folder** intended for educational purposes. Use it to learn Git concepts hands-on by executing real commands and observing their outcomes.

## Common Git Commands to Practice
- `git init` - Initialize a new repository
- `git add <file>` - Stage changes for commit
- `git commit -m "message"` - Commit staged changes
- `git status` - Check repository status
- `git log` - View commit history
- `git branch` - List, create, or delete branches
- `git checkout -b <branch>` - Create and switch to a new branch
- `git merge <branch>` - Merge branches
- `git push` - Push commits to remote repository
- `git pull` - Pull updates from remote repository

## Virtual Environment Setup

1. Create the environment: `python -m venv env`
2. Activate it:
  - Windows: `env\Scripts\activate`
  - Mac/Linux: `source env/bin/activate`
3. Install libraries: `pip install pandas numpy matplotlib`

## Creating a .gitignore File

1. Create a new file in your project root: `touch .gitignore`
2. Add the virtual environment folder:
  ```
  env/
  ```
3. Add other common Python files to ignore:
  ```
  __pycache__/
  *.pyc
  .DS_Store
  ```
4. Save the file and commit it to your repository