from setuptools import setup, find_packages

setup(
    name="phylo_converge",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "biopython",
        "matplotlib",
    ],
    entry_points={
        "console_scripts": [
            "phylo_converge=phylo_converge:main",
        ],
    },
    author="Ahmed Yassin",
    author_email="ahmedyassin300@outlook.com",
    description="A package to calculate genetic convergence and draw phylogenetic trees.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url=""
    classifiers=[
        "programming Language :: python :: 3",
        "License:: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',


)