import setuptools   


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="slavniy-pypi-package",
    version="0.1.2",
    author="Slavniy D. M. ",
    author_email="herzenmoon@gmail.com",
    description="https://github.com/slavndn/prog5_lr3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slavndn/prog5_lr3",
    packages=setuptools.find_packages(),
    
    
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
     python_requires='>=3.6',
)