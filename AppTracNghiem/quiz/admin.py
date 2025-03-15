from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):  # Hiển thị câu trả lời dạng bảng
    model = Answer
    extra = 4  # Tạo sẵn 4 ô trống để nhập câu trả lời

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'get_correct_answers')  # Hiển thị số câu đúng
    list_filter = ('answers__is_correct',)  # Bộ lọc theo câu trả lời đúng/sai
    search_fields = ('question_text',)  # Cho phép tìm kiếm câu hỏi
    inlines = [AnswerInline]  # Gộp chung câu hỏi & câu trả lời

    def get_correct_answers(self, obj):
        return ", ".join([answer.answer_text for answer in obj.answers.filter(is_correct=True)])
    get_correct_answers.short_description = "Câu trả lời đúng"

admin.site.register(Question, QuestionAdmin)
