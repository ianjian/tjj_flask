import time
import app
from app import db


def get_specific_work(key):
    cir = app.t_work.query.filter(app.t_work.title.like("%" + key + "%"))
    lst = app.t_work.to_json(cir)
    return lst


def get_circumstances(title):
    cir = app.t_circumstances.query.filter_by(title=title)  # list
    lst = app.t_circumstances.to_json(cir)
    return lst


def get_all_work():
    query = app.t_work.query.all()
    work = app.t_work.to_json(query)
    return work


def get_all_fqa():
    query = app.t_fqa.query.all()
    fqa = app.t_fqa.to_json(query)
    return fqa


def get_all_interview():
    query = app.t_interview.query.all()
    interview = app.t_interview.to_json(query)
    return interview


def get_all_consult():
    lst = []
    query = app.t_consult.query.all()
    lst = app.t_consult.to_json(query)
    return lst


def get_all_report():
    query = app.t_report_letter.query.all()
    lst = app.t_report_letter.to_json(query)
    return lst


def get_all_mail():
    query = app.t_mail.query.all()
    lst = app.t_mail.to_json(query)
    return lst


def get_5_jx_data():
    query = app.t_jx_data.query.all()[:5]
    lst = app.t_jx_data.to_json(query)
    return lst


def get_5_system():
    query = app.t_system.query.all()[:5]
    lst = app.t_system.to_json(query)
    return lst


def get_9_system():
    query = app.t_system.query.all()[:9]
    lst = app.t_system.to_json(query)
    return lst


def get_one_work(id=None):
    query = app.t_work.query.filter_by(id=id)
    lst = app.t_work.to_json(query)
    return lst


def get_five_work():
    query = app.t_work.query.all()[0: 5]
    lst = app.t_work.to_json(query)
    return lst


def get_all_topic():
    query = app.t_topic.query.all()
    lst = app.t_topic.to_json(query)
    return lst


def get_all_tax():
    query = app.t_tax.query.all()
    lst = app.t_tax.to_json(query)
    return lst


def get_work_list():
    query = app.t_work.query.all()
    lst = app.t_work.to_json(query)
    return lst


def get_three_fund():
    query = app.t_fund.query.all()[: 3]
    lst = app.t_fund.to_json(query)
    return lst


def get_one_organization(data):
    query = app.t_organization.query.filter_by(id=data)
    lst = app.t_organization.to_json(query)
    return lst


def get_eight_leader():
    query = app.t_leader.query.all()[0: 8]
    lst = app.t_leader.to_json(query)
    return lst


def get_ten_fqa():
    query = app.t_fqa.query.all()[:10]
    lst = app.t_fqa.to_json(query)
    return lst


def get_12_work():
    query = app.t_work.query.all()[:12]
    lst = app.t_work.to_json(query)
    return lst


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
    lst = app.t_leader.to_json(query)
    return lst


def get_9_int():
    query = app.t_interview.query.all()[:9]
    lst = app.t_interview.to_json(query)
    return lst


def get_qua_all_relatives():  # 涉外调查机构资格认证
    query = app.t_org_qualification.query.filter_by(cate='有关文件')
    lst = app.t_org_qualification.to_json(query)
    return lst

def get_qua_all_procedure():  # 涉外调查机构资格认证
    query = app.t_org_qualification.query.filter_by(cate='网上审批')
    lst = app.t_org_qualification.to_json(query)
    return lst

def get_qua_all_table():  # 涉外调查机构资格认证
    query = app.t_org_qualification.query.filter_by(cate='表格下载')
    lst = app.t_org_qualification.to_json(query)
    return lst


def get_qua_all_state():  # 涉外调查机构资格认证
    query = app.t_org_qualification.query.filter_by(cate='状态查询')
    lst = app.t_org_qualification.to_json(query)
    return lst

def get_qua_all_notice():  # 涉外调查机构资格认证
    query = app.t_org_qualification.query.filter_by(cate='审批公告')
    lst = app.t_org_qualification.to_json(query)
    return lst

def get_all_qua():  # 涉外调查机构资格认证
    query = app.t_org_qualification.query.all()
    lst = app.t_org_qualification.to_json(query)
    return lst


def get_exam_all_relatives():  # 涉外调查机构资格认证
    query = app.t_proj_exam.query.filter_by(cate='有关文件')
    lst = app.t_proj_exam.to_json(query)
    return lst

def get_exam_all_procedure():  # 涉外调查机构资格认证
    query = app.t_proj_exam.query.filter_by(cate='网上审批')
    lst = app.t_proj_exam.to_json(query)
    return lst

def get_exam_all_table():  # 涉外调查机构资格认证
    query = app.t_proj_exam.query.filter_by(cate='表格下载')
    lst = app.t_proj_exam.to_json(query)
    return lst


def get_exam_all_state():  # 涉外调查机构资格认证
    query = app.t_proj_exam.query.filter_by(cate='状态查询')
    lst = app.t_proj_exam.to_json(query)
    return lst

