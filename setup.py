from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(

    name="emailbot",
    version="0.0.0",
    author="Craig Macfadyen",
    author_email="cdmacfadyen@gmail.com",
    description="Simple package to email you when scripts are finished.",
    long_description=long_description,
    long_description_content_type="text/markdown",   
    url="https://github.com/cdmacfadyen/emailbot",
    packages=["emailbot"],
    keywords=["email","simple"],
    classifiers=[
    'Development Status :: 4 - Beta',      
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3',      
    ],
)