from setuptools import setup, find_packages

setup(
    name='futml-churn-prediction',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'xgboost',
        'shap',
        'matplotlib',
        'flask',
        'pytest'
    ],
)
