import os

from SetupPython import PythonConfiguration as PythonRequirements
import Utils

platform = Utils.GetPlatform()
if platform == "Unknown":
	print("Platform not supported or unknown")
else:
	print(f"Detected platform: {platform[0]}-{platform[1]}\n")
	try:
		print("Checking Python...")
		if (not PythonRequirements.Validate()):
			raise Exception("PythonException")
		
		from SetupCMake import CMakeConfiguration as CMakeRequirements
		from SetupVulkan import VulkanConfiguration as VulkanRequirements
		os.chdir('./../') # Change from scripts directory to root

		print("\nChecking CMake...")
		if (not CMakeRequirements.Validate()):
			raise Exception("CMakeException")
		print("\nChecking Vulkan SDK...")
		if (not VulkanRequirements.Validate()):
			raise Exception("VulkanException")
	except:
		print("\nSetup was not completed")
	else:
		print("\nSetup completed!")
