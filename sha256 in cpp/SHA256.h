#ifndef SHA256_H
#define SHA256_H

#include <iostream>
#include "functions.h"
class SHA256{

    public:
        SHA256(){
            std::cout << K[0][0] << std::endl;
            Converter conv(2);
        }

    private:
        int K[64][32]{
            {{0}}
        };

};

#endif