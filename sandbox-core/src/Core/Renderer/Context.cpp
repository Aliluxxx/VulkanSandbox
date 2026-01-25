#include "Core/Renderer/Context.h"

namespace sb {

	void Context::BeginFrame() {


	}

	void Context::EndFrame() {


	}

	Ref<Context> Context::Create(const ContextSpecification& spec) {

		return CreateRef<Context>();
	}
}
