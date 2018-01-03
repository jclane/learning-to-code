/*
Make a function that looks through an array of objects (first argument) 
and returns an array of all objects that have matching property and 
value pairs (second argument). Each property and value pair of the source 
object has to be present in the object from the collection if it is to be 
included in the returned array.

For example, if the first argument is [{ first: "Romeo", last: "Montague" }, 
{ first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], 
and the second argument is { last: "Capulet" }, then you must return the 
third object from the array (the first argument), because it contains the 
property and its value, that was passed on as the second argument.
*/

function whatIsInAName(collection, source) {
  let arr = [];
  const sorEnt = Object.entries(source);
  
  for (var i = 0; i < collection.length; i++) {
      if (collection[i].hasOwnProperty(sorEnt[0][0]) && collection[i].hasOwnProperty(sorEnt[0][1])) {
        arr.push(collection[i]);
    }
  }
  
  return arr;
}


// This one has two souces to be returned instead of one
//console.log(whatIsInAName([{ "a": 1, "b": 2 }, { "a": 1 }, { "a": 1, "b": 2, "c": 2 }], { "a": 1, "b": 2 }));
// Should return [{ "a": 1, "b": 2 }, { "a": 1, "b": 2, "c": 2 }]

console.log(whatIsInAName([{ first: "Romeo", last: "Montague" }, { first: "Mercutio", last: null }, { first: "Tybalt", last: "Capulet" }], { last: "Capulet" }));