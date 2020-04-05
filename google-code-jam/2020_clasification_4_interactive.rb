#!/usr/bin/env ruby

# Solution for Round 1C 2019, problem 2 - Power Arrangers
# https://codingcompetitions.withgoogle.com/codejam/round/00000000000516b9/0000000000134e91

$stdout.sync = true

$count = 0

def get_bit(index, s, different_pair, same_pair)
  $count += 1
  check_fluctuations(s, different_pair, same_pair)
  puts index
  STDOUT.flush
  return STDIN.gets.to_i
end

def complement(array)
  array.map!{ |i| i ^ 1 if i}
end

def check_fluctuations(s, different_pair, same_pair)
  return unless $count != 1 && $count % 10 == 1
  if different_pair && same_pair
    bit_dif = get_bit(different_pair, s, different_pair, same_pair)
    bit_same = get_bit(same_pair, s, different_pair, same_pair)
    if bit_dif != s[different_pair - 1] && bit_same != s[same_pair - 1]
      complement(s)
    elsif bit_dif != s[different_pair - 1] && bit_same == s[same_pair - 1]
      s.reverse!
    elsif bit_dif == s[different_pair - 1] && bit_same != s[same_pair - 1]
      complement(s.reverse!)
    end
  else
    bit = get_bit(1, s, different_pair, same_pair)
    complement(s) if bit != s[0]
  end
end

t, b = STDIN.gets.split.map(&:to_i)

t.times do |t|
  s = Array.new(b, nil)
  different_pair = nil
  same_pair = nil
  $count = 0
  (1..b/2).each do |index|
    # Annoying fluctuations (when reversing as we query wrong index), just do one extra query
    get_bit(1, s, different_pair, same_pair) if $count % 10 == 9
    bit1 = get_bit(index, s, different_pair, same_pair)
    s[index - 1] = bit1
    bit2 = get_bit(b - index + 1, s, different_pair, same_pair)
    s[b - index] = bit2
    if bit1 != bit2
      different_pair = index
    else
      same_pair = index
    end
  end
  puts s.join
  STDOUT.flush
  veredict = STDIN.gets.chomp
  exit if veredict == 'N'
end

