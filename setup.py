from setuptools import setup, find_packages

setup(
    name="reconx",
    version="1.0.0",
    author="Purushotham R",
    author_email="your_email@example.com",
    description="A personal reconnaissance framework for bug bounty",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/reconx",
    packages=find_packages(),
    py_modules=["reconx"],
    python_requires=">=3.8",
    install_requires=[
        "requests",
        "httpx",
        "aiohttp",
        "asyncio",
        "pyjsparser",
        "beautifulsoup4",
        "slack_sdk",
        "discord-webhook",
        "colorama",
        "termcolor",
        "rich",
        "pyyaml",
        "tqdm",
        "packaging",
        "regex"
    ],
    entry_points={
        "console_scripts": [
            "reconx = reconx:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
