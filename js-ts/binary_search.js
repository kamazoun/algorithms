function binSearch(arr, k) {
  // if k not in arr: return -1? null
  let min = 0;
  let max = arr.length;
  let i = Math.floor(min + (max - min) / 2);

  while (arr[i] !== k) {
    if (arr[i] < k) {
      min = i;
    } else {
      max = i;
    }
    i = Math.floor(min + (max - min) / 2);
  }

  console.log(i);
}

binSearch([1, 1, 1, 2, 3, 3, 3, 4, 4, 5, 5, 8, 8, 9, 10], 9);
