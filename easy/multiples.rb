#!/usr/bin/env ruby
File.open(ARGV[0]).each_line do |line|  
    x,n = line.split(',').map{|x|x.to_i}
    m = n
    loop do
        break if m>x
        m+=n
    end
    p m
end