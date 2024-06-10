foo = {'ねじ', 'ボルト', 'ボルト', 'ナット'}

# fooはset型なので重複した値は含まれない
print(foo)  #  {'ナット', 'ねじ', 'ボルト'}

bar = {'ボルト', 'ナット', 'トラス小ねじ'}

# 差集合を取得できる
# 差集合 = foo に存在して bar には存在しない要素のこと
baz = foo - bar

# difference を利用しても良いらしい
# https://docs.python.org/ja/3/library/stdtypes.html#frozenset.difference
# こちらだと、他にも集合を加えられるみたいだった(*others)となっていたので
# baz = foo.difference(bar)

print(baz)  #  {'ねじ'}
