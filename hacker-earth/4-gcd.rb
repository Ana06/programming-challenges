LIMIT = 10 ** 9 + 7

def sol(n)
  combinations_array = []
  limit = n/8
  (n/4).downto(1).each do |number|
    number_multiples = n / number

    number_combinations = ((number_multiples-3)..number_multiples).reduce(1, :*) / 24

    if number <= limit
      i = combinations_array.length
      while (i -= number) >= 0
        number_combinations -= combinations_array[i][1]
      end
    end

    combinations_array << [number, number_combinations]
  end
  sum = combinations_array.map! { |e| e[0]**4 * e[1] }.reduce(0, :+)

  sum % LIMIT
end

cases = STDIN.gets.to_i

cases.times do |i|
  n = STDIN.gets.to_i
  puts sol(n)
end
