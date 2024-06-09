foo = {'ねじ', 'ボルト', 'ボルト', 'ナット'}

# fooはset型なので重複した値は含まれない
print(foo)  #  {'ナット', 'ねじ', 'ボルト'}

bar = {'ボルト', 'ナット', 'トラス小ねじ'}

# 差集合を取得できる
# 差集合 = foo に存在して bar には存在しない要素のこと
baz = foo - bar

print(baz)  #  {'ねじ'}