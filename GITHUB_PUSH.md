# Push this project to GitHub

The project is already initialized as a Git repo, committed, and has `origin` set to  
`https://github.com/samkamhkjc/ai_search_mockup.git`.

## 1. Create the repo on GitHub

Create **ai_search_mockup** under your account:

- **Quick create:**  
  [https://github.com/new?name=ai_search_mockup](https://github.com/new?name=ai_search_mockup)
- Leave “Initialize with README” **unchecked** (we already have local commits).
- Click **Create repository**.

## 2. Push from your machine

In **PowerShell** or **Command Prompt** (outside Cursor, if you hit proxy issues):

```powershell
cd "c:\Users\HKJCUser\PycharmProjects\ai_search_mockup"
git push -u origin master
```

If GitHub asks for auth, sign in (browser or token) when prompted.

---

**Optional:** If you use **GitHub CLI** (`gh`), you can create the repo and push in one go:

```powershell
cd "c:\Users\HKJCUser\PycharmProjects\ai_search_mockup"
gh repo create ai_search_mockup --private --source=. --remote=origin --push
```

Use `--public` instead of `--private` if you want a public repo.
