from distutils.core import setup
setup(
    # How you named your package folder (MyLib)
    name='Topsis-Shubham-101903131',
    packages=['Topsis-Shubham-101903131'],   # Chose the same as "name"
    version='0.0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='Simple Topsis Alogrithum ',
    author='Shubham Trivedi',                   # Type in your name
    author_email='strivedi_b19@thapar.edu',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/Greatgabbar/topsis-package.git',
    # I explain this later on
    download_url='https://github.com/Greatgabbar/topsis-package/archive/refs/tags/0.0.1.zip',
    # Keywords that define your package best
    keywords=['topsis', 'python', 'Selection'],
    install_requires=[            # I get to this in a second
        'numpy',
        'pandas',
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
