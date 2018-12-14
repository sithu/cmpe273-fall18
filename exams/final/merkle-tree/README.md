The given merkle tree based data integrity check application can detect differences between two directories. Complete the implemention by filling in all TODOs functions in _merkletree.py_.

You must be these provided directories A and B to find which files are different.

I. Complete the ```def print_tree(self, hash):``` function to print all files under a given directory along with hash value in the front of each node. (15 points)

_Directory structure_

```
A
|-- dir1
|   |-- file11.txt
|   |-- file12.txt
|   |-- file13.txt
|-- dir2
|   |-- file21.txt
|   |-- file22.txt
|   |-- file23.txt
|   `-- file24.txt
|-- file1.txt
|-- file2.txt
|-- file3.txt
`-- file4.txt
```

_Expected Output from print_tree():_

```
5a111c6eb0f1d0052b5420f75c5e4d33 A
    -> d23ca9d5fc333862cc16cfa4775bd728 dir1
    -> f41fba8a445fe47182a474534b3ee47f dir2
    -> cdd60fb7f1b59f3461895fb238c77a0a file1.txt
    -> e4069a89d02170a56e27daaa6ea81859 file2.txt
    -> 78e1885a370bc213414858c648e916fb file3.txt
    -> c97336b6e52347826f8c7b0168049909 file4.txt
d23ca9d5fc333862cc16cfa4775bd728 dir1
    -> 27064003da39a4a8bda08730b06fc7b9 dir1/file11.txt
    -> 61ba29b15e22f3030c0a0ce4e36c00da dir1/file12.txt
    -> bd7b8b855864cf813a5e9ff0f79ab350 dir1/file13.txt
27064003da39a4a8bda08730b06fc7b9 dir1/file11.txt
61ba29b15e22f3030c0a0ce4e36c00da dir1/file12.txt
bd7b8b855864cf813a5e9ff0f79ab350 dir1/file13.txt
f41fba8a445fe47182a474534b3ee47f dir2
    -> c8d661a948cf8dc9a70f9ca75633c34f dir2/file21.txt
    -> 59ee8564e4d1a52c17557f447bb98f40 dir2/file22.txt
    -> dc6d821c596f9cde0967875fa8de90fe dir2/file23.txt
    -> 0c9643339784601bb3f6f43e63d1604b dir2/file24.txt
c8d661a948cf8dc9a70f9ca75633c34f dir2/file21.txt
59ee8564e4d1a52c17557f447bb98f40 dir2/file22.txt
dc6d821c596f9cde0967875fa8de90fe dir2/file23.txt
0c9643339784601bb3f6f43e63d1604b dir2/file24.txt
cdd60fb7f1b59f3461895fb238c77a0a file1.txt
e4069a89d02170a56e27daaa6ea81859 file2.txt
78e1885a370bc213414858c648e916fb file3.txt
c97336b6e52347826f8c7b0168049909 file4.txt
```

II. Complete the ```def find_diff(merkle_tree_a, a_roothash, merkle_tree_b, b_roothash):``` function to find differences between the given two Merkle trees. (15 points)

> Hint: both ```find_diff``` and ```print_tree``` functions require to recursively call its own function to handle child nodes (hash -> dir/file).

_Expected output of correct solution_

> Individual hash value can be different, but the directory diff result must be the same as the below.

