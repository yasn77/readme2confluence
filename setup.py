import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="readme2confluence",
    version='0.1.4',
    author="Yasser Saleemi",
    author_email="yasser.saleemi@gmail.com",
    description="Create Confluence page from README",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yasn77/readme2confluence",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['markdown2==2.3.8', 'atlassian-python-api==1.13.29', 'Click==7.0'],
    entry_points={
        'console_scripts': [
            'readme2confluence = readme2confluence.cli:cli'
        ]
    }
)
