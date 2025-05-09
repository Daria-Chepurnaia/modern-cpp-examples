#include<iostream>

int global_var = 1;
//BSS (Block Started by Symbol)
int uninit_global_var;

int& returnStatic() {
    static int static_var_inside_func = 2;
    return static_var_inside_func;
}

int main() {
    int stack_var = 3;
    int* heap_var_ptr = new int(4);
    std::cout << "Address of global variable: " << &global_var << std::endl;
    std::cout << "Address of uninitialized global variable: " << &uninit_global_var << std::endl;
    std::cout << "Address of static varibale inside a function: " << &returnStatic() << std::endl;
    std::cout << "Address of stack variable: " << &stack_var << std::endl;
    std::cout << "Address of heap variable: " << heap_var_ptr << std::endl;

    delete heap_var_ptr;
}