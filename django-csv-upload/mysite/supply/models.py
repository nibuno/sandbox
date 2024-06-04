from django.db import models


class Supply(models.Model):
    """仕入モデル"""

    name = models.CharField("名前", max_length=100)
    price = models.IntegerField("価格")
    quantity = models.IntegerField("数量")
    created_at = models.DateTimeField("登録日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    class Meta:
        db_table = "supply"

    def __str__(self):
        return self.name
