from setuptools import setup, find_packages

setup(
      name='door',
      version='0.0.1',
      description='Environment to simulate door opening tasks',
      author='Erick Rosete Beas',
      author_email='erickrosetebeas@hotmail.com',
      url='https://github.com/ErickRosete/Time-Contrastive-Networks',
      packages=find_packages(),
      install_requires=[
                'tacto',
                'gym(==0.18.3)',
                'hydra.core(==1.1.0)',
                'pybulletX(==0.4.1)']
     )
