# from setuptools import find_packages,setup
# from typing import List

# def get_requirements(file_path:str)->List[str]:
#     requirements=[]
#     with open(file_path) as file_obj:
#         requirements=file_obj.readlines()
#         requirements=[req.replace("\n","") for req in requirements]
#     return requirements


# setup(
#     name='FaultDetection ',
#     version='0.0.1',
#     author='Aman Aditya Mourya',
#     author_email= 'amanaditya450@gmail.com',
#     install_requires=get_requirements('requirements.txt'),
#     packages=find_packages( )

# )

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e.'

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.
    """
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        # Remove whitespace and filter comments/empty lines
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='FaultDetection',  # No trailing space
    version='0.0.1',
    author='Aman Aditya Mourya',
    author_email='amanaditya450@gmail.com',
    install_requires=get_requirements('requirements.txt'),  # Correct parameter name
    packages=find_packages()

)
