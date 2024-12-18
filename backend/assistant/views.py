import json

from rest_framework import generics, status
from rest_framework.response import Response

from .app import get_sambanova_response
from .models import BiasAnalysis
from .serializers import BiasAnalysisSerializer


class BiasAnalysisCreateListView(generics.ListCreateAPIView):
    serializer_class = BiasAnalysisSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        article_text = serializer.validated_data.get('article_text')

        if article_text:
            # Call the function that interacts with SambaNova and get the feedback
            sambanova_feedback = get_sambanova_response(article_text)

            # Save the analysis result with feedback
            serializer.save(
                article_text=article_text,
                combined_feedback=json.dumps(sambanova_feedback)  # Store feedback as a JSON string
            )
        else:
            return Response({"error": "Article text is required."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BiasAnalysisDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BiasAnalysisSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        return BiasAnalysis.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        analysis_entry = self.get_object()
        self.perform_destroy(analysis_entry)
        return Response(status=status.HTTP_204_NO_CONTENT)