#ifndef ARG_H
#define ARG_H
#include <iostream>
#include <typeinfo>
#include <string>

using namespace std;


template <class T>
class arg{
    public:
        /** Default constructor */
        arg(arg&a)
        {

        }

        arg(T _value_)
        {
            value=_value_;
            try
            {
                _type_= typeid(YourClass).name();
            }
            catch (...)
            {
                try
                {
                    _type_
                }
            }
        }
        arg(T&_value_);
        std::string& getType()const;
        friend operator+(arg&a,const arg&b){}
        friend operator+(arg&a,const auto&b);
        /** Default destructor */
        virtual ~arg();

    protected:
        T& value;
        std::string&_type_;
    private:
};

#endif // ARG_H
