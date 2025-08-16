from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requiremets = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
        

setup(
    name="mlops_ud_1",
    version="0.0.1",
    author="HECTOR",
    author_email="hec2254@gmail.com",
    description="MLops Udemy",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
# c:\Users\HECTOR\Documents\HLor\Udemy\MLops_UD_1\stet.py