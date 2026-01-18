import os

from SetupCMake import CMakeConfiguration as CMakeRequirements
from SetupVulkan import VulkanConfiguration as VulkanRequirements

os.chdir('./../') # Change from scripts directory to root

print("Checking CMake...")
cmakeInstalled = CMakeRequirements.Validate()
print("\nChecking Vulkan SDK...")
vulkanInstalled = VulkanRequirements.Validate()

if (cmakeInstalled and vulkanInstalled):
	print("\nSetup completed!")
else:
	print("\nSetup was not completed")
