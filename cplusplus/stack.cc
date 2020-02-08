#include <iostream>

using namespace std;

struct rc {unsigned int row, column;};

class Stack {
  public:
    Stack(const size_t sz);
    bool isEmpty() const {return _top < 0;}
    void push(const rc &row_col);
    void push(const unsigned int row, const unsigned int col);
    void pop(rc &row_col);
    void pop(unsigned int &row, unsigned int &col);
    rc &tos() const;

  private:
    rc *_stk;
    const size_t _size;
    int _top;
};

Stack::Stack(const size_t sz) : _size(sz)
{
  _top = -1;
  _stk = new rc[sz];
}

void Stack::push(const rc &row_col)
{
  // should handle _top >= _size
  _stk[++_top] = row_col;
}

void Stack::push(const unsigned int row, const unsigned int col)
{
  // should handle _top >= _size
  _stk[++_top].row = row;
  _stk[  _top].col = col;
}

void Stack::pop(rc &row_col)
{
  // should handle _top < 0
  row_col = _stk[_top--];
}

void Stack::pop(unsigned int &row, unsigned int &col)
{
  // should handle _top < 0
  row = _stk[_top  ].row;
  col = _stk[_top--].col;
}

rc &Stack::tos() const
{
  // should handle _top < 0
  return _stk[_top];
}
