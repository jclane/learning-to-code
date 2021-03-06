// Translate the provided string to pig latin.

function translatePigLatin(str) {
  const vowels = /[aeiouAEIOU]/;
  
  if (vowels.test(str.charAt()) === true) {
    str += "way";
  } else {
    var num = str.search(vowels);
    var letter = str.slice(0, num);
    str = str.slice(num, str.length) + letter + "ay";
  }
    
  return str;
}

console.log(translatePigLatin("consonant"));
