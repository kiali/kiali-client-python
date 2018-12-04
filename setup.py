import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kiali-client",
    version="0.5.0",
    author="Guilherme Baufaker Rego",
    author_email="gbaufake@redhat.com",
    description="Python client to communicate with Kiali server over HTTP(S)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kiali/kiali-client-python",
    license='Apache License 2.0',
    keywords = "kiali, service-mesh, istio, kurbenetes, openshift",
    packages=setuptools.find_packages(),
    classifiers=(
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: System :: Monitoring',
    ),
)
