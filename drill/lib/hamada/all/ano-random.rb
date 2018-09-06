# coding: utf-8

# 実行方法:
#  $ ruby ano-random.rb
#
# 説明:
#  T をランダムに一般化
#
# 入出力: J(T) -> J(A)

require './common-io.rb'
require './common-csv.rb'
require './common-pseudonymize.rb'
require './common-date.rb'

# a のランダムな要素
def sample(a)
  a[rand(a.size)]
end

# a の各要素を自身を含むランダムな集合(大きさは高々m)化
def to_random_set(a, m = 10)
  a.map do |x|
    b = [x]
    rand(m).times{b << sample(a)}
    b = b.sort.uniq
    b.size == 1 ? x : '{' + b.join(';') + '}'
  end
end

# 最小値
def min(x, y)
  x < y ? x : y
end

# 最大値
def max(x, y)
  x > y ? x : y
end

# a の各要素を自身を含むランダムな範囲化
def to_random_range(a, m, s2num, num2s)
  a.map do |s|
    b0 = b1 = s2num.call(s)
    rand(m).times{
      c = s2num.call(sample(a))
      b0 = min(b0, c)
      b1 = max(b1, c)
    }
    b0 == b1 ? num2s.call(b0) : "[#{num2s.call(b0)};#{num2s.call(b1)}]"
  end
end

# 整数をランダムな範囲化
def to_random_range_int(a, m = 10)
  to_random_range(a, m, proc{|s| s.to_i}, proc{|i| i.to_s})
end

# 実数値をランダムな範囲化
def to_random_range_float(a, m = 10)
  to_random_range(a, m, proc{|s| s.to_f}, proc{|f| sprintf("%.2f", f)})
end

# 日付をランダムな範囲化
def to_random_range_date(a, m = 10)
  to_random_range(a, m,
            proc{|s| date2int(s)},
            proc{|t| int2date(t)})
end

# input T
t = read_table()

# t を行列化して転置
t = csv2mat(t).transpose

# 列ごとにランダム化
t[0] = pseudonymize(t[0])
t[1] = to_random_range_date(t[1], 10)
t[2] = to_random_set(t[2], 10)
t[3] = to_random_range_float(t[3], 3)
t[4] = to_random_range_int(t[4], 10)

# 2列目から4列目の各要素に対して確率 0.1 でセル削除
1.upto(4){|i| t[i] = t[i].map{|x| rand() < 0.1 ? '*' : x}}

# t を転置して文字列の配列化
t = mat2csv(t.transpose)

# 確率 0.1 で行削除
t = t.map{|x| rand() < 0.1 ? '*,*,*,*,*' : x}

# output A
write_table(t)
