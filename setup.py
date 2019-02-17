import setuptools

with open('README.md', 'r') as description_file:
    long_description = description_file.read()

setuptools.setup(name='Commands', version='0.0.1', author='Ivanenko Denis', author_email='ivanenko@ucu.edu.ua',
                 description='App to view .json files of any size.', long_description=long_description,
                 long_description_content_type='text/markdown', url='https://github.com/LilJohny/TwitterMap.git',
                 packages=setuptools.find_packages(),
                 classifiers=[
                     "Programming Language :: Python :: 3",
                     "License :: OSI Approved :: MIT License",
                     "Operating System :: OS Independent",
                 ], )
