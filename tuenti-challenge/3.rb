# Solution for Challenge 3 - Fortunata and Jacinta

# Prepocessing
ranking = Hash.new(0)
File.open('pg17013.txt').each do |line|
  words = line.downcase.gsub!(/[^a-záéíóúüñ]/, ' ').split
  words.reject! { |word| word.length < 3 }
  words.each { |word| ranking[word] += 1 }
end
final_ranking_array = ranking.sort_by {|k,v| [-v, k]}
final_ranking_hash = Hash[final_ranking_array.map.with_index { |e, i| [e[0],[e[1],i]] }]

cases = $<.gets.to_i
cases.times do |case_i|
  str = $<.gets(chomp: true)
  if str.to_i.to_s == str # it is a number
    sol = final_ranking_array[str.to_i - 1]
    puts "Case ##{case_i + 1}: #{sol[0]} #{sol[1]}"
  else
    sol = final_ranking_hash[str]
    puts "Case ##{case_i + 1}: #{sol[0]} ##{sol[1] + 1}"
  end
end

