from setuptools import setup, find_packages

setup(
    name="todo-cli",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click>=8.1.3",
        "pyyaml>=6.0",
        "colorama>=0.4.6"
    ],
    entry_points={
        "console_scripts": [
            "todo-cli=todo.main:cli",
        ],
    },
    python_requires=">=3.8",
)
