import csv
from csv import DictReader

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
        from io import StringIO
        for chunk in file.chunks():
            # bytesからstrに変換
            decoded_chunk: str = chunk.decode('utf-8')
            reader = csv.DictReader(StringIO(decoded_chunk))
            for row in reader:
                print(row)
                self.save_to_db2(row)