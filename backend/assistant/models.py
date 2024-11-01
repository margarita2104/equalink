from django.db import models


class BiasAnalysis(models.Model):
    article_text = models.TextField(blank=True, null=True, help_text="The article text submitted for bias analysis.")
    groq_feedback = models.TextField(blank=True, null=True, help_text="Feedback provided by the Groq API.")
    sambanova_feedback = models.TextField(blank=True, null=True, help_text="Feedback provided by the SambaNova API.")
    combined_feedback = models.TextField(blank=True, null=True, help_text="Consolidated feedback from both APIs.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bias Analysis | Created at: {self.created_at}"
