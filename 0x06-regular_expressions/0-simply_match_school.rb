#!/usr/bin/env ruby
#Ruby script that acccepts one argument and 
#pass it to a regular expressiion matching method
def match_school(input)
  if input.match(/School/)
    puts input.scan(/School/).join
  else
    puts ""
  end
end

input = ARGV[0]
match_school(input)
