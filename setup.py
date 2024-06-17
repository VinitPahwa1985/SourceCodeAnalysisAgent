from setuptools import find_packages, setup

setup(
    name="Source code analysis ai agent",
    version="0.0.1",
    author="Vinit pahwa",
    author_email="pahwavinit1512@gmail.com",
    packages=find_packages(),
    install_requires=["faiss-cpu","groq","langchain-groq","PyPDF2","langchain_google_genai","langchain","streamlit","langchain_community","python-dotenv","pypdf","google-cloud-aiplatform>=1.38","GitPython","chromadb"]
)