import setuptools

with open("README.md", "r") as file:
    description = file.read()

setuptools.setup(
    name="pymath",
    version="0.1",
    author="Dennis Lönard",
    author_email="dennis.loenard97@gmx.de",
    packages=["pymath"],
    description="A Python Wrapper for cmath-lib",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/loenard97/pymath-lib",
    license="GPL-3.0",
    python_requires=">=3.8",
    install_requires=[]
)