/*
Compare and update the inventory stored in a 2D array against a second 2D 
array of a fresh delivery. Update the current existing inventory item 
quantities (in arr1). If an item cannot be found, add the new item and 
quantity into the inventory array. The returned inventory array should be 
in alphabetical order by item.
*/

function updateInventory(arr1, arr2) {

  function getSorted(a, b) {
    if (a[1] === b[1]) {
      return 0;
    } else {
      return (a[1] < b[1]) ? -1 : 1;
    }
  }
  
  if (arr1.length > 0) {
    arr1.sort(getSorted);
    arr2.sort(getSorted);
    for (var arr in arr2) {
      for (var i = 0; i < arr1.length; i++) {
        if (arr1[i].indexOf(arr2[arr][1]) > -1) {
          arr1[i][0] += arr2[arr][0];
          break;
        } else if (i == arr2.length - 1) {
          arr1.push(arr2[arr]); 
          break;
        }
      }
    }
  } else {
    for (var i = 0; i < arr2.length; i++) {
      arr1.push(arr2[i]);
    }
  }
  
  arr1.sort(getSorted);

  return arr1;
}

// Example inventory lists
var curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
];

var newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
];


/* This should return 
[[88, "Bowling Ball"], 
  [2, "Dirty Sock"], 
  [3, "Hair Pin"], 
  [3, "Half-Eaten Apple"], 
  [5, "Microphone"], 
  [7, "Toothpaste"]]
*/
//console.log(updateInventory([[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]));
// WORKING


/* This should return
[[67, "Bowling Ball"], 
  [2, "Hair Pin"], 
  [3, "Half-Eaten Apple"], 
  [7, "Toothpaste"]]
*/
//console.log(updateInventory([], [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]));
// WORKING

/* This should return
[[1, "Bowling Ball"],
  [0, "Dirty Sock"], 
  [1, "Hair Pin"], 
  [1, "Half-Eaten Apple"], 
  [0, "Microphone"], 
  [1, "Toothpaste"]]
*/
console.log(updateInventory([[0, "Bowling Ball"], [0, "Dirty Sock"], [0, "Hair Pin"], [0, "Microphone"]], [[1, "Hair Pin"], [1, "Half-Eaten Apple"], [1, "Bowling Ball"], [1, "Toothpaste"]]));
// WORKING