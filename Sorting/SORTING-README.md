Sorting
=======

Each module contains an implementation of a sorting algorithm indicated by the name of the module. This implementation can be used by calling the function with the same name, and the general signature for this function is as follows:

`<algorithm name>(data, min_val=0, max_val=0)`

* `data` is an array of the integers to sort.
* `min_val` and `max_val` are only required for non-comparative algorithms; this is indicated in the specific scripts. These indicate the minimum and maximum values in data.

Each implementation returns an array of all values in data, but sorted in ascending order.