from setuptools import setup

from distutils.core import setup



setup(name='kiali-client',
      packages=['kiali'],
      version='0.4.1',
      description='Python client to communicate with Kiali server over HTTP(S)',
      author='Guilherme Baufaker Rego',
      author_email='gbaufake@redhat.com',
      url='http://github.com/Kiali-QE/kiali-client-python',
      license='Apache License 2.0',
      keywords=["kiali, service-mesh, istio"],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Monitoring',
      ],

      zip_safe=False)
