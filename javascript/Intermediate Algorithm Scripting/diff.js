/* 
Compare two arrays and return a new array with any items only 
found in one of the two given arrays, but not both. In other 
words, return the symmetric difference of the two arrays.
*/


// THIS DOES NOT WORK

function diff(arr1,arr2) {
  var newArr = [];

  arr1.forEach(function(element) {
   
    if (arr2.indexOf(element) == -1) {
     newArr.push(element);
     console.log(newArr);
    }

  });

  arr2.forEach(function(element) {
   
    if (arr1.indexOf(element) == -1) {
     newArr.push(element);
     console.log(newArr);
    }

  });
 
  return newArr;

}

console.log(diff([1,2,3,5],[1,2,3,4,5]));
