from setuptools  import find_packages, setup

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()

__version__ = "1.0.0"

REPO_NAME = "EndToEndML_MLOPS"
AUTHOR_USER_NAME = "sk650897"
SRC_REPO = "MLproject"
AUTHOR_EMAIL = "sk650897@gmail.com"

setup(
name = SRC_REPO,
version = __version__,
author = AUTHOR_USER_NAME,
author_email = AUTHOR_EMAIL,
description = "A small python package for ML app",
long_description = long_description,
long_description_content = "text/markdown",
url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
project_urls ={
    "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
},
package_dir={"":"src"},
packages=find_packages(where="src")
)
