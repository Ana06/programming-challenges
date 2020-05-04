# Solution for Challenge 1 - Rock, Paper, Scissors

require 'set'

def winner(players_array)
  return '-' if players_array[0] == players_array[1]
  players = Set.new(players_array)
  return 'R' if players == Set['R', 'S']
  return 'S' if players == Set['S', 'P']
  return 'P' if players == Set['P', 'R']
end

cases = $<.gets.to_i
cases.times do |case_i|
  players = $<.gets.split

  puts "Case ##{case_i + 1}: #{winner(players)}"
end

