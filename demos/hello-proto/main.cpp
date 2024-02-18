#include <iostream>
#include "demos/hello-proto/hello.pb.h"

using namespace std;

int main(int argc, char **argv)
{
    Hello msg;
    msg.set_name("World");
    cout << "Hello, " << msg.name() << "!" << endl;
    return 0;
}
