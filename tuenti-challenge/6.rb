# Solution for Challenge 6 - Knight Labyrinth

require 'socket'

$hostname = '52.49.91.111'
$port = 2003

def print_map
  $map.each { |line| r = line.join; puts r unless r.strip.empty?}
end

def read(line, colum)
  line_index = line
  while line_index < line + 5
    map_line = $s.gets(chomp:true)
    next if map_line.nil? || map_line.empty? || map_line.include?('no time to lose!')
    if map_line.include?('---') # I found the princess!
      print_map
      puts "#{map_line}"
      $s.close
      exit
    end
    $map[line_index][colum..(colum + 4)] = map_line.split('')
    line_index += 1
  end
  0
end

def new_state(state, movement_i)
  movement = $movements_arr[movement_i]
  [state, movement].transpose.map(&:sum)
end

def open_state(state, previous_i)
  go_back_i = (previous_i + 4) % 8
  open_states = []
  $movements_arr.each_with_index do |movement, index|
    next if index == go_back_i
    new_state = new_state(state, index)
    unless $map[new_state[0]][new_state[1]] == '#' || $closed_states[new_state]
      open_states << [new_state, index, $visited_states[new_state]]
    end
  end
  if open_states.empty?
    $closed_states[state] = true
    return [new_state(state, go_back_i), go_back_i]
  end
  # Explore unexplored areas!
  open_states.sort_by{|state, movement_i, visited| visited }.first[0..1]
end

$s = TCPSocket.open($hostname, $port)
$map = Array.new(220) { Array.new(220, ' ') }
$movements_str = ['2U1R', '1U2R', '2U1L', '1U2L',
                  '2D1L', '1D2L', '2D1R', '1D2R',]
$movements_arr = [[-2, 1], [-1, 2], [-2, -1], [-1, -2],
                  [2, -1], [1, -2], [ 2,  1], [ 1,  2]]
$closed_states = {}
$visited_states = Hash.new(0)

previous_i = 6 # The previous state is a wall
state = [110, 110]
read(108, 108)
loop.with_index do |_, i|
  new_state, movement_i = open_state(state, previous_i)
  $visited_states[new_state] += 1
  $s.puts($movements_str[movement_i])
  status = read(new_state[0] - 2, new_state[1] - 2)
  state = new_state
  previous_i = movement_i
end

