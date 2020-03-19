import time
import app


def get_circumstances(title):
    lst = {}
    cir = app.t_circumstances.query.filter_by(title=title)  # list
    for i in cir:
        lst = {
            'id': i.id,
            'title': i.title,
            'content': i.content,
            'datetime': i.datetime,
        }
    return lst


def get_all_work():
    work = []
    query = app.t_work.query.all()
    for i in query:
        temp = {"id": i.id, "title": i.title, "content": i.content, "datetime": i.datetime}
        work.append(temp)
    return work


def get_all_fqa():
    fqa = []
    query = app.t_fqa.query.all()
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.content, 'datetime': i.datetime}
        fqa.append(temp)
    return fqa


def get_all_interview():
    interview = []
    query = app.t_interview.query.all()
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.content, 'datetime': str(i.datetime)[: 10]}
        interview.append(temp)
    return interview


def get_all_consult():
    lst = []
    query = app.t_consult.query.all()
    for i in query:
        temp = {
            'id': i.id,
            'theme': i.theme,
            'answer': i.answer,
            'ask_time': i.ask_time,
        }
        lst.append(temp)
    return lst


def get_5_jx_data():
    lst = []
    query = app.t_jx_data.query.all()[:5]
    for i in query:
        temp = {
            'id': i.id,
            'title': i.title,
            'content': i.content,
            'datetime': i.datetime,
            'file': i.data_file,
            'img': i.graph,
        }
        lst.append(temp)
    return lst


def get_5_system():
    lst = []
    query = app.t_system.query.all()[:5]
    for i in query:
        temp = {
            'id': i.id,
            'title': i.title,
            'content': i.content,
            'datetime': i.datetime,
            # 'file': i.jx_data_file,
            # 'img': i.jx_data_image,
        }
        lst.append(temp)
    return lst


def get_one_work(id=None):
    lst = []
    query = app.t_work.query.filter_by(id=id)
    for i in query:
        lst = {'id': i.id, 'title': i.title, 'content': i.content, 'datetime': i.datetime, }
    return lst


def get_five_work():
    lst = []
    query = app.t_work.query.all()[0: 5]
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.content, 'datetime': i.datetime, }
        lst.append(temp)
    return lst


def get_work_list():
    lst = []
    query = app.t_work.query.all()
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.content, 'datetime': i.datetime, }
        lst.append(temp)
    return lst


def get_three_fund():
    lst = []
    query = app.t_fund.query.all()[: 3]
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.content, 'datetime': i.datetime, }
        lst.append(temp)
    return lst


def get_one_organization(data):
    lst = {}
    query = app.t_organization.query.filter_by(id=data)
    for i in query:
        lst = {'id': i.id, 'title': i.title, 'content': i.content}
    return lst


def get_eight_leader():
    lst = []
    query = app.t_leader.query.all()[0: 8]
    for i in query:
        temp = {'id': i.id, 'name': i.name, 'title': i.leader_title, 'content': i.intro,
                'img': i.leader_image}
        lst.append(temp)
    return lst


def get_ten_fqa():
    fqa = []
    query = app.t_fqa.query.all()[:10]
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.fqa_content, 'datetime': str(i.fqa_datetime)[: 10]}
        fqa.append(temp)
    return fqa


def get_12_work():
    work12 = []
    query = app.t_work.query.all()[:12]
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.content,
                'datetime': str(i.work_datetime)[: 10]}
        work12.append(temp)
    return work12


def get_3_theme():
    theme3 = []
    query = app.t_survey_theme.query.all()[:3]
    for i in query:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if current_time < str(i.theme_finish):
            temp = {'id': i.theme_id, 'title': i.theme_title, 'start': i.theme_start, 'finish': i.theme_finish,
                    'state': '进行中'}
        else:
            temp = {'id': i.theme_id, 'title': i.theme_title, 'start': i.theme_start, 'finish': i.theme_finish,
                    'state': '已结束'}
        theme3.append(temp)
    return theme3


def get_all_theme():
    theme = []
    query = app.t_survey_theme.query.all()[:3]
    for i in query:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if current_time < str(i.theme_finish):
            temp = {'id': i.theme_id, 'title': i.theme_title, 'start': i.theme_start, 'finish': i.theme_finish,
                    'state': '进行中'}
        else:
            temp = {'id': i.theme_id, 'title': i.theme_title, 'start': i.theme_start, 'finish': i.theme_finish,
                    'state': '已结束'}
        theme.append(temp)
    return theme


def get_leader_intro():
    query = app.t_leader.query.all()
    leader = []
    for i in query:
        temp = {"id": i.id, "name": i.name, "title": i.leader_title, "intro": i.intro}
        leader.append(temp)
    return leader

def get_9_int():
    int9 = []
    query = app.t_interview.query.all()[:9]
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.content,
                'datetime': str(i.int_datetime)[: 10]}
        int9.append(temp)
    return int9


def get_all_file():
    int9 = []
    query = app.t_file.query.all()
    for i in query:
        temp = {'id': i.file_id, 'title': i.file_title, 'content': i.file_content,
                'datetime': str(i.file_datetime)[: 10], 'path': i.file_path}
        int9.append(temp)
    return int9


def get_all_law():
    int9 = []
    query = app.t_law.query.all()
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.int_content,
                'datetime': str(i.int_datetime)[: 10], 'path': i.law_path}
        int9.append(temp)
    return int9


def get_all_policy():
    int9 = []
    query = app.t_policy.query.all()
    for i in query:
        temp = {'id': i.id, 'title': i.title, 'content': i.content,
                'datetime': str(i.int_datetime)[: 10], 'path': i.policy_path}
        int9.append(temp)
    return int9


def get_one_fqa(id):
    lst = {}
    query = app.t_fqa.query.filter_by(id=id)
    for i in query:
        lst = {'id': i.id, 'title': i.title, 'content': i.content, 'datetime': i.datetime}
    return lst


def get_1_consult(id):
    lst = {}
    query = app.t_consult.query.filter_by(id=id)
    for i in query:
        lst = {'id': i.id, 'asker': i.asker, 'ask_time': i.ask_time,
               'question': i.question, 'answer': i.answer, 'ans_time': i.ans_time}
    return lst


def get_4_consult():
    lst = []
    query = app.t_consult.query.all()[:4]
    for i in query:
        temp = {'id': i.id, 'ask_time': i.ask_time, 'question': i.question,
                'answer': i.answer}
        lst.append(temp)
    return lst


def get_1_interview(data):
    lst = {}
    query = app.t_interview.query.filter_by(id=data)
    for i in query:
        lst = {'id': i.id, 'title': i.title, 'content': i.content, 'datetime': i.datetime}
    return lst
