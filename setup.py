import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ftw-fedeotaran",
    version="0.0.1",
    author="Fede Otaran",
    author_email="otaran.federico@gmail.com",
    description="Simple dispatcher library based on data input",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fedeotaran/ftw",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
