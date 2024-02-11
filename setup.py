from setuptools import setup, find_packages

setup(
    name='Ragbuilder',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        "google-generativeai",
        "langchain-google-genai",
        "chromadb",
        "pypdf",
      ],
    author='Loaii abdalslam',
    author_email='loaiabdalslam@gmail.com',
    description='RAG Builder For Applications using Gemeni and Google Embeddings and Chromadb.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/loaiabdalslam/Ragbuilder',
    license='MIT',
)