'''
Created on 18-Dec-2015

@author: Suman Saurabh
'''


from setuptools import setup


required_packages = [
    'Flask==0.10.1',
    'PyYaml==3.11',
    'Flask-RESTful==0.3.5',
    'Pygments==1.6',
    'Sphinx==1.2b1',
    'Werkzeug==0.9.1',
    'anyjson==0.3.3',
    'coverage==3.6',
    'docutils==0.10',
    'mock==1.0.1',
    'nose==1.3.0',
    'python-memcached==1.53',
    'requests==1.2.3',
    'selenium==2.48.0',
    'pyvirtualdisplay==0.1.5',
    'beautifulsoup4==4.4.1',
    'celery==3.1.19',
    'apscheduler==3.0.5',
    'sphinx-bootstrap-theme==0.3.1',
    'sphinxcontrib-httpdomain==1.1.9'
]

setup(
    name='tcapi.TrueCallerApp',
    description='CRUD operation on TrueCaller service',
    version='0.0.1',
    packages=['tcapi',
              'tcapi.TrueCallerApp'],
    namespace_packages=['tcapi'],
    install_requires=required_packages,
    dependency_links=[('https://github.com/surfly/gevent/tarball/master#'
                       'egg=gevent-1.0dev')],
    extras_require={
        'test': [
            'nose==1.3.0',
            'ddbmock==1.0.3',
        ]
    }
)
