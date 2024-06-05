import csv
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Supply

class UploadCSVView(View):
    template_name = 'upload_csv.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        csv_file = request.FILES['csv_file']
        # csv_file_data = self.read_csv_file(csv_file)
        # csv_file_data = self.chunks_csv(csv_file)
        self.chunks_csv(csv_file)
        # self.save_to_db(csv_file_data)
        messages.success(request, 'CSV upload successful!')
        return render(request, self.template_name)

    # def read_csv_file(self, file):
    #     print(type(file))  # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    #     csv_file_data = file.read().decode('utf-8').splitlines()
    #     print(type(csv_file_data))  # <class 'list'>
    #     reader = csv.DictReader(csv_file_data)
    #     print(type(reader))  # <class 'csv.DictReader'>
    #     return reader

    def save_to_db(self, reader):
        for row in reader:
            print(row)  # dict
            print(type(row))
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
            print(chunk)
            print(type(chunk))  # bytes
            decoded_chunk = chunk.decode('utf-8')
            print(decoded_chunk)
            print(type(decoded_chunk))  # str
            reader = csv.DictReader(StringIO(decoded_chunk))
            for row in reader:
                print(row)
                self.save_to_db2(row)