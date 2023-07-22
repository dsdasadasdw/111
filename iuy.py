from upload_files_to_github import upload_files_to_github

files = ['iuy.py']
branch = "main"
repo = 'dsdasadasdw/111'
token = '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'
upload_files_to_github(files, repo, token, branch)