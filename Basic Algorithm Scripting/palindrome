// Return true if the given string is a palindrome. Otherwise, return false.

function palindrome(str) {
  str = (str.toLowerCase().replace(/[\.,-\/#!$%\^&\*;:{}=\-_`~()]/g,'').replace(/\s+/g,''));
  var strArray = str.split("").reverse().join("").split(" ").reverse();

if (str == strArray.toString()) {
    return true;
  } else {
    return false;
  }
}

console.log(palindrome("Race car"));
