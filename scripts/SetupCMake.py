import os
import platform
import subprocess

import Utils

class CMakeConfiguration:
	installCMakeVersion = "4.2.1"
	cmakeDirectory = "./vendor"

	@classmethod
	def Validate(cls):
		if (not cls.CheckIfCMakeInstalled()):
			return False
		return True

	@classmethod
	def CheckIfCMakeInstalled(cls):
		try:
			output = subprocess.check_output(["cmake", "--version"], stderr=subprocess.STDOUT, text=True)
			first, second, version = output.splitlines()[0].split(" ")# Show first line
			print(f"CMake {version} is installed")
			return True
		except FileNotFoundError:
			print("CMake is not installed")
		except subprocess.CalledProcessError:
			print("CMake was found, but could be corrupted")

		cls.__InstallCMake()

		return False

	@classmethod
	def __InstallCMake(cls):
		permissionGranted = False
		while not permissionGranted:
			reply = str(input("Would you like to install CMake {0:s}? [Y/N]: ".format(cls.installCMakeVersion))).lower().strip()[:1]
			if reply == 'n' or reply == 'N':
				return
			permissionGranted = (reply == 'y' or reply == 'Y')

		system = platform.system()
		cmakeDir = cls.cmakeDirectory
		version = cls.installCMakeVersion

		if system == "Windows":
			cmakeInstallURL = f"https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}-windows-x86_64.msi"
			cmakePath = os.path.join(cmakeDir, f"vulkansdk-{version}-Installer.exe")
		elif system == "Linux":
			cmakeInstallURL = f"hhttps://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}-linux-x86_64.sh"
			cmakePath = os.path.join(cmakeDir, f"vulkansdk-{version}-x86_64.tar.xz")
		elif system == "Darwin":
			cmakeInstallURL = f"https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}-macos-universal.dmg"
			cmakePath = os.path.join(cmakeDir, f"vulkansdk-{version}-macos.zip")
		else:
			print(f"{system} not supported for automatic installation")
			return

		print("Downloading {0:s} to {1:s}".format(cmakeInstallURL, cmakePath))
		Utils.DownloadFile(cmakeInstallURL, cmakePath)
		if system == "Windows":
			print("Running Vulkan SDK installer...")
			os.startfile(os.path.abspath(cmakePath))
		else:
			print(f"Extract the archive manually")
		print("Re-run this script after installation!")
