#!/usr/bin/env ruby

## T,A' -> F'

## matching by unique records

require './common-io.rb'

##

DUPLICATED = ','

def to_id_tail(line)
  raise line unless /^([^,]+),(.*)$/ =~ line
  [$1, $2]
end

def make_tail2id(t)
  t.inject({}) do |h, line|
    id, tail = to_id_tail(line)
    h[tail] = (h[tail] ? DUPLICATED : id)
    h
  end
end

## input T,A'
#read_table_skip()
t = read_table()
a1 = read_table()

tail2id = make_tail2id(t)
pid2id = {}
a1.each do |line|
  pid, tail = to_id_tail(line)
  next unless tail2id[tail]
  next if tail2id[tail] == DUPLICATED
  pid2id[pid] = tail2id[tail]
end
res = pid2id.map{|kv| kv.join(',')}

## output F'
write_table(res)
