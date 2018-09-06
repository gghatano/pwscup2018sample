#!/usr/bin/env python3

# T,A' -> F'

import re
import random
from common import read_table, write_table

## input T,A'
t = read_table()
a1 = read_table()

cids = set()
pids = set()
cid_stocks = {}
item_pids = {}
pid_trnum = {}

for tr in t:
    cid,date,stockid,price,num = tr.split(',')
    cids.add(cid)
    cid_stocks[cid] = cid_stocks.get(cid,[])+[stockid]

for a_tr in a1:
    pid,date,stockid,price,num = a_tr.split(',')
    pids.add(pid) 
    pid_trnum[pid] = pid_trnum.get(pid,0)+1
    m=re.match(r"\{(.*)\}",stockid)
    sclist = m.group(1).split(";") if m else [stockid]
    for sc in sclist:
        item_pids[sc] = item_pids.get(sc,[])+[pid]

result = list()
unselected_pids = pids
for cid in cids:
    cid_trnum=len(cid_stocks[cid])
    cands = unselected_pids
    cands_trnum = [p for p in pid_trnum.keys() if pid_trnum[p] <= cid_trnum]
    cands = cands.intersection(set(cands_trnum)) # cid に合致する pid の候補．登場回数は単純減少なのを使って絞り込んでいる
    for stock in cid_stocks[cid]:
        if len(cands)<=1: break
        cands = cands.intersection(set(item_pids.get(stock,[])))
    if len(cands)>0:
        pid = random.sample(cands,1)[0]
        result.append('{},{}'.format(pid,cid))
        unselected_pids.remove(pid)
    
## output F'
write_table(result)
