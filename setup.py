from setuptools import setup

setup(name='cpu_monitor',
      version='0.1',
      description='Cpu monitoring and burning tool',
      author='yotabits',
      author_email='tkostas75@gmail.com',
      license='MIT',
      packages=['cpu_monitor'],
      scripts=['bin/cpu_watcher'],
      install_requires=[
          'py-cpuinfo',
          'plotly',
          'dash',
          'dash_renderer',
          'dash_core_components',
          'dash_html_components'
      ],
      zip_safe=False)