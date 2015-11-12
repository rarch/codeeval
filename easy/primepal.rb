#!/usr/bin/env ruby

# def eratosthenes(n)
#   nums = [nil, nil, *2..n]
#   (2..Math.sqrt(n)).each do |i|
#     (i**2..n).step(i){|m| nums[m] = nil}  if nums[i]
#   end
#   nums.compact
# end

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