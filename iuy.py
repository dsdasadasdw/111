from upload_files_to_github import upload_files_to_github

from github import Github

files = ['iuy.py']
branch = "main"
repo = 'dsdasadasdw/111'
token = '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'

g = Github("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")
user = g.get_user("dsdasadasdw")
repo1 = user.get_repo("111")
contents = repo1.get_contents("iuy.py")
repo1.delete_file(contents.path, "ree", contents.sha, branch="main")

upload_files_to_github(files, repo, token, branch)





