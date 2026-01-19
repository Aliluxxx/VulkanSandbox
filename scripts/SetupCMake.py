import os
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

		(system, arch) = Utils.GetPlatform()
		cmakeDir = cls.cmakeDirectory
		version = cls.installCMakeVersion

		# Windows
		if system == "Windows":
			if arch == "x86_64":
				cmakeInstallURL = f"https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}-windows-x86_64.msi"
				cmakePath = os.path.join(cmakeDir, f"cmake-{version}-x86_64-installer.exe")
			if arch == "x86":
				cmakeInstallURL = f"https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}-windows-i386.msi"
				cmakePath = os.path.join(cmakeDir, f"cmake-{version}-x86-installer.exe")
			if arch == "arm64":
				cmakeInstallURL = f"https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}-windows-arm64.msi"
				cmakePath = os.path.join(cmakeDir, f"cmake-{version}-arm64-installer.exe")
		# Linux
		elif system == "Linux":
			if arch == "x86_64":
				cmakeInstallURL = f"https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}-linux-x86_64.sh"
				cmakePath = os.path.join(cmakeDir, f"cmake-{version}-x86_64-installer.sh")
			if arch == "aarch64":
				cmakeInstallURL = f"https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}-linux-aarch64.sh"
				cmakePath = os.path.join(cmakeDir, f"cmake-{version}-aarch64-installer.sh")
		# MacOSX
		elif system == "MacOSX":
			cmakeInstallURL = f"https://github.com/Kitware/CMake/releases/download/v{version}/cmake-{version}-macos10.10-universal.dmg"
			cmakePath = os.path.join(cmakeDir, f"cmake-{version}-universal-installer.dmg")
		else:
			print(f"{system}-{arch} not supported for automatic installation")
			return

		print("Downloading {0:s} to {1:s}".format(cmakeInstallURL, cmakePath))
		Utils.DownloadFile(cmakeInstallURL, cmakePath)
		if system == "Windows":
			print("Running CMake installer...")
			os.startfile(os.path.abspath(cmakePath))
		elif system == "Linux" or system == "MacOSX":
			print("Running CMake installer...")
			subprocess.run(["chmod", "+x", cmakePath])
			subprocess.run([f"./{cmakePath}"])
		else:
			print("Cannot execute the installation automatically")
			print(f"Execute the installation manually (installer is located at \"{os.path.abspath(cmakeDir)}\")")
		print("Re-run this script after installation!")
