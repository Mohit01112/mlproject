from setuptools import setup, find_packages

def get_requirements(file_path):
    """Reads the requirements file and returns a list of dependencies."""
    with open(file_path) as f:
        requirements = f.read().splitlines()
        if '-e .' in requirements:
            requirements.remove('-e .')  # optional: remove editable mode
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="mohit",
    author_email="rajemohit330@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
