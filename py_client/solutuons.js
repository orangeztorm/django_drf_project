// given an array of integer,
// display the closet value to zero
// incase th values are found , then display the positive one

const solution = (arr) => {
    let closest = arr[0];
    for (let i = 0; i < arr.length; i++) {
        if (Math.abs(arr[i]) < Math.abs(closest)) {
        closest = arr[i];
        }
    }
    return closest;
    }

    console.log(solution([8, 5, 10, -100, -5, -99, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));
    // console.log(solution([0,-1, -1.0])) => 1