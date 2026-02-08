# GitHub API User Info Fetcher

A Python script that uses GitHub's REST API to fetch and display user information.

## What It Does

This is a command-line tool that lets you look up any GitHub user and see their:
- Followers list
- Following list
- Basic profile info (name, login, follower/following counts)
- Repository details (names, visibility, fork status, default branch)

## How It Works

The script uses the `requests` library to make HTTP GET requests to GitHub's public API endpoints:
- `https://api.github.com/users/{username}` - Basic user info
- `https://api.github.com/users/{username}/followers` - Followers
- `https://api.github.com/users/{username}/following` - Following
- `https://api.github.com/users/{username}/repos` - Repositories

No authentication is needed since it only accesses public data.

## Usage

```bash
python api2.py
```

When you run it:
1. Enter a GitHub username
2. Choose from the menu:
   - 1: See who they're following
   - 2: See their followers
   - 3: See basic profile info
   - 4: See repository details
   - 5: Exit

## Requirements

```bash
pip install requests
```

## Example

```
Enter the username you would like to show details of: torvalds

What operation would you like to perform to fetch from GITHUB?
1: Following
2: Followers
3: Basic info
4: Repository details
5: Exit
Enter the choice (1-5): 3

torvalds has the basic info:
Name: Linus Torvalds
Login: torvalds
Total followers: 200000
Total following: 0
```

## API Rate Limits

GitHub allows 60 requests per hour for unauthenticated requests. If you need more, you can add a personal access token to the headers.
