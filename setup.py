from setuptools import setup, find_packages

setup(
	name = "idea-collection", 
	version = "0.1.0", 
        #url = "TBD",
	license = "public domain", 
	description = "An idea collection tool for django", 
	author = "Jui Dai, Jennifer Ehlers, David Kennedy, Shashank Khandelwal, CM Lubinski", 
	packages = find_packages('src'), 
	package_dir = {'':'src'}, 
	install_requires = ['setuptools'], 
)

