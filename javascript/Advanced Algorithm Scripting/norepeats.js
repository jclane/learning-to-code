/*
Return the number of total permutations of the provided string that 
don't have repeated consecutive letters. Assume that all characters 
in the provided string are each unique.

For example, aab should return 2 because it has 6 total permutations 
(aab, aab, aba, aba, baa, baa), but only 2 of them (aba and aba) don't 
have the same letter (in this case a) repeating.
*/

function permAlone(str) {
  var permArr = [], usedChars = [];
  let count = 0;
  
  function permute(input) {
    var i, ch, chars = input.split("");
    for (i = 0; i < chars.length; i++) {
      ch = chars.splice(i, 1);
      usedChars.push(ch);
      if (chars.length == 0)
        permArr[permArr.length] = usedChars.join("");
        permute(chars.join(""));
        chars.splice(i, 0, ch);
        usedChars.pop();
      }
      return permArr;
    }
    
  permute(str);
  str = 0;
  
  permArr.forEach(function(el) {   
    if (!(/([a-z])\1/i).test(el)) {
      str++;
    }
  });
  
  return str;
}

// This should return 2.
console.log(permAlone('aab'));
