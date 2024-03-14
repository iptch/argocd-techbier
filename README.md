# argocd-techbier
![img_2.png](images/argocd_logo_transparent.png)

## Overview
This repository holds the manifests (Kubernetes .yaml files) for the hands-on part
of the ArgoCD TechBier taking place on March 14th, 2024.


## Hands-On Tasks

> Note: Whenever you encounter DEIN_KUERZEL put your ipt shortname, in my case `mhr`, to avoid conflicts.


### Part 1 - ArgoCD Basics 🤓
```
Goals
-----
[1] Understand and apply refresh.
[2] Understand and apply sync.
[3] Deploy your first ArgoCD Application.
```
**1.1 Exploring ArgoCD [5 min]**
- Visit the [argocd.codeandski.ch](https://argocd.codeandski.ch) web UI. Credentials will be put on a Flipchart.
- Try clicking around and answer the following questions. Discuss with your neighbour.
  - How many Applications are "Synced"? What options does the ArgoCD Dashboard give to monitor this?
  - What is your username, who issued it?
  - What `git` repositories are linked with this ArgoCD instance?
  - What `kubernetes clusters` are linked with this ArgoCD instance?
  - What is the difference between "Synced" and "Healthy"

**1.2 Fixing your Application in GitOps Style [10 min]**
- Find _your_ application (type DEIN_KUERZEL in the search, it's actually named hello_DEIN_KUERZEL). Open it up with: ![img.png](images/application_open_button.png)
- The Application seems to be out of sync. Why is that? Can you spot the reason?
- Implement the fix on YOUR BRANCH (!) and push it to GitHub
  <details>
  <summary>Hints for solution</summary>
  
  TODO: Explain the solution rather in detail here.
  </details>
- Go to your Applicaiton in ArgoCD. Hit _refresh_. What happened?
- Now hit _sync_. What happened? All green? Congrats!!!

**1.3 Creating your own ArgoCD Application [10 min]**
- 

### Part 2 - ArgoCD Advanced 😎
```
Goals
-----
[1] Understand and configure auto-sync.
[2] Working with the app-of-apps pattern? (Vorschlag)
```

**2.1 TODO: What do we do here?!**
...