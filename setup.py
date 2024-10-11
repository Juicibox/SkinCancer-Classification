import setuptools

with open("README.md", "r", encoding="UTF-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "SkinCancer-Classification"
AUTHOR = "Juicibox"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "juiciboxchemstry@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A small CNN classifier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
