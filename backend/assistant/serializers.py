from rest_framework import serializers
from .models import BiasAnalysis


class BiasAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = BiasAnalysis
        fields = ['id', 'article_text', 'combined_feedback', 'created_at']
        read_only_fields = ['id', 'combined_feedback', 'created_at']

    def validate_article_text(self, value):
        """
        Custom validation for article_text to ensure it's not empty.
        """
        if not value:
            raise serializers.ValidationError("Article text cannot be empty.")
        return value
