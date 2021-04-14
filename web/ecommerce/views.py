from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from elasticsearch import Elasticsearch

from drf_yasg.utils import swagger_auto_schema

from .serializers import IteminfoSerializer


class SearchView(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(
        description='Ecommerce Iteminfo',
        request_body=IteminfoSerializer,
        tags=['Iteminfo'],
        operation_description='제품 정보'
    )
    def get(self, request):
        es = Elasticsearch('http://elastic:changeme@localhost:9200')

        search_word = request.GET.get('search')

        if not search_word:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={'message': 'search word param is missing'})

        docs = es.search(index='test',
                         doc_type='dictionary_datas',
                         body={
                             "query": {
                                 "multi_match": {
                                     "query": search_word,
                                     "fields": ["item_name", "item_stock"]
                                 }
                             }
                         })
        data_list = docs['hits']

        return Response(data_list)
