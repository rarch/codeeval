#!/usr/bin/env ruby

def fizzbuzz(f,b,n)
    (1..n).each do |i|
        if i%f==0
            print 'F'
        end
        if i%b==0
            print 'B'
        end
        if i%f!=0 && i%b!=0
            print i
        end
        break if i==n
        print " "
    end
    puts
end

File.open(ARGV[0]).each_line do |line|
    x,y,n=line.split().map{|d|d.to_i}
    # p x
    fizzbuzz(x,y,n)
end