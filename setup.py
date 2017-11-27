from setuptools import setup

setup(name='cpu_monitor',
      version='0.1',
      description='Cpu monitoring and burning tool',
      author='yotabits',
      author_email='tkostas75@gmail.com',
      license='MIT',
      url='https://github.com/yotabits/cpu_monitor',
      packages=['cpu_monitor'],
      scripts=['bin/cpu_monitor'],
      install_requires=[
          'py-cpuinfo',
          'plotly',
          'colorama',
          'dash',
          'dash_renderer',
          'dash_core_components',
          'dash_html_components'
      ],
      zip_safe=False)
