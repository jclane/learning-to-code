// Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.

function titleCase(str) {
  var strArray = str.split(' ');

  for (i = 0; i < strArray.length; i++) {
    strArray[i] = strArray[i].charAt(0).toUpperCase() + strArray[i].slice(1).toLowerCase();
  }

  str = strArray.join(' ');

  return str;
}

console.log(titleCase("I'm a liTTle tea pot"));
