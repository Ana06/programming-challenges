# Solution for Problem 5 - Function value
# https://www.hackerearth.com/problem/algorithm/june-circuits-function-value-bdd25438

def exp_mod(base, exponent, modulo)
  result = 1
  while exponent > 0
    if exponent.odd?
      result = (result * base) % modulo
    end
    base = base**2 % modulo
    exponent = exponent / 2
  end

  result
end

def sum_to(r, modulo)
  return 0 if r < 1
  return 1 if r == 1

  sum = 0

  if r.odd?
    sum += exp_mod(3,r/2, modulo)
    r -= 1
  end

  k = r/4
  # geometric serie 1 + 9**2 + ... + 9**(k-1): (9**k-1)/8
  geometric_serie = (exp_mod(9,k, modulo * 8) - 1) / 8
  sum += if r % 4 == 2
            2*k + 30 * geometric_serie + 2
          else
            2*k + 10* geometric_serie
          end

  sum % modulo
end


T, P = STDIN.gets.split.map(&:to_i)

T.times do |i|
  l, r = STDIN.gets.split.map(&:to_i)

  puts (sum_to(r, P) - sum_to(l-1, P)) % P
end

