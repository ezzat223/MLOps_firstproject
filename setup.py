from setuptools import find_packages, setup
from typing import List 

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str) -> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='diamond_price_prediction', # package name
    version='0.0.1',                 # initial version of the package
    author='Ezzat Fahmy',
    author_email='ezzat22hegazy@gmail.com',
    description='A package for predicting diamond prices',
    license='MIT',
    # A list of dependencies that will be installed when the package is installed.
    # You could replace it with the above function
    # install_requires=get_requirements('requirements.txt')
    install_requires=["scikit-learn","pandas","numpy"],
    packages=find_packages()
)