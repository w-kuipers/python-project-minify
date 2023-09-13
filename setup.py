import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-project-minify",
    version="1.0.1",
    author="Wibo Kuipers",
    author_email="w.kuipers@filmage.nl",
    description="A quick way to compile your Python project into it's most compact form. Built on the great python-minify package.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/w-kuipers/python-project-minify",
    project_urls={
        "Bug Tracker": "https://github.com/w-kuipers/python-project-minify/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['minify-project=python_project_minify.__main__:main']
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=['python-minifier==2.9.0', 'tqdm==4.66.1', 'colorama==0.4.6'],
)