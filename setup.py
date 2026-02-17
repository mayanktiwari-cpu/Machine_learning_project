from setuptools import find_packages,setup
from typing import List

e_dot= "-e ."
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if e_dot in requirements:
            requirements.remove()

    return requirements

setup(
    name="Price_optimization",
    version="0.0.1",
    author="Mayank",
    packages=find_packages(),
    install_requires=get_requirements("requirement.txt")
)
    




