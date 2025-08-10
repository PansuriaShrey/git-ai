# **git-ai**

_AI-powered Git commands using AWS Bedrock & Claude AI_

## Overview

**git-ai** is a collection of AI-powered Git commands that enhance your development workflow.  
Currently includes tools for generating professional commit messages, with more AI-powered Git utilities coming soon.

### Available Commands

- **`acm`** - AI-powered commit message generator
  - Analyzes your code changes and suggests commit messages following the **Conventional Commits** standard
  - Powered by **Claude 3.5 Sonnet** via **AWS Bedrock**

## Prerequisites

- Python 3.9+
- Poetry
- Git
- AWS credentials with Bedrock access

## Installation

```bash
./install.sh
```

## Configuration

Set your AWS credentials using one of these methods:

**Option 1: Environment Variables**

```bash
export AWS_ACCESS_KEY_ID=your_access_key_here
export AWS_SECRET_ACCESS_KEY=your_secret_key_here
export AWS_REGION=us-east-1
```

**Option 2: .env File**

```bash
# Create .env file
AWS_ACCESS_KEY_ID=your_access_key_here
AWS_SECRET_ACCESS_KEY=your_secret_key_here
AWS_REGION=us-east-1
```

## Usage in your repo

### Using the `acm` command

```bash
# Stage your changes
git add .

# Generate commit message
acm
```
