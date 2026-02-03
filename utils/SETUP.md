# Getting Started

---

## Step 1: Create a GitHub Account

If you don't already have one:

1. Go to **[github.com/signup](https://github.com/signup)**
2. Sign up with your email
3. Verify your email address

---

## Step 2: Install Homebrew

Homebrew is a package manager for Mac that makes installing software easy.

**Open Terminal** (press `Cmd + Space`, type "Terminal", hit Enter) and paste this command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Follow the prompts. When it's done, **restart your Terminal**.

> **Note:** After installation, you may need to run two commands it shows you to add Homebrew to your PATH. They'll look something like:
> ```bash
> echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
> eval "$(/opt/homebrew/bin/brew shellenv)"
> ```

---

## Step 3: Install Your AI Coding Tools

Once Homebrew is installed, run these commands in Terminal:

### Install Google Antigravity
```bash
brew install --cask antigravity
```

### Install Cursor
```bash
brew install --cask cursor
```

### Install GitHub CLI (for cloning repos)
```bash
brew install gh
```

---

## Step 4: Get Free Student Access

### Cursor (Free for 1 Year)

1. Go to **[cursor.com/students](https://cursor.com/students)**
2. Sign up with your student email (.edu)
3. Get Cursor Pro free for 1 year

### Google Gemini (Free for Students)

1. Go to **[gemini.google/students](https://gemini.google/students/)**
2. Sign in with your Google account
3. Verify your student status
4. Get free access to Gemini Advanced

---

## Step 5: Clone This Repo

First, authenticate with GitHub:

```bash
gh auth login
```

Choose:
- GitHub.com
- HTTPS
- Login with a web browser

Then clone this repo:

```bash
gh repo clone YOUR_USERNAME/sj-mba
```

This will download the project to your computer. Navigate into it:

```bash
cd sj-mba
```

Now you can open it in Cursor or Antigravity!

---

## Quick Reference

| Tool | What it does |
|------|--------------|
| **Antigravity** | Google's AI-powered IDE (VS Code fork) with Gemini built-in |
| **Cursor** | AI-powered IDE with Claude/GPT integration |
| **GitHub CLI** | Interact with GitHub from your terminal |

---

## Opening Projects in Your IDE

### In Cursor
```bash
cursor .
```

### In Antigravity
```bash
antigravity .
```

(Or just open the apps and use File > Open Folder)

---

## Need Help?

If something doesn't work:
1. Make sure you restarted Terminal after installing Homebrew
2. Try running `brew doctor` to check for issues
3. Text me!
