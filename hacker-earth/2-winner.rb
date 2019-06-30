cases = STDIN.gets.chomp.to_i

def winner(n, k)
  (n % (k + 1) == 0) ? 'Dishant' : 'Arpa'
end

cases.times do |i|
  n, k = STDIN.gets.split.map(&:to_i)

  puts winner(n, k)
end

