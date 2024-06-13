from django import forms

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(
        label="CSVファイル",  # 入力すると文字列をHTML側で表示できる
        max_length=1000,  # 最大文字数を制限できる（ファイルだとあまり意味がない？）
        allow_empty_file=False,  # 空ファイルを許可しない
    )
