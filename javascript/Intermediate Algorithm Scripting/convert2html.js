/*
Convert the characters &, <, >, " (double quote), and ' (apostrophe), in a 
string to their corresponding HTML entities.
*/

function convertHTML(str) {

  const amp = /[&]/g;
  const less = /[<]/g;
  const greater = /[>]/g;
  const doubleQ = /["]/g;
  const apos = /[']/g;

  str = str.replace(amp, "&amp;");
  str = str.replace(less, "&lt;");
  str = str.replace(greater, "&gt;");
  str = str.replace(doubleQ, "&quot;");
  str = str.replace(apos, "&apos;");
  
  return str;
}

console.log(convertHTML("Dolce & Gabbana"));
