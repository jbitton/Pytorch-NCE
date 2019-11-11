import setuptools


setuptools.setup(
    name='pytorch-nce2',
    version='0.0.1',
    author='Kaiyu Shi',
    author_email='skyisno.1@gmail.com',
    description='An NCE implementation in pytorch',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Stonesjtu/Pytorch-NCE',
    packages=['nce'],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
