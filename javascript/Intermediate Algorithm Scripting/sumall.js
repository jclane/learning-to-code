// We'll pass you an array of two numbers. Return the sum of those two numbers and all numbers between them.

function sumAll(arr) {  
  var newArr = [];
  var min = Math.min(arr[0],arr[1]);
  var max = Math.max(arr[0],arr[1]);
  
  for (var i = min; i <= max; i++) {
    newArr.push(i);
  }

  var sumOfAllValuesInArray = newArr.reduce(function(previousValue, currentValue) {
    return previousValue + currentValue;
  });
  
  return(sumOfAllValuesInArray);
  
}

console.log(sumAll([1, 4]));
