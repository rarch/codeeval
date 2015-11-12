#!/usr/bin/env ruby
def isprime(n)
    return false if n<2 or n%2==0
    3.step(Math.sqrt(n).ceil,2) do |i|
        return false if n%i==0
    end
    true
end

count=1
sum=2
n=3
while count<1000 do
    if isprime(n)
        count+=1
        sum+=n
    end
    n+=2
end
puts sum