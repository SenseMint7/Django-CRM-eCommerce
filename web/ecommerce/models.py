# from django.db import models
from django.utils.html import format_html
from djongo import models


class ItemInfo(models.Model):
    """
    제품에 대한 정보
    """
    item_name = models.CharField('제품 이름', max_length=255)
    item_price = models.IntegerField('제품 가격')
    item_company = models.CharField('제품 회사', max_length=255)
    item_stock = models.IntegerField('제품 재고')
    item_image = models.ImageField('제품 이미지', upload_to="%Y/%m/%d")
    item_content = models.TextField('제품 설명')

    def image_(self):
        """
        제품 이미지(썸네일)
        """
        return format_html('<img src="/media/{0}" width="100" height="100" />'.format(self.item_image))

    class Meta:
        verbose_name_plural = "제품 정보"

    def __str__(self):
        return self.item_name

