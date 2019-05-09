Question: 870 Advantage Shuffle

For this question, we can see that we are given two arrays, and need to find the greatest advantage between the two arrays. We can sort the two arrays first, which has a time complexity of O(nlogn), and we now have two sorted array A_s and B_s.

We set up two iterators, A_t and B_t, and initialize them at index 0. We continue add the iterator A_t, and if the corresponding number in A_s is larger than the corresponding number in B_s by iterator B_t, we set the number in A_s at the former position of B_s in the original B array. If the number in A_s of iterator A_t is smaller, then this number has no value at all, and we need to match this number with the largest remaining number in B_s.