// Compiled with: g++ -Wall -std=c++14 -pthread

#include <iostream>
//#include <array>

using namespace std;

template <typename T>
class SquareGrid
{
  public:
    SquareGrid(const unsigned int dim);
  protected:
    T **_obj;
    const unsigned int _dim;
};

template <typename T>
SquareGrid<T>::SquareGrid(const unsigned int dim) : _dim(dim)
{
  _obj = new T* [dim];
  for (auto i = 0; i < dim; i++)
  {
    _obj[i] = new T[dim];
  }
}



class IntSquareGrid : public SquareGrid<int>
{
  public:
    IntSquareGrid(const unsigned int dim) : SquareGrid(dim) {}
    void initialize();
    void print();
};

void IntSquareGrid::initialize()
{
  for (auto i = 0; i < _dim; i++)
  {
    for (auto j = 0; j < _dim; j++)
    {
      _obj[i][j] = (i + 1) * 100 + j + 1;
    }
  }
}

void IntSquareGrid::print()
{
  for (auto i = 0; i < _dim; i++)
  {
    cout << "[" << i << "][0.." << _dim - 1 << "]: ";
    for (auto j = 0; j < _dim; j++)
    {
      cout << "\t" << _obj[i][j];
    }
    cout << endl;
  }
}


struct pixel {int x,y;};

class PixelGrid : public SquareGrid<pixel>
{
  public:
    PixelGrid(const unsigned int dim) : SquareGrid(dim) {}
    void initialize(const double density);
    void print();
};

/* ======  Traditional C=style below:

void process_square(int **square, const size_t dim)
{
  cout << __func__ << "(*, " << dim << ")" << endl;
  for (auto i = 0; i < dim; i++)
  {
    cout << "[" << i << "][" << dim << "]: ";
    for (auto j = 0; j < dim; j++)
    {
      cout << "\t" << square[i][j];
    }
    cout << endl;
  }
}


void initialize_square(int **square, const size_t dim)
{
  cout << __func__ << "(*, " << dim << ")" << endl;
  for (auto i = 0; i < dim; i++)
  {
    for (auto j = 0; j < dim; j++)
    {
      square[i][j] = (i + 1) * 100 + j + 1;
    }
  }
}


int **allocate_square(const size_t dim)
{
  cout << __func__ << "(" << dim << ")" << endl;
  int **square = new int *[dim];
  for (auto i = 0; i < dim; i++) {
    square[i] = new int[dim];
  }
  return square;
}

===== Tradition C-style above */


int main(const int argc, char *argv[])
{
  size_t dim = 0;

  if (argc > 1) {
    dim = atoi(argv[1]);
  }

  //int **square = allocate_square(dim);
  //initialize_square(square, dim);
  //process_square(square, dim);

  /*
  double density = getDensity();

  PixelGrid bfs(dim);
  bfs.initialize(density);
  bfs.print();

  PixelGrid dfs(dim);
  dfs.initialize(density);
  dfs.print();
  */

  IntSquareGrid square(dim);
  square.initialize();
  square.print();

  return 0;
}
