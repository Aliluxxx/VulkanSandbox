#pragma once

#include "Core/Renderer/Context.h"

namespace sb {

	class Renderer {

	public:

		static void Init(Ref<Context> context);
		static void Shutdown();

		static void Begin();
		static void End();
	};
}
