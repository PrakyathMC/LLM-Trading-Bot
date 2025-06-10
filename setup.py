
from setuptools import find_packages, setup


setup(
    name = "financebot",
    version="0.0.1",
    author="Prakyath",
    author_email="prakyathmc7@gmail.com",
    packages = find_packages(),
    install_requires = ["langchain==0.1.0", "langchain-community==0.0.13", "langchain-astradb"," datasets", "python-dotenv==1.0.0"," PyPDF2==3.0.1", "flask"]   
)