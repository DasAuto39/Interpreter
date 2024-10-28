#include <iostream>
#include <cmath> // Untuk fungsi atan

int main() {
    /*
    // Deklarasi variabel dengan tipe long double
    long double iC, iL, iR;
    
    int x; // Variabel untuk loop
    
    // Input nilai x
    std::cout << "Masukkan nilai x: ";
    std::cin >> x;
    for(;x > 0; --x)
    {

    
    // Input nilai i1, i2, dan i3
    std::cout << "Masukkan nilai i1: ";
    std::cin >> iC;
    std::cout << "Masukkan nilai i2: ";
    std::cin >> iL;
    std::cout << "Masukkan nilai i3: ";
    std::cin >> iR;
    
    // Menghitung arctan((i1 - i2) / i3) dengan tipe long double
    long double result = atanl((iC - iL) / iR);
    
    long double result_degrees = result * (180.0 / M_PI);
    // Menampilkan hasil
    std::cout << "Hasil arctan((ic - il) / ir) adalah: " << result_degrees << std::endl;
    }
    return 0;
    */
   long double xr,xc,xl;
   std::cout<< "Masukkan nilai xr xc,xl"<<std::endl;
   std::cin>> xr;
   std::cin>> xc;
   std::cin>> xl;
   long double p2w = xl - xc;
   long double result = sqrt(xr*xr + (p2w*p2w));
    std::cout << result;



}
