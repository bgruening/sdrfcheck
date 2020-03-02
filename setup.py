from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()

ENTRY_POINTS = '''
        [console_scripts]
        sdrtcheck=sdrfcheck.sdrfcheck:cli
'''

setup(name='sdrfcheck',
      version='0.0.4',
      description='Python tools for SDRF proteomics validation',
      url='http://github.com/bigbio/sdrfcheck',
      long_description=readme(),
      long_description_content_type='text/markdown',
      author='BigBio Team',
      entry_points=ENTRY_POINTS,
      author_email='ypriverol@gmail.com',
      license='LICENSE',
      include_package_data=True,
      install_requires=['requests', 'pandas_schema', 'pandas', 'ebi-ols-client', 'click'],
      scripts=['sdrfcheck/sdrfcheck.py'],
      packages=find_packages(),
      python_requires='>=3.4',
      zip_safe=False)
