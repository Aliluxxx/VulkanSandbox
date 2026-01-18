import os
import platform
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

		if (cls.requiredVulkanVersion not in vulkanSDK):
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

		system = platform.system()
		vulkanDir = cls.vulkanDirectory
		version = cls.installVulkanVersion

		if system == "Windows":
			vulkanInstallURL = f"https://sdk.lunarg.com/sdk/download/{version}/windows/vulkansdk-windows-X64-{version}.exe"
			vulkanPath = os.path.join(vulkanDir, f"vulkansdk-{version}-X64.exe")
		elif system == "Linux":
			vulkanInstallURL = f"https://sdk.lunarg.com/sdk/download/{version}/linux/vulkansdk-linux-x86_64-{version}.tar.xz"
			vulkanPath = os.path.join(vulkanDir, f"vulkansdk-{version}-x86_64.tar.xz")
		elif system == "Darwin":
			vulkanInstallURL = f"https://sdk.lunarg.com/sdk/download/{version}/mac/vulkansdk-macos-{version}.zip"
			vulkanPath = os.path.join(vulkanDir, f"vulkansdk-{version}.zip")
		else:
			print(f"{system} not supported for automatic installation")
			return

		print("Downloading {0:s} to {1:s}".format(vulkanInstallURL, vulkanPath))
		Utils.DownloadFile(vulkanInstallURL, vulkanPath)
		if system == "Windows":
			print("Running Vulkan SDK installer...")
			os.startfile(os.path.abspath(vulkanPath))
		else:
			print(f"Extract the archive manually") # Linux: tar -xzf {vulkanPath} -C {vulkanDir}
		print("Re-run this script after installation!")
		quit()

if __name__ == "__main__":
	VulkanConfiguration.Validate()
