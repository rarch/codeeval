#!/usr/bin/env ruby

# def eratosthenes(n)
#     is_prime = [false,false]+[true]*(n-1)
#     2.upto(Math.sqrt(n).ceil) do |i|
#       next if !is_prime[i]
#       (i*i).step(n,i) do |j|
#         is_prime[j] = false
#       end
#     end
#     (0..n).select{|i| is_prime[i]}
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