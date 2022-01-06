#include "P2.h"

P2::P2(const P2&a)
{
    x=a.getx;
    y=a.gety;
    c=a.getc;
    active=a.getactive;
}
std::vector<int>& P2::coordonner()const
{
    std::vector<int> C;
    C.resize(3);
    C.push_back(x);
    C.push_back(y);
    C.push_back(c);
    C.shrink_to_fit();
    std::vector<int>& rC=C;
    return rC;
}
bool& P2::actif() const
{
    bool& cactive = active;
    return cactive;
}
//P2::P2(int [1] &xy){x=xy[0];y=xy[1];c=0;active=true;}
//P2::P2(int [2] &xyc){x=xyc[0];y=xyc[1];c=xyc[2];active=true;}
P2::P2(int x_,int y_,int c_,bool active_)
{
    x = x_;
    y=y_;
    c=c_;
    active=active_;
}
P2::~P2()
{
    //dtor
}
