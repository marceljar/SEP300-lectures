#include <iostream>
#include <thread>
#include <chrono>

void task(const char* name, int sec) {
    std::cout << name << " started\n";
    std::this_thread::sleep_for(std::chrono::seconds(sec));
    std::cout << name << " finished after " 
                      << seconds << " seconds\n";
}

int main() {
    std::thread t1(task, "Task A", 3);
    std::thread t2(task, "Task B", 1);
    std::thread t3(task, "Task C", 4);
    std::thread t4(task, "Task D", 2);

    t1.join();
    t2.join();
    t3.join();
    t4.join();

    return 0;
}
