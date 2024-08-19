from setuptools import setup

setup(
    name='cloudflare-bypasser',
    version='0.1',
    py_modules=['CloudflareBypasser'],
    install_requires=[
        'DrissionPage==4.0.5.6'
    ],
    include_package_data=True,
)
