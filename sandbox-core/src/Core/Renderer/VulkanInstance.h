#pragma once

#include <vulkan/vulkan.h>

#include "Core/Base/Base.h"

namespace sb {

	class VulkanInstance {

	public:

		VulkanInstance();

		void Init(VkApplicationInfo app_info, const bool enable_validation);
		void Destroy();
		inline const VkInstance& GetHandle() const { return m_VkInstance; }

	private:

		bool CheckValidationLayerSupport();

		VkInstance m_VkInstance;
	};
}
