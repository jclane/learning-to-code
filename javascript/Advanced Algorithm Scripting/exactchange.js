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
          subCid(1,0.01);
          break;
        case 1:
          console.log("Insufficient Funds");
          break;
        case 0:
          status = "closed";
          break;
     }
   }
 }
 
  while (changeDue > 0) {
    if (status == "closed") {
      console.log("closed");
      break;
    } else if (changeDue >= 100) {
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
  
  for (var el in change) {
    
  }
  
  for (var i = 0; i < change.length; i++) {
    switch (change[i][0]) {
      case 0: 
        change[i][0] = "PENNY";
        break;
      case 3: 
        change[i][0] = "QUARTER";
        break;
    }
  }
  
  return change;
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

console.log(checkCashRegister(19.50, 20.02, [["PENNY", 0], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25], ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00], ["ONE HUNDRED", 100.00]]));
