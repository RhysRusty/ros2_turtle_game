from setuptools import find_packages, setup

package_name = 'turtle_motion'

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
    maintainer='rr',
    maintainer_email='rr@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "go_to_goal = turtle_motion.turtle_goal:main",
            "turtle_spawner = turtle_motion.turtle_spawner:main"
        ],
    },
)