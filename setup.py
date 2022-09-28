import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='teste',
    version='0.0.1',
    author='Paulo Fappi',
    author_email='paulo.fappi@jumplabel.com.br',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://bitbucket.org/jumplabel-projetos/teste-packege/',
    project_urls = {
        "Bug Tracker": "https://github.com/Muls/toolbox/issues"
    },
    license='MIT',
    packages=['teste-packege'],
    install_requires=['requests'],
)