# coding: utf-8

# 概要: T, A' が正しい前提で F' の書式を確認
# 入力: J(T, A', F')
# 出力:
#   正しければ何もなし
#   正しくなければ標準エラーにエラーメッセージを吐いてエラー終了

require './common-io.rb'

# IDの集合を取り出す
def to_ids(t)
  h = {}
  t.each{|line| h[line.split(/,/)[0]] = true}
  return h
end

# エラーメッセージを吐いて終了
def error(i, msg = '')
  raise "Line #{i}: #{msg}"
end

# input T, A', F'
t = read_table()
a1 = read_table()
f1 = read_table()

# T のID集合
tids = to_ids(t)
# A' のID集合
pids = to_ids(a1)

seen = {}
f1.each_with_index do |s, i|
  # F' のフォーマットは '(仮ID),(ID)'
  error(i, "invalid format") unless /\A(\d+),(\d+)\z/ =~ s
  pid, tid = [$1, $2]
  # 仮IDはAに含まれなくてはならない
  error(i, "unknown pid") unless pids[pid]
  # IDはTに含まれなくてはならない
  error(i, "unknown id") unless tids[tid]
  # F'に同一の仮IDが2度含まれてはいけない
  error(i, "duplicated pid") if seen[pid]
  seen[pid] = true
end
