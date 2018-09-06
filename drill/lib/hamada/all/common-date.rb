## date
require 'date'

# yy/mm/dd -> int
def date2int(d)
  raise d unless /^(\d+)\/(\d+)\/(\d+)$/ =~ d
  Date.new($1.to_i, $2.to_i, $3.to_i) - Date.parse('2010-01-01')
end

# int -> yy/mm/dd
def int2date(n)
  d = (Date.parse('2010/1/1') + n)
  "#{d.year}/#{d.month}/#{d.day}"
end
