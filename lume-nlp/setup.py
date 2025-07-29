from setuptools import setup, find_packages

setup(
    name="lume_nlp",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "transformers",
        "torch",
        "numpy",
        "pandas",
        "scikit-learn"
    ],
)