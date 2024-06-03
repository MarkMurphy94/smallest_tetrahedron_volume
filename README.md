# Smallest Tetrahedron Volume:

A script that reads a list of points on a 3D plane from a file, and identifies the indices of four points that form a 'valid' tetrahedron with the smallest possible volume.
Each point is defined by its coordinates and an associated number, and is presented in the following format: (x, y, z, n), where x, y, and z are floats, and n is an integer ranging from 0 to 100

In this exercise, A'valid' tetrahedron had to be formed with points such that the sum of their n values is equal to 100.

## Example:

Suppose you the following points:

```
[(3.00, 4.00, 5.00, 22), 

(2.00, 3.00, 3.00, 3), 

(1.00, 2.00, 2.00, 4), 

(3.50, 4.50, 5.50, 14), 

(2.50, 3.50, 3.50, 24), 

(6.70, 32.20, 93.0, 5), 

(2.50, 3.00, 7.00, 40)]
```

A tetrahedron formed by the points with indices 0, 3, 4, 6 is the only valid tetrahedron in this example; because 22 + 14 + 24 + 40 = 100

The output is a list of the zero-based indices of these four points in ascending order.
