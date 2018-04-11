from setuptools import setup

from distutils.core import setup
from os import path
from setuptools.command.install import install

here = path.abspath(path.dirname(__file__))

# Create rst here from Markdown
if path.exists(path.join(here, 'README.md')):
    import pypandoc
    z = pypandoc.convert('README.md','rst',format='markdown')
    with open('README.rst','w') as outfile:
        outfile.write(z)

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(name='kiali-client',
      version='0.3',
      description='Python client to communicate with Kiali server over HTTP(S)',
      url='http://github.com/kialiqe/kiali-client-python',
      author='Guilherme Baufaker Rego',
      author_email='gbaufake@redhat.com',
      license='Apache License 2.0',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Monitoring',
      ],
      packages=['kiali'],
      zip_safe=False)