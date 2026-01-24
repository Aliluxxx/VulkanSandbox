import os
import subprocess

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

		import inquirer
		from SetupCMake import CMakeConfiguration as CMakeRequirements
		from SetupVulkan import VulkanConfiguration as VulkanRequirements
		os.chdir('./../') # Change from scripts directory to root

		print("\nChecking CMake...")
		if (not CMakeRequirements.Validate()):
			raise Exception("CMakeException")
		print("\nChecking Vulkan SDK...")
		if (not VulkanRequirements.Validate()):
			raise Exception("VulkanException")

		print("\nRunning CMake...")
		(system, arch) = Utils.GetPlatform()

		if system == "Windows":
			generators = [
				("Visual Studio 2022", "Visual Studio 17 2022", "vs2022"),
				("Visual Studio 2019", "Visual Studio 16 2019", "vs2019"),
				("Visual Studio 2017", "Visual Studio 15 2017", "vs2017"),
				("Visual Studio 2015", "Visual Studio 14 2015", "vs2015"),
				("Ninja", "Ninja", "ninja"),
				("Makefile (MinGW)", "MinGW Makefiles", "make")
			]
		elif system == "MacOSX":
			generators = [
				("Xcode", "Xcode", "xcode"),
				("Ninja", "Ninja", "ninja"),
				("Unix Makefiles", "Unix Makefiles", "make")
			]
		else:
			generators = [
				("Ninja", "Ninja", "ninja"),
				("Unix Makefiles", "Unix Makefiles", "make"),
				("CodeLite", "CodeLite - Unix Makefiles", "codelite")
			]

		choices = [label for label, _, _ in generators]

		question = [
			inquirer.List(
				"generator",
				message="Choose a build system:",
				choices=choices,
				carousel=True
			)
		]

		answer = inquirer.prompt(question)
		selected_label = answer["generator"]

		final_dir = ""
		for label, generator, dir in generators:
			if label == selected_label:
				selected_generator = generator
				final_dir = dir
				break

		cmd = ["cmake", "-B", "build/" + final_dir, "-G", selected_generator]
		subprocess.run(cmd, check=True)
	except Exception as e:
		print(type(e).__name__ + ":", e)
		print("\nSetup was not completed")
	else:
		print("\nSetup completed!")
