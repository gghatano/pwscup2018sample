## csv <-> mat
def csv2mat(c)
  c.map{|s| s.split(/,/)}
end

def mat2csv(m)
  m.map{|a| a.join(',')}
end
