#!/usr/bin/env ruby
File.open(ARGV[0]).each_line do |line|  
    # Do something with line, ignore empty lines
    n,i,j = line.split(',').map{|x|x.to_i}
    x,y = [i,j].map{|p|(n>>p-1)&1}
    p x==y
end