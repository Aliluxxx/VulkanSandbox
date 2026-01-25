#include "Core/Renderer/Context.h"

namespace sb {

	Context::Context(const ContextSpecification& spec)
		: m_Specification(spec)
	{}

	void Context::Init() {

		SB_TRACE("Context initialization");
	}

	void Context::Destroy() {

		SB_TRACE("Context deinitialization");
	}

	void Context::BeginFrame() {


	}

	void Context::EndFrame() {


	}

	Ref<Context> Context::Create(const ContextSpecification& spec) {

		return CreateRef<Context>(spec);
	}
}
