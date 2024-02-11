from setuptools import setup, find_packages

setup(
    name='RagBulder',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "google-generativeai",
        "langchain-google-genai",
        "chromadb",
        "pypdf",
        # add any dependencies here
    ],
    author='Loaii abdalslam',
    author_email='loaiabdalslam@gmail.com',
    description='A short description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/loaiabdalslam/Ragbuilder',
    license='MIT',
)