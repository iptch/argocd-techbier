import subprocess
import os

# Replace these paths with your actual paths
repo_path = "/Users/matt/code/argocd-techbier"
manifests_file_path = "hello-techbier-template.yaml"

# List of branch names
branch_names = [
    "sta", "aka", "csb", "oto", "aba", "bju", "dkn", "dng", "fst", "jgr", "jhu", "kdu", "mkc", "meg", "ost",
    "pfi", "rbe", "sho", "tsh", "vvo", "wga", "gme", "pni"
]  # Add more names as needed

# Ensure you are in the repo directory
os.chdir(repo_path)

# Read the content of your manifests.yaml file
with open(manifests_file_path, 'r') as file:
    manifests_content = file.read()

for branch_name in branch_names:
    # Checkout to a new branch for each name. It will create the branch if it doesn't exist.
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)
    print(f'checked out {branch_name}')
    # Ensure the src directory exists
    os.makedirs(os.path.join(repo_path, "src"), exist_ok=True)

    # Path to the manifests.yaml in the repo
    repo_manifests_path = os.path.join(repo_path, "src", "manifests.yaml")

    # Write the content to manifests.yaml in the current branch
    with open(repo_manifests_path, 'w') as file:
        file.write(manifests_content)
    print(f'wrote file {repo_manifests_path}')

    # Add the manifests.yaml file to the staging area
    subprocess.run(["git", "add", "src/manifests.yaml"], check=True)
    print(f'ran git add')

    # Commit the change
    subprocess.run(["git", "commit", "-m", f"Add manifests.yaml to {branch_name}"], check=False)
    print(f'ran git commit')

    # Push the branch to the remote repository. Replace 'origin' with your remote name if it's different.
    subprocess.run(["git", "push", "--set-upstream", "origin", branch_name], check=True)
    print(f'ran git push')

    # Optional: Checkout back to your main branch or any branch you want to return to after the operation
    subprocess.run(["git", "checkout", "mhr"], check=True)