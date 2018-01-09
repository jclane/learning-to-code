/*
Create a function that takes two or more arrays and returns an array of 
the symmetric difference (△ or ⊕) of the provided arrays.

Given two sets (for example set A = {1, 2, 3} and set B = {2, 3, 4}), 
the mathematical term "symmetric difference" of two sets is the set of 
elements which are in either of the two sets, but not in 
both (A △ B = C = {1, 4}). For every additional symmetric difference 
you take (say on a set D = {2, 3}), you should get the set with elements 
which are in either of the two the sets but not 
both (C △ D = {1, 4} △ {2, 3} = {1, 2, 3, 4}).
*/

function sym(args) {
  args = Array.prototype.slice.call(arguments);

  let result = [];
  
  // Reduces 'args' to an 1 deminsional array and counts how many times a 
  // value appears in the new array
  let reduce = args.reduce((a, b) => a.concat(b))
                .reduce(function (allValues, value) {
                  if (value in allValues) {
                    allValues[value]++;
                  } else {
                    allValues[value] = 1;
                  }
                  return allValues;
                }, {});
                
  for (var key in reduce) { 
    if (reduce[key] === 1) {
      result.push(parseInt(key));
    }
  }
                
                
  return result;
}

console.log(sym([1, 2, 3], [5, 2, 1, 4]));
console.log("Should be [3, 4, 5]");

console.log(sym([1, 2, 5], [2, 3, 5], [3, 4, 5]));
console.log("Should be [1, 4, 5]");