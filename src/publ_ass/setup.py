from setuptools import find_packages, setup

package_name = 'publ_ass'

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
    maintainer='vitor',
    maintainer_email='vitormoraeslages@gmail.com',
    description='Exemplo de um publicador e um assinante',
    license='Apache License 2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'talker = publ_ass.codigo_publicador:main',
            'listener = publ_ass.codigo_assinante:main',
        ],
    },
)
