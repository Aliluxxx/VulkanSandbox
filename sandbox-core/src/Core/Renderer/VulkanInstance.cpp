#include "VulkanLayerAndExtension.h"
#include "VulkanDebugger.h"

#include "VulkanInstance.h"

namespace sb {

	VulkanInstance::VulkanInstance()
		: m_VkInstance(VK_NULL_HANDLE)

	{}

	void VulkanInstance::Init(VkApplicationInfo app_info, const bool enable_validation) {

		if (enable_validation && !CheckValidationLayerSupport())
			SB_ASSERT(false, "Validation layer requested, but not available");

		VkInstanceCreateInfo createInfo{};
		createInfo.sType = VK_STRUCTURE_TYPE_INSTANCE_CREATE_INFO;
		createInfo.pApplicationInfo = &app_info;

		std::vector<const char*> requiredExtensions = VulkanLayerAndExtension::GetRequiredExtensions();
		//requiredExtensions.push_back(VK_KHR_PORTABILITY_ENUMERATION_EXTENSION_NAME);

		if (enable_validation)
			requiredExtensions.push_back(VK_EXT_DEBUG_UTILS_EXTENSION_NAME);

		//createInfo.flags |= VK_INSTANCE_CREATE_ENUMERATE_PORTABILITY_BIT_KHR;

		createInfo.enabledExtensionCount = (Uint32)requiredExtensions.size();
		createInfo.ppEnabledExtensionNames = requiredExtensions.data();

		VkDebugUtilsMessengerCreateInfoEXT debugCreateInfo{};
		if (enable_validation) {

			createInfo.enabledLayerCount = (Uint32)VulkanLayerAndExtension::GetValidationLayers().size();
			createInfo.ppEnabledLayerNames = VulkanLayerAndExtension::GetValidationLayers().data();

			VulkanDebugger::SetupDebugMessengerCreateInfo(debugCreateInfo);
			createInfo.pNext = (VkDebugUtilsMessengerCreateInfoEXT*)&debugCreateInfo;
		}

		else {

			createInfo.enabledLayerCount = 0;
			createInfo.pNext = nullptr;
		}

		if (vkCreateInstance(&createInfo, nullptr, &m_VkInstance) != VK_SUCCESS)
			SB_ASSERT(false, "Failed to create the vulkan instance");
	}

	void VulkanInstance::Destroy() {

		vkDestroyInstance(m_VkInstance, nullptr);
	}

	bool VulkanInstance::CheckValidationLayerSupport() {

		for (const auto& layer : VulkanLayerAndExtension::GetValidationLayers())
			if (!VulkanLayerAndExtension::CheckLayerSupport(layer))
				return false;

		return true;
	}
}
