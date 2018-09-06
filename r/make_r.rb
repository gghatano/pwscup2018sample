# coding: utf-8

# 実行方法:
#  $ ruby make_r.rb
#
# 説明:
#  R.csv を生成

# パラメータ
P = 1.0 / 3 # p
ALPHA = 0.01 / 20 # \alpha
N = 1000 # 顧客数

# log((i+1)!) = log(i+1) + log(i!) を利用して，LOG_FACT = (log(0!), log(1!), ..., log(N!)) を計算
LOG_FACT = (0...N).each_with_object([0]){|i, a| a << a[-1] + Math.log(i+1)}
# log P
LOG_P = Math.log(P)

# log( {n \choose r} ) を計算
def log_choose(n, r)
  LOG_FACT[n] - LOG_FACT[r] - LOG_FACT[n - r]
end

# {n \choose k} p^k を計算
def prob(n, k)
  Math.exp(log_choose(n, k) + k * LOG_P)
end

# s_k := \sum_{i = k}^{n} prob(n, k) とするとき，
# s_k < ALPHA を満たす最小の k を求める
def find_min_k(n)
  s = 0.0
  n.downto(1) do |k|
    s += prob(n, k)
    return k + 1 if s >= ALPHA
  end
  return 0
end

$stderr.puts [
"p = #{P}",
"alpha = #{ALPHA}",
"n = #{N}"
]

# 各 r(n) を計算して出力
$stdout.puts "0,1" # r(0) := 1
1.upto(N) do |n|
  r = find_min_k(n) # r(n)
  # n,r(n) を出力
  $stdout.puts [n, r].join(',')
end
