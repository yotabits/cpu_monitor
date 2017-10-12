from setuptools import setup

setup(name='cpu_monitor',
      version='0.1',
      description='Cpu monitoring and burning tool',
      author='yotabits',
      author_email='tkostas75@gmail.com',
      license='MIT',
      packages=['cpu_monitor'],
      install_requires=[
          'py-cpuinfo',
      ],
      zip_safe=False)