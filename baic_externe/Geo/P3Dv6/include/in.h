#ifndef IN_H
#define IN_H
#include <vector>
#include "P3D.h"
bool In(const int&valeur,const std::vector<int>& data)
{
    for(int i:data)
    {
        if(i==valeur)
            return true;
    }
    return false;
}
bool In(const P3D&valeur,const std::vector<P3D>& data)
{
    for(P3D i:data)
    {
        if(i==valeur)
            return true;
    }
    return false;
}
class in
{
    public:
        /** Default constructor */
        in();
        /** Default destructor */
        virtual ~in();

    protected:

    private:
};

#endif // IN_H
