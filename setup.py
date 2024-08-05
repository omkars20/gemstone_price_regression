from setuptools import setup, find_packages

setup(
    name='gemstone_price_regression',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'mlflow'
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
