# Solution for Challenge 13 - The Great Toilet Paper Fortress

# Do not program this, but write a mathematical formula!
def m(h, d1=1, d2=d1)
  d1 * d2 * h + (2 * (h - 2) * (h * (3 * d1 + 3 * d2 + 8 * h - 8) - 6)) / 3
end

def result n
  return 'IMPOSSIBLE' if n < 43

  h_max = 3
  (4..n).each do |h|
    break if m(h) > n
    h_max = h
  end

  m_max = nil
  d1_max = nil
  d2_max = nil
  (1..n).each do |d1|
    m = m(h_max, d1)
    break if m > n
    d1_max = d1
    m_max = m
    m = m(h_max, d1, d1 + 1)
    if m <= n
      m_max = m
      d2_max = d1 + 1
    else
      d2_max = d1
    end
  end

  "#{h_max} #{m_max.round}"
end

cases = $<.gets.to_i
cases.times do |case_i|
  n = $<.gets.to_i
  puts "Case ##{case_i + 1}: #{result(n)}"
end

