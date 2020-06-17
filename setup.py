import setuptools

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="dummy_libecl",
    version="0.0.1",
    author="R&T Equinor",
    description="A dummy package to be able to import fmu-ensemble without having libecl",
    long_description=LONG_DESCRIPTION,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
