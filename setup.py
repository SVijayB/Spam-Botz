import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Spam-Botz", # Replace with your own username
    version="1.0.0",
    author="S Vijay Balaji",
    author_email="vijaybalajitheboss@gmail.com",
    description="A simple and easy to use Spam Bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.vijaybalaji.social/Spam-Botz/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)