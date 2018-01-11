/*
Design a cash register drawer function checkCashRegister() that accepts 
purchase price as the first argument (price), payment as the second 
argument (cash), and cash-in-drawer (cid) as the third argument.

cid is a 2D array listing available currency.

Return the string "Insufficient Funds" if cash-in-drawer is less than 
the change due. Return the string "Closed" if cash-in-drawer is equal 
to the change due.

Otherwise, return change in coin and bills, sorted in highest to lowest order.

!!! HINTS !!!

Hint: 1
It is easier to handle if you have to close the register, or if you 
know how much money is in your register beforehand and you will not 
have enough money to complete the transaction. For this it is 
recommended to have a function to assign this information to 
a variable.

Hint: 2
Life is easier when you get to know the value of each currency type 
in the register instead of how much money is composed of that 
particular currency. So be sure to watch out for that.
try to solve the problem now

Hint: 3
You will have to get as much change from one type before moving to 
the next from greater value to lesser, and keep going until you have 
covered the whole change.
*/

function checkCashRegister(price, cash, cid) {
  let change = [];
  let changeDue = cash - price;
  let status = "open";
  changeDue = Number(changeDue.toFixed(2));
  let monies = [];
  let totalCid;
  
  const values = new Object();
    values.PENNY = 0.01;
    values.NICKEL = 0.05;
    values.DIME = 0.10;
    values.QUARTER = 0.25;
    values.ONE = 1.00;
    values.FIVE = 5.00;
    values.TEN = 10.00;
    values.TWENTY = 20.00;
    values.HUNDRED = 100.00;
  
  // Push the values in 'cid' into the array 'monies'
  for (var i = 0; i < cid.length; i++) {
    monies.push(cid[i][1]);
  }
  
  // Turn 'monies' into an array with the amount of coins/dollars on hand
  for (var i = 0; i < monies.length; i++) {
    var valArr = Object.values(values);
    monies[i] = Math.round(monies[i] / valArr[i]);
  }
  
  // Subtract the coins/dollars from the "drawer" and the value from 'changeDue'
  function subCid(item, value) {
   if (monies[item] >= 1) {
    monies[item] = monies[item] - 1;
    changeDue = changeDue - value;
    changeDue = Number(changeDue.toFixed(2));
    change.push([item, value]);
   } else {
     switch (item) {
        case 8: 
          subCid(7,20);
          break;
        case 7:
          subCid(6,10);
          break;
        case 6:
          subCid(5,5);
          break;
        case 5:
          subCid(4,1);
          break;
        case 4:
          subCid(3,0.25);
          break;
        case 3:
          subCid(2,0.10);
          break;
        case 2:
          subCid(1,0.05);
          break;
        case 1:
          subCid(0,0.01);
          break;
        case 0:
          status = "Insufficient Funds";
          break;
        default:
          status = "Insufficient Funds";
          break;
     }
   }
 }
  
  // While register is open and change is due...
  while (status == "open" && changeDue > 0) {
      if (changeDue >= 100) {
        subCid(8, 100);
      } else if (changeDue >= 20) {
        subCid(7, 20);
      } else if (changeDue >= 10) {
        subCid(6, 10);
      } else if (changeDue >= 5) {
        subCid(5, 5);
      } else if (changeDue >= 1) {
        subCid(4, 1); 
      } else if (changeDue >= 0.25) {
        subCid(3, 0.25);
      } else if (changeDue >= 0.10) {
        subCid(2, 0.10);
      } else if (changeDue >= 0.05) {
        subCid(1, 0.05);
      } else if (changeDue >= 0.01) {
        subCid(0, 0.01);
      }
    }

  // If register still open there must be change to give...
  if (status == "open") {
    let result = new Object();
      result.PENNY = 0;
      result.NICKEL = 0;
      result.DIME = 0;
      result.QUARTER = 0;
      result.ONE = 0;
      result.FIVE = 0;
      result.TEN = 0;
      result.TWENTY = 0;
      result.HUNDRED = 0;      
    
    for (var i = 0; i < change.length; i++) {
      switch (change[i][0]) {
        case 0: 
          result.PENNY = result.PENNY + change[i][1];
          break;
        case 1:
          result.NICKEL = result.NICKEL + change[i][1];
          break;
        case 2: 
          result.DIME = result.DIME + change[i][1];
          break;
        case 3: 
          result.QUARTER = result.QUARTER + change[i][1];
          break;
        case 4: 
          result.ONE = result.ONE + change[i][1];
          break;  
        case 5: 
          result.FIVE = result.FIVE + change[i][1];
          break;
        case 6: 
          result.TEN = result.TEN + change[i][1];
          break;
        case 7: 
          result.TWENTY = result.TWENTY + change[i][1];
          break;
        case 8: 
          result.HUNDRED = result.HUNDRED + change[i][1];
          break;
      }
    }
    
    change = Object.entries(result);
    
    for (var i = 8; i >= 0; i--) {
      if (change[i][1] == 0) {
        change.splice(i,1);
      }
    }
  
    if (monies.reduce((a,b) => a + b) != 0) {
      return change.reverse();
    } else if (monies.reduce((a,b) => a + b) == 0) {
      return "Closed";
    } else {
      return status;
    }
  }
  return status;
}

// Example cash-in-drawer array:
// [["PENNY", 1.01],
// ["NICKEL", 2.05],
// ["DIME", 3.10],
// ["QUARTER", 4.25],
// ["ONE", 90.00],
// ["FIVE", 55.00],
// ["TEN", 20.00],
// ["TWENTY", 60.00],
// ["ONE HUNDRED", 100.00]]

//console.log(checkCashRegister(19.50, 20.02, [["PENNY", 1.05], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25], ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00], ["ONE HUNDRED", 100.00]]));
//console.log("Should return an array");

//console.log(checkCashRegister(19.50, 20.00, [["PENNY", 0.01], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
//console.log("Should return a string");

//console.log(checkCashRegister(19.50, 20.00, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25], ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00], ["ONE HUNDRED", 100.00]]));
// looking for ['QUARTER', 0.50] here

//console.log(checkCashRegister(19.50, 20.00, [["PENNY", 0.50], ["NICKEL", 0], ["DIME", 0], ["QUARTER", 0], ["ONE", 0], ["FIVE", 0], ["TEN", 0], ["TWENTY", 0], ["ONE HUNDRED", 0]]));
// should return "Closed".

console.log(checkCashRegister(3.26, 100.00, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25], ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00], ["ONE HUNDRED", 100.00]]));
// should return [["TWENTY", 60.00], ["TEN", 20.00], ["FIVE", 15.00], ["ONE", 1.00], ["QUARTER", 0.50], ["DIME", 0.20], ["PENNY", 0.04]]
// this one is about the order they're returned in