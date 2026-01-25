#pragma once

#include "Core/Base/Base.h"
#include "Core/Base/Log.h"
#include "Core/Base/Application.h"

extern sb::Application* sb::CreateApplication(ApplicationCommandLineArgs args);

#ifdef SB_PLATFORM_WINDOWS

int main(int argc, char** argv) {

	sb::Log::Init();

	sb::Application* app = sb::CreateApplication({ argc, argv });
	app->Run();
	delete app;

	return 0;
}

#else

int main() {

	sb::Log::Init();

	sb::Application app = sb::CreateApplication({ 0, nullptr });
	app->Run();
	delete app;

	return 0;
}

#endif
