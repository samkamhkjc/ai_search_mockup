# Deploy as static site

Use the **project root** as the publish/output directory. No build step.

---

## Netlify

1. Push this repo to **GitHub** (or GitLab/Bitbucket).
2. Go to [netlify.com](https://netlify.com) → **Add new site** → **Import an existing project**.
3. Connect your repo.  
   - **Build command:** leave empty (or `#`)  
   - **Publish directory:** `.` (or leave default; `netlify.toml` sets it)
4. **Deploy**. You’ll get a URL like `https://random-name.netlify.app`.

---

## Vercel

1. Push to **GitHub**.
2. Go to [vercel.com](https://vercel.com) → **Add New** → **Project** → import the repo.
3. **Framework Preset:** Other (or leave auto).  
   - **Root Directory:** leave as `.`  
   - No build command needed for static.
4. **Deploy**. URL like `https://your-project.vercel.app`.

---

## GitHub Pages

1. Push to **GitHub**.
2. **Settings** → **Pages** → **Source:** Deploy from a branch.
3. **Branch:** `main` (or `master`) → **Folder:** `/ (root)** → **Save**.
4. Site: `https://<username>.github.io/<repo-name>/`

---

## Cloudflare Pages

1. Push to **GitHub**.
2. [dash.cloudflare.com](https://dash.cloudflare.com) → **Workers & Pages** → **Create** → **Pages** → **Connect to Git**.
3. Select repo.  
   - **Build command:** leave empty  
   - **Build output directory:** `.`
4. **Save and Deploy**. URL like `https://your-project.pages.dev`.
