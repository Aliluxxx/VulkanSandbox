#pragma once

#include "Core/Base/Base.h"
#include "Core/Renderer/VulkanInstance.h"

namespace sb {

	class VulkanDebugger {

	public:

		VulkanDebugger();

		void Init(VulkanInstance* instance);
		void Destroy();

		inline const VkDebugUtilsMessengerEXT& GetHandle() const { return m_VkDebugMessenger; }

		static void SetupDebugMessengerCreateInfo(VkDebugUtilsMessengerCreateInfoEXT& create_info);

	private:

		VulkanInstance* m_Instance;
		VkDebugUtilsMessengerEXT m_VkDebugMessenger;
	};
}
