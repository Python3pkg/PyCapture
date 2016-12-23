from setuptools import setup

setup(
    name='PyCapture',
    version=__import__('pycapture').__version__,
    url='https://github.com/Manato0x2cc/PyCapture',
    author='Manato0x2cc',
    author_email='manato0x2cc@gmail.com',
    description=('Take a screenshot from Python Script'),
    license='Apache',
    packages=['pycapture'],
    test_suite='tests',
    install_requires=['PyAutoGUI'],
    keywords="gui screenshot capture img image",
    classifiers=[
        'Environment :: MacOS X',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
)