def get_exam_all_notice():  # 涉外调查机构资格认证
    query = app.t_proj_exam.query.filter_by(cate='审批公告')
    lst = app.t_proj_exam.to_json(query)
    return lst

def get_all_exam():  # 涉外调查机构资格认证
    query = app.t_proj_exam.query.all()
    lst = app.t_proj_exam.to_json(query)
    return lst

def get_all_relatives():  # 地方统计调查项目管理
    query = app.t_proj_manage.query.filter_by(cate='有关文件')
    lst = app.t_proj_manage.to_json(query)
    return lst


def get_all_procedure():
    query = app.t_proj_manage.query.filter_by(cate='审批程序')
    lst = app.t_proj_manage.to_json(query)
    return lst


def get_all_table():
    query = app.t_proj_manage.query.filter_by(cate='表格下载')
    lst = app.t_proj_manage.to_json(query)
    return lst


def get_all_notice():
    query = app.t_proj_manage.query.filter_by(cate='审批公告')
    lst = app.t_proj_manage.to_json(query)
    return lst

def get_all_system_download():  # 统计制度下载
    query = app.t_file_download.query.filter_by(cate='统计制度下载')
    lst = app.t_file_download.to_json(query)
    return lst

def get_all_report_download():  # 统计报表下载
    query = app.t_file_download.query.filter_by(cate='统计报表下载')
    lst = app.t_file_download.to_json(query)
    return lst


def get_all_sys():
    query = app.t_system.query.all()
    lst = app.t_system.to_json(query)
    return lst


def get_1_sys(id):
    query = app.t_system.query.filter_by(id=id)
    lst = app.t_system.to_json(query)
    return lst


def add_2_mail(account, is_encrypt, asker, phone, email, theme, question):
    add = app.t_mail(
        account=account,
        is_encrypt=is_encrypt,
        asker=asker,
        phone=phone,
        email=email,
        theme=theme,
        question=question,
        ask_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    )
    db.session.add(add)
    db.session.commit()


def get_all_statistics():
    query = app.t_jx_statistics.query.all()
    lst = app.t_jx_statistics.to_json(query)
    return lst


def get_all_jx_data():
    query = app.t_jx_data.query.all()
    lst = app.t_jx_data.to_json(query)
    return lst


def get_all_cn_data():
    query = app.t_cn_data.query.all()
    lst = app.t_cn_data.to_json(query)
    return lst


def get_all_global_data():
    query = app.t_global_data.query.all()
    lst = app.t_global_data.to_json(query)
    return lst


def get_all_file():
    query = app.t_file.query.all()
    lst = app.t_file.to_json(query)
    return lst


def get_all_law():
    query = app.t_law.query.all()
    lst = app.t_law.to_json(query)
    return lst


def get_all_policy():
    query = app.t_policy.query.all()
    lst = app.t_policy.to_json(query)
    return lst


def get_one_fqa(id):
    query = app.t_fqa.query.filter_by(id=id)
    lst = app.t_fqa.to_json(query)
    return lst


def get_1_consult(id):
    query = app.t_consult.query.filter_by(id=id)
    lst = app.t_consult.to_json(query)
    return lst


def get_1_mail(id):
    query = app.t_mail.query.filter_by(id=id)
    lst = app.t_mail.to_json(query)
    return lst


def get_1_report_letter(id):
    query = app.t_report_letter.query.filter_by(id=id)
    lst = app.t_report_letter.to_json(query)
    return lst


def get_4_consult():
    query = app.t_consult.query.all()[:4]
    lst = app.t_consult.to_json(query)
    return lst


def get_1_interview(data):
    query = app.t_interview.query.filter_by(id=data)
    lst = app.t_interview.to_json(query)
    return lst


def add_2_consult(account, is_encrypt, asker, phone, email, theme, question):
    add = app.t_consult(
        account=account,
        is_encrypt=is_encrypt,
        asker=asker,
        phone=phone,
        email=email,
        theme=theme,
        question=question,
        ask_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    )
    db.session.add(add)
    db.session.commit()


def add_2_report_letter(account, is_encrypt, asker, phone, email, theme, question):
    add = app.t_report_letter(
        account=account,
        is_encrypt=is_encrypt,
        asker=asker,
        phone=phone,
        email=email,
        theme=theme,
        question=question,
        ask_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
    )
    db.session.add(add)
    db.session.commit()


def get_5_qua():
    query = app.t_org_qualification.query.all()[:5]
    lst = app.t_org_qualification.to_json(query)
    return lst


def get_5_qua_tab():
    lst = []
    query = app.t_org_qualification.query.filter_by(cate=u'表格下载')[:5]
    lst = app.t_org_qualification.to_json(query)
    return lst


def get_5_qua_exam():
    query = app.t_org_qualification.query.filter_by(cate=u'网上审批')[:5]
    lst = app.t_org_qualification.to_json(query)
    return lst


def get_5_qua_state():
    query = app.t_org_qualification.query.filter_by(cate=u'状态查询')[:5]
    lst = app.t_org_qualification.to_json(query)
    return lst


