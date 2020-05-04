# Solutions for Challenge 12 - Hackerman Origins

def str_to_i text
  text.each_byte.reduce(''){ |result, b| result << b.to_s(16).rjust(2, '0') }.to_i(16)
end


e = 65537 # Common value of e

f = File.open('plaintexts/test1.txt')
text1 = str_to_i(f.read)
f = File.open('plaintexts/test2.txt')
text2 = str_to_i(f.read)
f = File.open('ciphered/test1.txt')
ciphered1 = str_to_i(f.read)
f = File.open('ciphered/test2.txt')
ciphered2 = str_to_i(f.read)

# Be patient, this will take some time!
n = (text1**e - ciphered1).gcd(text2**e - ciphered2)
puts n

