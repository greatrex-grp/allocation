import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fp:
    install_requires = fp.read()

print(setuptools.find_packages())

setuptools.setup(
    name="allocation",
    version="1.0.0",
    author="David Greatrex",
    author_email="dcgreatrex@gmail.com",
    description="Allocation algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/greatrex-grp/allocation",
    packages=setuptools.find_packages(),
    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)