def get_5_qua_real():
    query = app.t_org_qualification.query.filter_by(cate=u'有关文件')[:5]
    lst = app.t_org_qualification.to_json(query)
    return lst


def get_5_qua_noti():
    query = app.t_org_qualification.query.filter_by(cate=u'审批公告')[:5]
    lst = app.t_org_qualification.to_json(query)
    return lst


def get_5_exam():
    query = app.t_proj_exam.query.all()[:5]
    lst = app.t_proj_exam.to_json(query)
    return lst


def get_5_exam_table():
    query = app.t_proj_exam.query.filter_by(cate=u'表格下载')[:5]
    lst = app.t_proj_exam.to_json(query)
    return lst


def get_5_exam_exam():
    query = app.t_proj_exam.query.filter_by(cate=u'网上审批')[:5]
    lst = app.t_proj_exam.to_json(query)
    return lst


def get_5_exam_state():
    query = app.t_proj_exam.query.filter_by(cate=u'状态查询')[:5]
    lst = app.t_proj_exam.to_json(query)
    return lst


def get_5_exam_real():
    query = app.t_proj_exam.query.filter_by(cate=u'有关文件')[:5]
    lst = app.t_proj_exam.to_json(query)
    return lst


def get_5_exam_noti():
    query = app.t_proj_exam.query.filter_by(cate=u'审批公告')[:5]
    lst = app.t_proj_exam.to_json(query)
    return lst


def get_5_mana():
    query = app.t_proj_manage.query.all()[:5]
    lst = app.t_proj_manage.to_json(query)
    return lst


def get_5_mana_table():
    query = app.t_proj_manage.query.filter_by(cate=u'表格下载')[:5]
    lst = app.t_proj_manage.to_json(query)
    return lst


def get_5_mana_exam():
    query = app.t_proj_manage.query.filter_by(cate=u'网上审批')[:5]
    lst = app.t_proj_manage.to_json(query)
    return lst


def get_5_mana_state():
    query = app.t_proj_manage.query.filter_by(cate=u'状态查询')[:5]
    lst = app.t_proj_manage.to_json(query)
    return lst


def get_5_mana_real():
    query = app.t_proj_manage.query.filter_by(cate=u'有关文件')[:5]
    lst = app.t_proj_manage.to_json(query)
    return lst


def get_5_mana_noti():
    query = app.t_proj_manage.query.filter_by(cate=u'审批公告')[:5]
    lst = app.t_proj_manage.to_json(query)
    return lst


def get_1_jx_data(id):
    query = app.t_jx_data.query.filter_by(id=id)
    temp = app.t_jx_data.to_json(query)
    return temp


def get_1_cn_data(id):
    query = app.t_cn_data.query.filter_by(id=id)
    temp = app.t_cn_data.to_json(query)
    return temp


def get_1_global_data(id):
    query = app.t_global_data.query.filter_by(id=id)
    temp = app.t_global_data.to_json(query)
    return temp


def get_1_topic(id):
    query = app.t_topic.query.filter_by(id=id)
    temp = app.t_topic.to_json(query)
    return temp


def get_1_fund(id):
    query = app.t_fund.query.filter_by(id=id)
    temp = app.t_fund.to_json(query)
    return temp


def get_1_tax(id):
    query = app.t_tax.query.filter_by(id=id)
    temp = app.t_tax.to_json(query)
    return temp


def get_1_jx_sta(id):
    query = app.t_jx_data.query.filter_by(id=id)
    temp = app.t_jx_data.to_json(query)
    return temp


def get_1_jx_sur(id):
    query = app.t_jx_survey.query.filter_by(id=id)
    temp = app.t_jx_survey.to_json(query)
    return temp


def get_1_cn_sta(id):
    query = app.t_cn_data.query.filter_by(id=id)
    temp = app.t_cn_data.to_json(query)
    return temp


def get_1_file(id):
    query = app.t_file.query.filter_by(id=id)
    temp = app.t_file.to_json(query)
    return temp


def get_1_law(id):
    query = app.t_law.query.filter_by(id=id)
    temp = app.t_law.to_json(query)
    return temp

def get_1_policy(id):
    query = app.t_policy.query.filter_by(id=id)
    temp = app.t_policy.to_json(query)
    return temp


def get_1_qualification(id):
    query = app.t_org_qualification.query.filter_by(id=id)
    temp = app.t_org_qualification.to_json(query)
    return temp


def get_1_exam(id):
    query = app.t_proj_exam.query.filter_by(id=id)
    temp = app.t_proj_exam.to_json(query)
    return temp


def get_1_manage(id):
    query = app.t_proj_manage.query.filter_by(id=id)
    temp = app.t_proj_manage.to_json(query)
    return temp

def get_all_jx_statistics():
    query = app.t_jx_statistics.query.all()
    temp = app.t_jx_statistics.to_json(query)
    return temp


def get_all_jx_survey():
    query = app.t_jx_survey.query.all()
    temp = app.t_jx_survey.to_json(query)
    return temp


def get_all_cn_statistics():
    query = app.t_cn_statistics.query.all()
    temp = app.t_cn_statistics.to_json(query)
    return temp