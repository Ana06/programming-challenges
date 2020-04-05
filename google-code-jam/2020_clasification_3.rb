# Solution for Qualification Round 2020, problem 3 - Parenting Partnering Returns
# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

def schedule
  n = $<.gets.to_i
  cameron = 0
  jamie = 0
  solution = '0' * n
  activities = n.times.map { |i| [i, $<.gets.split.map(&:to_i)] }
  activities.sort! { |a, b | a[1][0] <=> b[1][0] }
  activities.each do |i, activity_times|
    if activity_times[0] >= cameron # I like to keep Cameron busy
      solution[i] = 'C'
      cameron = activity_times[1]
    elsif activity_times[0] >= jamie
      solution[i] = 'J'
      jamie = activity_times[1]
    else
      return 'IMPOSSIBLE'
    end
  end
  return solution
end

cases = $<.gets.to_i
cases.times do |case_i|
  puts "Case ##{case_i + 1}: #{schedule}"
end

