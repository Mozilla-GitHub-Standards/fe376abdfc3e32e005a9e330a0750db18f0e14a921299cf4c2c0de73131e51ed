import os
from setuptools import setup, find_packages

ROOT = os.path.abspath(os.path.dirname(__file__))


setup(
    name='django-session-csrf',
    version='0.7.1',
    description='CSRF protection for Django without cookies.',
    long_description=open(os.path.join(ROOT, 'README.rst')).read(),
    author='Jeff Balogh',
    author_email='jbalogh@mozilla.com',
    url='http://github.com/mozilla/django-session-csrf',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',        
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
