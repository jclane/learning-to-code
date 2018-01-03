/*
You will be provided with an initial array (the first argument in the destroyer 
function), followed by one or more arguments. Remove all elements from the 
initial array that are of the same value as these arguments.
*/

function destroyer(arr) {
  
  var args = Array.from(arguments).slice(1);
  
  return arr.filter(function(el) { 
    return !args.includes(el);
  });
    
}

console.log(destroyer([3, 5, 1, 2, 2], 2, 3, 5));
