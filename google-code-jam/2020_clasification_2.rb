# Solution for Qualification Round 2020, problem 2 - Nesting Depth
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9f

cases = $<.gets.to_i
cases.times do |case_i|
  # I could use the gets(chomp: true) if Google wouldn't use such an old version of Ruby
  line = $<.gets.chomp.each_char.map(&:to_i)
  open_parenthesis = 0
  solution = ''
  line.each do |number|
    if open_parenthesis < number
      solution <<  '(' * (number - open_parenthesis)
    elsif number < open_parenthesis
      solution << ')' * (open_parenthesis - number)
    end
    solution << number.to_s
    open_parenthesis = number
  end
  solution << ')' * open_parenthesis
  puts "Case ##{case_i + 1}: #{solution}"
end

