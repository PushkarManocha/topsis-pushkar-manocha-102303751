from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="topsis-pushkar-manocha-102303751",
    version="1.0.1",
    author="Pushkar Manocha 102303751",
    author_email="pmanocha_be23@thapar.edu",
    description="TOPSIS (MCDM) implementation for ranking alternatives using multiple criteria.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["numpy", "pandas"],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "topsis-pushkar-manocha-102303751=topsis_pushkar_manocha_102303751.cli:main"
        ]
    },
)
