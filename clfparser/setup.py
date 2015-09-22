from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='clfparser',
      version='0.2',
      description='Apache Common/Combined Log Format Parser',
      long_description=readme(),
      classifiers=[
         'Development Status :: 3 - Alpha',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python :: 2.7',
         'Topic :: Text Processing'
      ],
      keywords='apache common combined log spark',
      url='http://github.com/nnon/commonlogformat.git',
      author='Rob Mackinnon',
      author_email='remackinnon@gmail.com',
      license='MIT',
      packages=['clfparser'],
      zip_safe=False)
