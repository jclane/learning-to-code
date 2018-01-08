/*
Sum all the prime numbers up to and including the provided number.

A prime number is defined as a number greater than one and having only 
two divisors, one and itself. For example, 2 is a prime number because it's 
only divisible by one and two.

The provided number may not be a prime.
*/

function sumPrimes(num) {
  var primes = [];
  var sum = 0;
    
  // Count up to num
  for (var counter = 0; counter <= num; counter++) {
    var notPrime = false;
    
    // Check if Prime
    for (var i = 2; i <= counter; i++) {
      if (counter % i === 0 && counter !== i) {
        notPrime = true;
      }
    }
    
    // If prime add to primes array
    if (notPrime === false) {
      primes.push(counter);
    }
  }
  
   // Sum numbers in primes array
 for (var j = 2; j < primes.length; j++) {
   sum += primes[j];

 }
  
  return sum;

}

console.log(sumPrimes(10));