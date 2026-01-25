#include "spdlog/sinks/stdout_color_sinks.h"

#include "Core/Renderer/VulkanDebuggerCallback.h"

namespace sb {

	std::shared_ptr<spdlog::logger> Log::s_CoreLogger;
	std::shared_ptr<spdlog::logger> Log::s_ClientLogger;
	std::shared_ptr<spdlog::logger> Log::s_VulkanLogger;

	void Log::Init() {

		s_CoreLogger = spdlog::stdout_color_mt("CORE");
		s_CoreLogger->set_pattern("[%T.%e][%n][%s:%#][%^%l%$]: %v");
		s_CoreLogger->set_level(spdlog::level::trace);

		s_ClientLogger = spdlog::stdout_color_mt("APP");
		s_ClientLogger->set_pattern("[%T.%e][%s:%#][%^%l%$]: %v");
		s_ClientLogger->set_level(spdlog::level::trace);

		s_VulkanLogger = spdlog::stdout_color_mt("VULKAN");
		s_VulkanLogger->set_pattern("[%T.%e][%n][%^%l%$]: %v");
		s_VulkanLogger->set_level(spdlog::level::warn);
	}

	VKAPI_ATTR VkBool32 VKAPI_CALL VulkanDebugCallback(
		VkDebugUtilsMessageSeverityFlagBitsEXT message_severity,
		VkDebugUtilsMessageTypeFlagsEXT message_type,
		const VkDebugUtilsMessengerCallbackDataEXT* pCallbackData,
		void* pUserData)

	{

		std::string type;
		switch (message_type) {

			case VK_DEBUG_UTILS_MESSAGE_TYPE_GENERAL_BIT_EXT:
				type = "GENERAL_BIT_EXT";
				break;
			case VK_DEBUG_UTILS_MESSAGE_TYPE_VALIDATION_BIT_EXT:
				type = "VALIDATION_BIT_EXT";
				break;
			case VK_DEBUG_UTILS_MESSAGE_TYPE_PERFORMANCE_BIT_EXT:
				type = "PERFORMANCE_BIT_EXT";
				break;
			case VK_DEBUG_UTILS_MESSAGE_TYPE_DEVICE_ADDRESS_BINDING_BIT_EXT:
				type = "DEVICE_ADDRESS_BINDING_BIT_EXT";
				break;
		}

		switch (message_severity) {

			case VK_DEBUG_UTILS_MESSAGE_SEVERITY_VERBOSE_BIT_EXT:
				sb::Log::GetVulkanLogger()->trace("({0} | {1}) {2}", type, pCallbackData->pMessageIdName, pCallbackData->pMessage);
				break;
			case VK_DEBUG_UTILS_MESSAGE_SEVERITY_INFO_BIT_EXT:
				sb::Log::GetVulkanLogger()->info("({0} | {1}) {2}", type, pCallbackData->pMessageIdName, pCallbackData->pMessage);
				break;
			case VK_DEBUG_UTILS_MESSAGE_SEVERITY_WARNING_BIT_EXT:
				sb::Log::GetVulkanLogger()->warn("({0} | {1}) {2}", type, pCallbackData->pMessageIdName, pCallbackData->pMessage);
				break;
			case VK_DEBUG_UTILS_MESSAGE_SEVERITY_ERROR_BIT_EXT:
				sb::Log::GetVulkanLogger()->error("({0} | {1}) {2}", type, pCallbackData->pMessageIdName, pCallbackData->pMessage);
				break;
		}

		return VK_FALSE;
	}
}
