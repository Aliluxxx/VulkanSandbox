#include "Core/Renderer/Context.h"

namespace sb {

	Context::Context(const ContextSpecification& spec)
		: m_Specification(spec)
	{}

	void Context::Init() {

		SB_TRACE("Context initialization");

		// Vulkan instance

		VkApplicationInfo appInfo{};
		appInfo.sType = VK_STRUCTURE_TYPE_APPLICATION_INFO;
		appInfo.pApplicationName = m_Specification.AppName.c_str();
		appInfo.applicationVersion = VK_MAKE_VERSION(1, 0, 0);
		appInfo.pEngineName = m_Specification.EngineName.c_str();
		appInfo.engineVersion = VK_MAKE_VERSION(1, 0, 0);
		appInfo.apiVersion = VK_API_VERSION_1_3;
		m_Instance.Init(appInfo, m_Specification.EnableDebug);

		// Vulkan debugger
		if (m_Specification.EnableDebug)
			m_Debugger.Init(&m_Instance);
	}

	void Context::Destroy() {

		SB_TRACE("Context deinitialization");

		if (m_Specification.EnableDebug)
			m_Debugger.Destroy();
		m_Instance.Destroy();
	}

	void Context::BeginFrame() {


	}

	void Context::EndFrame() {


	}

	Ref<Context> Context::Create(const ContextSpecification& spec) {

		return CreateRef<Context>(spec);
	}
}
