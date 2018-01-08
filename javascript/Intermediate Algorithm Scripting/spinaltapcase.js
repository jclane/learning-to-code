// Convert a string to spinal case. Spinal case is all-lowercase-words-joined-by-dashes.

function spinalCase(str) {
  const regexp = /[\s\_]/g;
  
  str = str.replace(/([a-z])([A-Z])/g, '$1 $2').replace(regexp, '-').toLowerCase();

  return str;
}

console.log(spinalCase('AllThe-small Things'));