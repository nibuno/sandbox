import random

# random.normalvariate
# 正規分布
# mu=平均
# sigma=標準偏差

for i in range(10):
    random.normalvariate(mu=0, sigma=1)
    # 例えば、以下のようになる
    """
    0.07012413030886526
    -0.8053222232101854
    -0.6156729917996437
    -0.07791680550735719
    0.09369095179235093
    0.4337309507561014
    0.19756601885804223
    0.8099696874538449
    1.1611989419760143
    -1.2113131691520214
    """

# シーケンス用の関数
# https://docs.python.org/ja/3/library/random.html#functions-for-sequences

# random.choice
# seqからランダムに1つ選択
random.choice(seq=[1, 2, 3, 4, 5])

# random.choices
# populationから重複ありでk個選び、リストで返す
random.choices(population=[1, 2, 3, 4, 5], weights=None, cum_weights=None, k=3)
