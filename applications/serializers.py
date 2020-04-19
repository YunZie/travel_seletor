# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

# from chatting import documents as articles_documents
 
 
class WeatherSerializer(DocumentSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'body',
            'author',
            'created',
            'modified',
            'pub_date',
        )   

