from setuptools import setup

setup(
    name="reconx",
    version="1.0",
    py_modules=["reconx"],
    install_requires=[],
    entry_points={
        "console_scripts": [
            "reconx=reconx:main"
        ]
    },
    author="Purushotham R",
    description="Bug bounty focused reconnaissance framework",
)
