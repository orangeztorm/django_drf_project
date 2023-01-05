// given an array of integer,
// display the closet value to zero
// incase th values are found , then display the positive one
// in best time and space complexity

function solution(A) {
    // write your code in JavaScript (Node.js 8.9.4)
    let min = A[0];
    for (let i = 0; i < A.length; i++) {
        if (Math.abs(A[i]) < Math.abs(min)) {
        min = A[i];
        } else if (Math.abs(A[i]) === Math.abs(min)) {
        min = Math.abs(A[i]);
        }
    }
    return min;
    }
    