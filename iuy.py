from upload_files_to_github import upload_files_to_github

from github import Github

files = ['iuy.py']
branch = "main"
repo = 'dsdasadasdw/111'
token = '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'
upload_files_to_github(files, repo, token, branch)

#g = Github("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")
#user = g.get_user("dsdasadasdw")
#repo1 = user.get_repo("111")
#contents = repo1.get_contents("iuy.py")
#repo1.delete_file(contents.path, "ree", contents.sha, branch="main")



