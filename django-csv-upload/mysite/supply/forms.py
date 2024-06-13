from django import forms

class UploadCSVForm(forms.Form):
    csv_file = forms.FileField(
        label="CSVファイル",  # 入力すると文字列をHTML側で表示できる
    )
