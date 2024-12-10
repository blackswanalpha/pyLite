from setuptools import setup, find_packages

setup(
    name='pylite',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'SQLAlchemy',
        'Flask-SQLAlchemy',
        'click',
        # Add other necessary dependencies
    ],
    entry_points={
        'console_scripts': [
            'pylite=pylite.cli:main',
        ],
    },
    author=' kamande_mbugua-97.18',
    author_email='kamandembugua18@gmail.com',
    description='A lightweight framework for creating desktop, mobile, and web applications.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/blackswanalpha/pyLite',  # Update this with your actual repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
