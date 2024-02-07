from setuptools import find_packages, setup

package_name = 'robotutorial_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='turtlehouse',
    maintainer_email='darya.minieieva@ucu.edu.ua',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'robotutorial_python_node = robotutorial_python.robotutorial_python_node:main'
        ],
    },
)
