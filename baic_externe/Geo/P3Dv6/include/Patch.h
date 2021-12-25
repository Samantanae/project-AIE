#ifndef PATCH_H
#define PATCH_H
#include "P3D.h"


template<typename T>
bool In(const T&valeur,const std::vector<T>& data)
{
    for(T i:data)
    {
        if(i==valeur)
            return true;
    }
    return false;
}


class Patch
{
    public:
        /** Default constructor */
        Patch(const P3D& Ci,const P3D& Cf,const std::vector<P3D>&Data,const std::vector<int>&Floor,const std::vector<int>&not_Floor);
        Patch(const P3D& Ci,const P3D& Cf,const std::vector<P3D>&Data,const std::vector<int>&not_Floor);
        /** Default destructor */
        virtual ~Patch();

    protected:
        std::vector<P3D> data;
        P3D ci;
        P3D cf;
        std::vector<int> floor;
        std::vector<int> not_floor;
        std::vector<P3D> l;
        std::vector<std::vector<P3D>> t;


    private:

};

#endif // PATCH_H
