import subprocess
import urllib.request
import os

def install_software(package):
	"""
	Function to install a software package.
	"""
	try:
		if package == 'firefox':
			url = 'https://download.mozilla.org/?product=firefox-latest&os=win64&lang=en-US'
			installer_path = 'firefox_installer.exe'
			urllib.request.urlretrieve(url, installer_path)
			subprocess.check_call([installer_path, '-ms'])
			os.remove(installer_path)
		else:
			subprocess.check_call(['pip', 'install', package])
		print("Successfully installed {package}")
	except subprocess.CalledProcessError:
		print("Failed to install {package}")


software_packages = ['numpy', 'pandas', 'matplotlib', 'firefox']

for package in software_packages:
	if package == "firefox":
		install_software(package)
