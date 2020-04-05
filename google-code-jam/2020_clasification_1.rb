# Solution for Qualification Round 2020, problem 1 - Vestigium
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

cases = $<.gets.to_i
cases.times do |case_i|
  n = $<.gets.to_i
  trace = 0
  num_rows = 0
  columns = Array.new(n){[]}
  n.times do |i|
    line = $<.gets.split.map(&:to_i)
    trace += line[i]
    line.each_with_index do |x, index|
      columns[index] << x
    end
    num_rows += 1 if line.uniq!
  end
  # I could use the sum() method if Google wouldn't use such an old version of Ruby
  num_columns = columns.map! { |column| column.uniq! ? 1 : 0 }.inject(0) { |sum, x| sum + x }
  puts "Case ##{case_i + 1}: #{trace} #{num_rows} #{num_columns}"
end

