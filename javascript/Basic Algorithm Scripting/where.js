/*
Return the lowest index at which a value (second argument) 
should be inserted into an array (first argument) once it 
has been sorted. The returned value should be a number.
*/

function getIndexToIns(arr, num) {
  var index;
  
  arr.push(num);
  arr = arr.sort((a, b) => a - b);
  index = arr.indexOf(num);
  
  return index;
}

console.log(getIndexToIns([2, 5, 10], 15)); 
