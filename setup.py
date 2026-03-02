from setuptools import find_packages, setup

setup(
    name="felo-finance",
    version="0.1.0",
    description="Felo - Programación en Finanzas",
    package_dir={"": "src"},
    packages=find_packages(where="src", include=["felo_finance*"]),
)