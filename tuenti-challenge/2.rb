# Solution for Challenge 2 - The Lucky One

cases = $<.gets.to_i
cases.times do |case_i|
  n = $<.gets.to_i
  winners = {}
  loosers = {}
  n.times do |case_i|
    winner, looser, r = $<.gets.split.map(&:to_i)
    winner, looser = looser, winner if r == 0
    loosers[looser] = true
    winners.delete(looser)
    winners[winner] = true unless loosers[winner]
  end
  strongest_player = winners.shift[0]  # There should be only one
  puts "Case ##{case_i + 1}: #{strongest_player}"
end

