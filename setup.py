from setuptools import find_packages, setup

package_name = 'comprobo_warmup_project'

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
    maintainer='mampane',
    maintainer_email='mampane@olin.edu',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop = comprobo_warmup_project.teleop:main',
            'drive_square = comprobo_warmup_project.drive_square:main',
            'wall_follower = comprobo_warmup_project.wall_follower:main',
            'person_follower = comprobo_warmup_project.person_follower:main',
            'obstacle_avoider = comprobo_warmup_project.obstacle_avoider:main',
            'finite_state_controller = comprobo_warmup_project.finite_state_controller:main',
        ],
    },
)
