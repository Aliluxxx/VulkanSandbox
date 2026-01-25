#include <Core.h>

int main() {

	sb::Timer timer;
	Test();
	SB_INFO("Closed after {0}s", timer.GetElapsedTime().AsSeconds());

	return 0;
}
