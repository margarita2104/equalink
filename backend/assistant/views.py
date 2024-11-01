from rest_framework import generics, status
from rest_framework.response import Response

from .app import analyze_article_for_bias  # Import your analysis function
from .models import BiasAnalysis
from .serializers import BiasAnalysisSerializer


class BiasAnalysisCreateListView(generics.ListCreateAPIView):
    serializer_class = BiasAnalysisSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        article_text = serializer.validated_data.get('article_text')

        if article_text:
            # Call your analysis function and get the feedback
            combined_feedback = analyze_article_for_bias(article_text)

            # Save the analysis result with feedback
            serializer.save(
                article_text=article_text,
                combined_feedback=combined_feedback
            )
        else:
            return Response({"error": "Article text is required."}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        # Optionally filter by user if needed, or return all analyses
        return BiasAnalysis.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BiasAnalysisDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BiasAnalysisSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        # Optionally filter by user if needed, or return all analyses
        return BiasAnalysis.objects.all()

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        analysis_entry = self.get_object()
        self.perform_destroy(analysis_entry)
        return Response(status=status.HTTP_204_NO_CONTENT)
