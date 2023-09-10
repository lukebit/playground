// Your First C++ Program

#include <iostream>


long long add_up_to(long n)
{
    long long s = 0;
    for (long long i=1; i <= n; i++)
    {
        s = s + i;
    }

    return s;
}

int main() {
    std::cout << add_up_to(9223372036854775L) << std::endl;
    return 0;
}
