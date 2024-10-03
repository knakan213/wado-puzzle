import sys
import itertools
import random

# 二字熟語の各1文字目から、その字に続く2文字目の集合への辞書abと
# 各2文字目から、その字に先行する1文字目の集合への辞書baを作成する
ab, ba = {}, {}
with open('all.csv') as f:
    # all.csvは(二字または三字)熟語が頻度順に並んでいる 
    # 出題を常識的な難易度にするため、ここでは最頻20000項目程度を使う
    for s in f.readlines()[:20000]:
        if s[2] == ',': # 二字熟語を選別
            ab.setdefault(s[0], set()).add(s[1])
            ba.setdefault(s[1], set()).add(s[0])
            
def solve(uldr):
    '''上左下右の漢字を表わす長さ4のシーケンスを取り、解答の集合を返す'''
    return set.intersection(*(d.get(x, set())
                              for d, x in zip((ab, ab, ba, ba), uldr)))

assert solve('明告昼熱') == {'白'} # Wikipediaに載っていた例
assert solve('支退口席') == {'出'} # 灘中学校 2009年 入試 国語

def main():
    '''和同開珎パズルをランダムに生成し出題する'''
    xs = list(set(ab) & set(ba)) # 答えの候補のリスト
    while True:
        x = random.choice(xs) # 答えをランダムに選ぶ
        # xを答えとする出題のリストqsを作る
        qs = [(u, l, d, r)
              for d, r in itertools.combinations(ab[x], 2)
              for u, l in itertools.combinations(ba[x], 2)
              if solve((u, l, d, r)) == {x}] # 答えがユニークに定まる出題に限定
        if qs:
            u, l, d, r = random.choice(qs)
            print(f'   {u}')
            print(f'{l}[  ]{r}')
            print(f'   {d}')
            input()
            print(x, ':', u+x, l+x, x+d, x+r)
            print()

if __name__ == '__main__':
    if len(sys.argv) == 2 and len(sys.argv[1]) == 4:
        print(*solve(sys.argv[1]))
    elif len(sys.argv) == 1:
        main()
    else:
        print('Invalid arguments:', ' '.join(sys.argv))
        print('Usage: python3', sys.argv[0])
        print('       python3 %s <four kanjis>' % sys.argv[0])
        print('Example: python3 %s 妥割方分' % sys.argv[0])
        sys.exit(1)
