from setuptools import find_packages,setup

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->list:
    '''
    this function will return the list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith('#')]#req.strip() removes any leading or trailing whitespace characters.
#if req.strip() and not req.startswith('#') filters out empty lines and comments.
       
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='nlp_txt_clssfctn',
version='0.0.1',
author='Fina',
author_email='finarheiner.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)
