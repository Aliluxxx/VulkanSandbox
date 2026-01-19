import os
import platform
import subprocess
from pathlib import Path

import Utils

class VulkanConfiguration:
	requiredVulkanVersion = "1.4."
	installVulkanVersion = "1.4.335.0"
	vulkanDirectory = "./vendor"

	@classmethod
	def Validate(cls):
		if (not cls.CheckVulkanSDK()):
			print("Vulkan SDK not installed correctly.")
			return False

		if (not cls.CheckVulkanSDKDebugLibs()):
			print("No Vulkan SDK debug libs found. Install Vulkan SDK with debug libs.")
			print("Debug configuration disabled.")
			return False

		return True

	@classmethod
	def CheckVulkanSDK(cls):
		vulkanSDK = os.environ.get("VULKAN_SDK")
		if (vulkanSDK is None):
			print("You don't have the Vulkan SDK installed!")
			cls.__InstallVulkanSDK()
			return None
		else:
			print(f"Located Vulkan SDK at {vulkanSDK}")

		if (platform.system() != "Linux" and cls.requiredVulkanVersion not in vulkanSDK):
			print(f"You don't have the correct Vulkan SDK version! (Required: {cls.requiredVulkanVersion}*)")
			cls.__InstallVulkanSDK()
			return False

		print(f"Correct Vulkan SDK located at {vulkanSDK}")
		return True

	@classmethod
	def CheckVulkanSDKDebugLibs(cls):
		vulkanSDK = os.environ.get("VULKAN_SDK")
		shadercdLib = Path(f"{vulkanSDK}/Lib/shaderc_sharedd.lib")
		return shadercdLib.exists()

	@classmethod
	def __InstallVulkanSDK(cls):
		permissionGranted = False
		while not permissionGranted:
			reply = str(input("Would you like to install VulkanSDK {0:s}? [Y/N]: ".format(cls.installVulkanVersion))).lower().strip()[:1]
			if reply == 'n' or reply == 'N':
				return
			permissionGranted = (reply == 'y' or reply == 'Y')

		(system, arch) = Utils.GetPlatform()
		vulkanDir = cls.vulkanDirectory
		version = cls.installVulkanVersion

		# Windows
		if system == "Windows":
			if arch == "x86_64":
				vulkanInstallURL = f"https://sdk.lunarg.com/sdk/download/{version}/windows/vulkansdk-windows-X64-{version}.exe"
				vulkanPath = os.path.join(vulkanDir, f"vulkansdk-{version}-x86_64-installer.exe")
			if arch == "arm64":
				vulkanInstallURL = f"https://sdk.lunarg.com/sdk/download/{version}/windows/vulkansdk-windows-ARM64-{version}.exe"
				vulkanPath = os.path.join(vulkanDir, f"vulkansdk-{version}-arm64.exe")
		# Linux
		elif system == "Linux":
			pass
		# MacOSX
		elif system == "MacOSX":
			vulkanInstallURL = f"https://sdk.lunarg.com/sdk/download/{version}/mac/vulkansdk-macos-{version}.zip"
			vulkanPath = os.path.join(vulkanDir, f"vulkansdk-{version}-universal.zip")
		else:
			print(f"{system}-{arch} not supported for automatic installation")
			return

		if system != "Linux":
			print("Downloading {0:s} to {1:s}".format(vulkanInstallURL, vulkanPath))
			Utils.DownloadFile(vulkanInstallURL, vulkanPath)

		if system == "Windows":
			print("Running Vulkan SDK installer...")
			os.startfile(os.path.abspath(vulkanPath))
		if system == "Linux":
			import distro # type: ignore
			if distro.id() in ("ubuntu", "debian", "raspbian", "raspios"):
				print("Running apt to install Vulkan SDK...")
				subprocess.run(["sudo", "apt", "update"], check=True)
				subprocess.run(["sudo", "apt", "install", "-y",
										"vulkan-utils", "libvulkan-dev", "vulkan-validationlayers"], check=True)
			elif distro.id() in ("fedora", "centos", "rhel"):
				print("Running dnf to install Vulkan SDK...")
				subprocess.run(["sudo", "dnf", "install", "-y",
											"vulkan-tools", "vulkan-loader-devel", "vulkan-validation-layers"], check=True)
			elif distro.id() in ("arch", "manjaro"):
				print("Running pacman to install Vulkan SDK...")
				subprocess.run(["sudo", "pacman", "-Sy", "--noconfirm",
												"vulkan-icd-loader", "vulkan-tools", "vulkan-validation-layers"], check=True)
			else:
				print(f"{distro.name()} is not supported for automatic installation")
		elif system == "MacOSX":
			print("Unzipping Vulkan SDK installer...")
			Utils.UnzipFile(vulkanPath)
			vulkanInstaller = os.path.join(vulkanDir, f"vulkansdk-macOS-{version}.app/Contents/MacOS/vulkansdk-macOS-{version}")
			print("Running Vulkan SDK installer...")
			subprocess.run(["chmod", "+x", vulkanInstaller])
			subprocess.run([f"./{vulkanInstaller}"])
		else:
			print("Cannot execute the installation automatically")
			print(f"Execute the installation manually (installer is located at \"{os.path.abspath(vulkanDir)}\")")
		print("Re-run this script after installation!")
		quit()

if __name__ == "__main__":
	VulkanConfiguration.Validate()
