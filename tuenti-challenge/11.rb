# Solution for Challenge 11 - All the Possibilities

cases = $<.gets.to_i
cases.times do |case_i|
  numbers = $<.gets.split.map(&:to_i)
  n_0 = numbers.shift
  valid_numbers = (1..(n_0 - 1)).to_a - numbers

  # Table for dynamic programming - similar to coin change problem
  table = Array.new(n_0 + 1, 0)
  table[0] = 1
  valid_numbers.each do |i|
    (i..n_0).each do |j|
      table[j] += table[j - i]
    end
  end
  puts "Case ##{case_i + 1}: #{table[n_0]}"
end

