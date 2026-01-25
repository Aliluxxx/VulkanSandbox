#include "VulkanDebuggerCallback.h"

#include "VulkanDebugger.h"

namespace sb {

	VulkanDebugger::VulkanDebugger()
		: m_Instance(nullptr), m_VkDebugMessenger(VK_NULL_HANDLE)

	{}

	void VulkanDebugger::Init(VulkanInstance* instance) {

		m_Instance = instance;
		VkDebugUtilsMessengerCreateInfoEXT createInfo;
		SetupDebugMessengerCreateInfo(createInfo);

		auto func = (PFN_vkCreateDebugUtilsMessengerEXT)vkGetInstanceProcAddr(m_Instance->GetHandle(), "vkCreateDebugUtilsMessengerEXT");
		if (func != nullptr)
			if (func(m_Instance->GetHandle(), &createInfo, nullptr, &m_VkDebugMessenger) != VK_SUCCESS)
				SB_ASSERT(false, "Failed to create the vulkan debugger");
	}

	void VulkanDebugger::Destroy() {

		auto func = (PFN_vkDestroyDebugUtilsMessengerEXT)vkGetInstanceProcAddr(m_Instance->GetHandle(), "vkDestroyDebugUtilsMessengerEXT");
		if (func != nullptr)
			func(m_Instance->GetHandle(), m_VkDebugMessenger, nullptr);
	}

	void VulkanDebugger::SetupDebugMessengerCreateInfo(VkDebugUtilsMessengerCreateInfoEXT& create_info) {

		create_info = {};
		create_info.sType = VK_STRUCTURE_TYPE_DEBUG_UTILS_MESSENGER_CREATE_INFO_EXT;
		create_info.messageSeverity = VK_DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT | VK_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT | VK_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT;
		create_info.messageType = VK_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT | VK_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT | VK_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT;
		create_info.pfnUserCallback = VulkanDebugCallback;
		create_info.pUserData = nullptr; // Optional
	}
}
