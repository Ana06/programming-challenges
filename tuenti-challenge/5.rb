# Solution for Challenge 5 - Tuentistic Numbers

def tuentistics(n)
  num_tuentistics = n / 20
  n %= 20

  index = 0
  while n > 0 && index < num_tuentistics
    to_add = [n, 9].min
    n -= to_add
    index += 1
  end
  return 'IMPOSSIBLE' if n > 0
  return num_tuentistics
end

cases = $<.gets.to_i
cases.times do |case_i|
  n = $<.gets.to_i
  puts "Case ##{case_i + 1}: #{tuentistics(n)}"
end

