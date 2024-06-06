import csv
from csv import DictReader
from io import StringIO

from django.contrib import messages
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render
from django.views import View

from .models import Supply


class UploadCSVView(View):
    template_name = 'upload_csv.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        csv_file = request.FILES['csv_file']
        self.chunks_csv(csv_file)
        messages.success(request, 'CSV upload successful!')
        return render(request, self.template_name)

    def read_csv_file(self, file: InMemoryUploadedFile):
        csv_file_data: list = file.read().decode('utf-8').splitlines()
        reader: DictReader = csv.DictReader(csv_file_data)
        return reader

    def save_to_db(self, reader):
        for row in reader:
            # rowのtypeはdict
            Supply.objects.update_or_create(
                name=row['名前'],
                price=row['価格'],
                quantity=row['数量']
            )

    def save_to_db2(self, row):
        Supply.objects.update_or_create(
            name=row['名前'],
            price=row['価格'],
            quantity=row['数量']
        )


    def chunks_csv(self, file):
        for chunk in file.chunks():
            # bytesからstrに変換
            decoded_chunk: str = chunk.decode('utf-8')
            reader = csv.DictReader(StringIO(decoded_chunk))
            reader_list = list(reader)
            # 1回目のループでreaderが空になる
            # これは、readerがイテレータであり、1回目のループで最後まで読み込んでしまうため
            # 対処法としては、リストに変換することが考えられる
            # ただし、リストにした場合はreaderが空になるので1回目のreaderも使えなくなる
            print("1回目のreader")
            for row in reader:
                print(row)
                self.save_to_db2(row)
            # 2回目のループはreaderが空なので何もできない
            print("2回目のreader")
            for row in reader:
                print(row)
                self.save_to_db2(row)

            print("1回目のreader_list")
            for row in reader_list:
                print(row)  # {'名前': 'ねじ', '価格': '100', '数量': '10'}
                self.save_to_db2(row)

            print("2回目のreader_list")
            for row in reader_list:
                print(row)
                self.save_to_db2(row)