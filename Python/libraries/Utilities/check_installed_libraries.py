'''
https://www.geeksforgeeks.org/how-to-list-installed-python-packages/

'''


import pkg_resources

installed_packages = pkg_resources.working_set
for package in installed_packages:
	print(f"{package.key},  v : {package.version},   path : {package.location}")
