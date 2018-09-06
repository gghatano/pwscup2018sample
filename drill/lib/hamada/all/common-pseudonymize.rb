## pseudonymize
def pseudonymize2(ids)
  uids = ids.sort.uniq
  id2pid = Hash[uids.zip((1..uids.size).to_a.shuffle)]
  ids.map{|id| id2pid[id]}
end

def pseudonymize(ids)
  is_id = Hash[ids.map{|id| [id, true]}]
  n = is_id.size
  pids = (1..(n * 2)).to_a.delete_if{|i| is_id[i.to_s]}[0,n]
  id2pid = Hash[is_id.map{|id,tr| id}.zip(pids.shuffle)]
  ids.map{|id| id2pid[id]}
end
