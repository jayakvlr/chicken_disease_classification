import setuptools

with open("README.md",encoding='utf-8') as f:
    long_description=f.read()

__version__="0.0.0"

REPO_NAME='Chicken disease classifier'
AUTHOR_USER_NAME='jayakvlr'
SRC_REPO='chicken_disease_classification'
AUTHOR_EMAIL='jayakvlr"gmail.com'

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A model MLOPS project for deep learning classification",
    long_description=long_description,
    long_description_content='text/markdown',
    url=f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}.git",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues"

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where='src')
)
