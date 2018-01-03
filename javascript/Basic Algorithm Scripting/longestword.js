// Return the length of the longest word in the provided sentence.

function findLongestWord(str) {
  var strArray = str.split(' ');
  var longest;
  var foo = 0;

  for (var i = 0; i < strArray.length; i++) {
      if (strArray[i].length > foo) {
        foo = strArray[i].length;
        longest = strArray[i];
        str = longest;
      }
  }

  return str.length;
}

console.log(findLongestWord('The quick brown fox jumped over the lazy dog'));
