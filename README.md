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

**1.2 Creating and Fixing your Application in GitOps Style [10 min]**
- Checkout the git repository https://github.com/iptch/argocd-techbier.git
- Checkout your branch `git checkout DEIN_KUERZEL`
- Change the DEIN_KUERZEL occurrences in the src/manifests.yaml file and push it to GitHub.
- Let's create an ArgoCD App via the UI. Hit "New App" in the ArgoCD UI.
  - Give the app the name "hello-techbier-DEIN_KUERZEL" (simply the name of the ArgoCD Application)
  - Project name: "Default" (can be used to group Applications, we simply use Default for everything here)
  - Sync Policy: "Manual"
  - Repository URL: https://github.com/iptch/argocd-techbier.git
  - Revision: "DEIN_KUREZEL" (this is simply the branch to point to for the source)
  - Path: "src" (the folder in which to look for manifests)
  - Destination: "https://kubernetes.default.svc" (this points to the local cluster where ArgoCD runs in)
  - Namespace: "ns-techbier-DEIN_KUERZEL" (the namespace must match ne ns in the manifest)
  - --> Hit Create!
- The App seems to be out of sync... Hit _sync_.
- It seems that something is wrong... The App is still out of sync. Looks like we have to fix something.
- Implement the fix on YOUR BRANCH (!) and push it to GitHub.
  <details>
  <summary>Hints for solution</summary>
  
  Check the labels. You can put the whole manifest into ChatGPT and ask him whats wrong. He will tell you.
  </details>
- Go to your Applicaiton in ArgoCD. Hit _refresh_. What happened?
- Now hit _refresh_ and _sync_. What happened? All green? Congrats!!!

### Part 2 - ArgoCD Advanced 😎
```
Goals
-----
[1] Understand and configure auto-sync.
[2] Working with the app-of-apps pattern (for the very fast).
```

**2.1 TODO: Autosync?!**
- Change your Application and enable Autosync via the UI (check-box at the bottom).
- Refresh and sync your Application.
- Now change the number of replicas to 10 and push it. Did it scale automatically?