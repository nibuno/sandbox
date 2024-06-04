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
        csv_file_data = self.read_csv_file(csv_file)
        self.save_to_db(csv_file_data)
        messages.success(request, 'CSV upload successful!')
        return render(request, self.template_name)

    def read_csv_file(self, file):
        csv_file_data = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(csv_file_data)
        return reader

    def save_to_db(self, reader):
        for row in reader:
            Supply.objects.update_or_create(
                name=row['名前'],
                price=row['価格'],
                quantity=row['数量']
            )
