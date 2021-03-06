from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in project_system/__init__.py
from project_system import __version__ as version

setup(
	name="project_system",
	version=version,
	description="Project Allocation System",
	author="Pradyot Raina",
	author_email="pradyot.r@it.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
