from git import Repo, Git, rmtree
from tempfile import mkdtemp


def checkout(url, tag, no_git=True):
    temp_dir = mkdtemp()

    Repo.clone_from(url, temp_dir)
    repo = Git(temp_dir)
    repo.checkout(tag)
    if no_git:
        rmtree(temp_dir + "/.git")

    return temp_dir
