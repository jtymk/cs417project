# cs417project

This is a python project for cs417 using the library 
import parse_temps provided by the class instructor.

The project takes data from a text file and stores it 
into 4 separate vectors. 

When running the program it writes the data from the vectors
into separate text files.

The program calculates piecewise linear interpolation and least squares approximation for the first core and writes the results into separate text files. 

# Sample Execution & Output

If run using 

```
python3 interpolation.py

```

The first five examples for linear inerpolation would appear as

```
0  <= x <      30  y_0      =    60.36666666666667 interpolation 
30  <= x <      60  y_0      =    110.6 interpolation 
60  <= x <      90  y_0      =    121.3 interpolation 
90  <= x <      120  y_0      =    173.5 interpolation 
120  <= x <      150  y_0      =    187.53333333333333 interpolation 

```
The first five examples for least squares approximation would appear as

```

f(x) = -0.012474057773125005x + (297.2549088442533)
f(x) = -0.012453062240207254x + (296.88076844765897)
f(x) = -0.012432049448614908x + (296.50632050148334)
f(x) = -0.01241107311337841x + (296.13252220756897)
f(x) = -0.012390044649454571x + (295.75779498044614)

```