```
python3 merkletree.py

Merkle Tree for directory: A
5a111c6eb0f1d0052b5420f75c5e4d33 A
    -> d23ca9d5fc333862cc16cfa4775bd728 dir1
    -> f41fba8a445fe47182a474534b3ee47f dir2
    -> cdd60fb7f1b59f3461895fb238c77a0a file1.txt
    -> e4069a89d02170a56e27daaa6ea81859 file2.txt
    -> 78e1885a370bc213414858c648e916fb file3.txt
    -> c97336b6e52347826f8c7b0168049909 file4.txt
d23ca9d5fc333862cc16cfa4775bd728 dir1
    -> 27064003da39a4a8bda08730b06fc7b9 dir1/file11.txt
    -> 61ba29b15e22f3030c0a0ce4e36c00da dir1/file12.txt
    -> bd7b8b855864cf813a5e9ff0f79ab350 dir1/file13.txt
27064003da39a4a8bda08730b06fc7b9 dir1/file11.txt
61ba29b15e22f3030c0a0ce4e36c00da dir1/file12.txt
bd7b8b855864cf813a5e9ff0f79ab350 dir1/file13.txt
f41fba8a445fe47182a474534b3ee47f dir2
    -> c8d661a948cf8dc9a70f9ca75633c34f dir2/file21.txt
    -> 59ee8564e4d1a52c17557f447bb98f40 dir2/file22.txt
    -> dc6d821c596f9cde0967875fa8de90fe dir2/file23.txt
    -> 0c9643339784601bb3f6f43e63d1604b dir2/file24.txt
c8d661a948cf8dc9a70f9ca75633c34f dir2/file21.txt
59ee8564e4d1a52c17557f447bb98f40 dir2/file22.txt
dc6d821c596f9cde0967875fa8de90fe dir2/file23.txt
0c9643339784601bb3f6f43e63d1604b dir2/file24.txt
cdd60fb7f1b59f3461895fb238c77a0a file1.txt
e4069a89d02170a56e27daaa6ea81859 file2.txt
78e1885a370bc213414858c648e916fb file3.txt
c97336b6e52347826f8c7b0168049909 file4.txt
------------------------------
Merkle Tree for directory: B
13236b34cf89620d54b20b9700681a64 B
    -> d23ca9d5fc333862cc16cfa4775bd728 dir1
    -> c1004e01de99ef195c4dcae30a165930 dir2
    -> cdd60fb7f1b59f3461895fb238c77a0a file1.txt
    -> e4069a89d02170a56e27daaa6ea81859 file2.txt
    -> 78e1885a370bc213414858c648e916fb file3.txt
    -> c97336b6e52347826f8c7b0168049909 file4.txt
d23ca9d5fc333862cc16cfa4775bd728 dir1
    -> 27064003da39a4a8bda08730b06fc7b9 dir1/file11.txt
    -> 61ba29b15e22f3030c0a0ce4e36c00da dir1/file12.txt
    -> bd7b8b855864cf813a5e9ff0f79ab350 dir1/file13.txt
27064003da39a4a8bda08730b06fc7b9 dir1/file11.txt
61ba29b15e22f3030c0a0ce4e36c00da dir1/file12.txt
bd7b8b855864cf813a5e9ff0f79ab350 dir1/file13.txt
c1004e01de99ef195c4dcae30a165930 dir2
    -> c8d661a948cf8dc9a70f9ca75633c34f dir2/file21.txt
    -> 59ee8564e4d1a52c17557f447bb98f40 dir2/file22.txt
    -> dc6d821c596f9cde0967875fa8de90fe dir2/file23.txt
    -> b909a28e6b8f06f84ea051bf0c8acd10 dir2/file24.txt
c8d661a948cf8dc9a70f9ca75633c34f dir2/file21.txt
59ee8564e4d1a52c17557f447bb98f40 dir2/file22.txt
dc6d821c596f9cde0967875fa8de90fe dir2/file23.txt
b909a28e6b8f06f84ea051bf0c8acd10 dir2/file24.txt
cdd60fb7f1b59f3461895fb238c77a0a file1.txt
e4069a89d02170a56e27daaa6ea81859 file2.txt
78e1885a370bc213414858c648e916fb file3.txt
c97336b6e52347826f8c7b0168049909 file4.txt
------------------------------
SAME: dir1
DIFF: dir2
SAME: dir2/file21.txt
SAME: dir2/file22.txt
SAME: dir2/file23.txt
DIFF: dir2/file24.txt
SAME: file1.txt
SAME: file2.txt
SAME: file3.txt
SAME: file4.txt
 ```