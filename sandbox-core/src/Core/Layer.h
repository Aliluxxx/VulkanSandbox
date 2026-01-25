#pragma once

#include "Core/Base.h"
#include "Core/Time.h"

namespace sb {

	class Layer {

	public:

		Layer(const std::string& debug_name = "Layer");
		virtual ~Layer();

		virtual void OnAttach() {}
		virtual void OnDetach() {}
		virtual void OnUpdate(Time ts) {}

#ifndef SB_DIST
		inline const std::string& GetName() const {

			return m_DebugName;
		}
#else
		inline std::string GetName() const {

			return "";
		}
#endif

	protected:

#ifndef SB_DIST
		std::string m_DebugName;
#endif
	};
}
