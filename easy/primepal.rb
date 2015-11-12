#!/usr/bin/env ruby

def isPrime(n)
    (2).upto(Math.sqrt(n).to_i+1) {|i|
      return false if n%i==0 }
    true
end

def isPal(n)
    s=n.to_s
    s==s.reverse
end

(1000).downto(2) {|i|
  if isPrime(i) && isPal(i)
    puts i
    exit(0)
  end}