# Solution for Challenge 9 - Just Another Day on Battlestar Galactica

$KEY = [3, 2, 2, 1, 1, 1, 3, 2, 9, 0, 8, 7, 5, 6, 1, 8, 7, 1, 4, 1, 6, 0, 4]
def decrypt(message)
  result = ''
  hex_message = [message].pack 'H*'
  hex_message.bytes.each_with_index do |n, i|
    result << (n ^ $KEY[i]).chr
  end
  puts result
end

decrypt(ARGV[0])
