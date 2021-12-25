#ifndef P3D_H
#define P3D_H
#include <vector>

class P3D
{
    public:
        /** Default constructor */
        P3D(int X=0,int Y = 0, int C = 0);

        bool& in(std::vector<P3D> xy);
        friend bool operator==(P3D &a, const P3D &b);
        /** Default destructor */
        virtual ~P3D();

    protected:
        int x;
        int y;
        int c;
    private:
};

#endif // P3D_H
