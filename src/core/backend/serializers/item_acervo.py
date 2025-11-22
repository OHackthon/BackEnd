from rest_framework.serializers import ModelSerializer, SlugRelatedField

from core.backend.models import Item
from uploader.models import Image
from uploader.serializers import ImageSerializer

class ItemAcervoSerializer(ModelSerializer):
    imagem_attachment_key = SlugRelatedField(
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)
    class Meta:
        model = Item
        fields = '__all__'
        depth = 1