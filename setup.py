from setuptools import setup,find_packages

setup(name='prake',
      version='0.1',
      description='Rapid Automatic Keywords Extraction',
      url='http://https://github.com/vitaled/prake/',
      author='Daniele Vitale',
      author_email='vitaled@gmail.com',
      license='Apache',
      packages=find_packages(),	
      package_data = {'data':['*.txt']},
      include_package_data=True,
      zip_safe=False)

      #packages=['prake'],

