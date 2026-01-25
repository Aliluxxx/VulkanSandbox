#include "VulkanLayerAndExtension.h"

namespace sb {

	std::vector<const char*> VulkanLayerAndExtension::m_ValidationLayers = { "VK_LAYER_KHRONOS_validation" };
	std::vector<const char*> VulkanLayerAndExtension::m_DeviceExtensions = { VK_KHR_SWAPCHAIN_EXTENSION_NAME };

	std::vector<const char*> VulkanLayerAndExtension::GetRequiredExtensions() {

		std::vector<const char*> extensions;

#if defined(SB_PLATFORM_WINDOWS)

		Uint32 glfwExtensionCount = 0;
		const char** glfwExtensions;
		glfwExtensions = glfwGetRequiredInstanceExtensions(&glfwExtensionCount);
		extensions.reserve(glfwExtensionCount);
		for (Uint32 i = 0; i < glfwExtensionCount; i++)
			extensions.push_back(glfwExtensions[i]);

#else

		Uint32 glfwExtensionCount = 0;
		const char** glfwExtensions;
		glfwExtensions = glfwGetRequiredInstanceExtensions(&glfwExtensionCount);
		extensions.reserve(glfwExtensionCount);
		for (Uint32 i = 0; i < glfwExtensionCount; i++)
			extensions.push_back(glfwExtensions[i]);

#endif

		return extensions;
	}

	bool VulkanLayerAndExtension::CheckLayerSupport(const char* requested_layer) {

		Uint32 layerCount = 0;
		vkEnumerateInstanceLayerProperties(&layerCount, nullptr);

		std::vector<VkLayerProperties> availableLayers(layerCount);
		vkEnumerateInstanceLayerProperties(&layerCount, availableLayers.data());

		bool layerFound = false;
		for (const auto& layerProp : availableLayers) {

			if (strcmp(requested_layer, layerProp.layerName) == 0) {

				layerFound = true;
				break;
			}
		}

		if (!layerFound)
			return false;

		return true;
	}

	bool VulkanLayerAndExtension::CheckDeviceExtensionSupport(VkPhysicalDevice device) {

		Uint32 extensionCount;
		vkEnumerateDeviceExtensionProperties(device, nullptr, &extensionCount, nullptr);

		std::vector<VkExtensionProperties> availableExtensions(extensionCount);
		vkEnumerateDeviceExtensionProperties(device, nullptr, &extensionCount, availableExtensions.data());

		std::set<std::string> requiredExtensions(m_DeviceExtensions.begin(), m_DeviceExtensions.end());

		for (const auto& extension : availableExtensions)
			requiredExtensions.erase(extension.extensionName);

		return requiredExtensions.empty();
	}
}
