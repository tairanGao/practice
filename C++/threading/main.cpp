#include <iostream>
#include <thread>
#include <string>


void function_1(){
    std::cout << " function 1" << std::endl;
}
int class1() {
//    function_1();
    int j = 1;
    std::thread t1(function_1); //t1 starts running
//    t1.join(); // main thread wait for t1 to finish

    t1.detach(); // separate the connection, t1 will run freely --> daemon process
    // nothing got print out since main thread runs faster than t1
    for(int i =0; i<=1000000; i++){
        j =i % 15;
    }
    std::cout << std::to_string(j) << std::endl;
//    t1.join(); //crash program since it's already been detached
    if (t1.joinable()){
        t1.join();
    }

    return 0;
}

class Fctor{
public:
    void operator()(){
        for (int i=0 ;i>-1000; i--){
            std::cout<<"from fctor"<< i <<std::endl;
        }
    }
};

int class2() {
    Fctor fct;
    std::thread t1(fct);

    //approach 1
    try{
        for (int i=0; i<100;i++){
            std::cout<< "from class2: "<< i << std::endl;
        }
    } catch(...){
        t1.join();
        throw;
    }

    //approch 2: RAII
    //Wrapper w(t1);


    return 0;
}

int main(){
    class2();
    return 1;
}