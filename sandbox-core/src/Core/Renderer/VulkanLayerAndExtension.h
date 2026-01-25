#pragma once

#ifdef SB_PRECOMPILED_HEADER
#include <vector>
#include <vulkan/vulkan.h>
#endif

#include "Core/Base/Base.h"

namespace sb {

	class VulkanLayerAndExtension {

	public:

		static std::vector<const char*> GetRequiredExtensions();
		static bool CheckLayerSupport(const char* requested_layer);
		static bool CheckDeviceExtensionSupport(VkPhysicalDevice device);

		inline static const std::vector<const char*>& GetValidationLayers() { return m_ValidationLayers; }
		inline static const std::vector<const char*>& GetDeviceExtensions() { return m_DeviceExtensions; }

	private:

		static std::vector<const char*> m_ValidationLayers;
		static std::vector<const char*> m_DeviceExtensions;
	};
}
