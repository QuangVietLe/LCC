# LCC
All the results and programming related to our research paper, "Observations on circuits in a variant of the Collatz Graph".

The Trivial Files details the cycles that are generated from applying g to a however many times, then applying the original collatz function to it until it reaches back to a, for a = 1,2,8, or 16.
The Nontrivial File details the cycles found by systematically going through many possible tuples and manually checking if they satisfy the LCF or not, which does not includes trivial tuples.
KnownNumbers contains all numbers found in cycles from trivial files and nontrivial file.
GoodTuples File contains all the satisfying tuples to the LCF.
TuplesTested File contains all the tuples tested in the file.

Collatz_Tester File includes the code we used to find trivial and non-trivial tuples.
Exhaustive_Algorithm File includes the exhaustive algorithm that we used to systematically find satisfying tuples.

NOTE: Although the files GoodTuples and TuplesTested have repeats, this does not affect any of the data that we presented in the paper.

Only the previous files are used in Section 3.1 of our paper to analyse the KnownNumbers file. 
Only the following file was used in Section 3.2 of our paper for analysing the tuple lengths.

TuplesToSize9 File contains all the tuples found by the exhaustive algorithm, including any trivial tuples found.
