from setuptools import find_packages,setup

setup(
    name='MCQ_GENARATOR',
    version='0.0.1',
    author='M BASAVA RAJU',
    author_email='ramatam05@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)