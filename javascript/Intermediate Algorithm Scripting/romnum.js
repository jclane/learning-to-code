// Convert the given number into a roman numeral.

function convert(num) {
  const numerals = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"];
  const numbers = [1000,900,500,400,100,90,50,40,10,9,5,4,1];
  let romNum = '';
  
  // For each element in numbers array
  for (var i in numbers ) {
    // While num is greater than or equal to numbers[i] (ex. 3999 >= 1000 is true)
    while ( num >= numbers[i] ) {
      romNum += numerals[i]; // Add roman numeral to romNum
      num -= numbers[i];  // Subtract numbers[i] from num (ex. 3999 - 1000)
    }
  }
  
  return romNum;

}

console.log(convert(29));
// should return XXIX
console.log(convert(3999));
// should return MMMCMXCIX