# Solution for Problem 1 - Rotation
# https://www.hackerearth.com/challenges/competitive/june-circuits-19/algorithm/rotation-1-38ecf5a7

n = STDIN.gets.chomp.to_i
s = STDIN.gets.chomp
t = STDIN.gets.chomp

n.times do |i|
  if s == t
    puts i
    exit
  end
  s = s[1..-1]
  t = t[0..-2]
end

puts 0
