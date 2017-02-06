from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    # pub_date컬럼을 기준으로 내림차순 정렬한 결과를 latest_question_list 에 할당
    latest_question_list = Question.objects.order_by('-pub_date')
    # 돌려줄 문자열을 작성
    output = ', '.join([q.question_text for q in latest_question_list])

    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }

    # output2 = ''
    # for q in latest_question_list:
    #     output2 += q.question_text + ', '
    # output2 = output2[:2]
    return HttpResponse(template.render(context, request))
    # return HttpResponse(output)



def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def result(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
