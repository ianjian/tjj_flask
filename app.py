from flask import Flask, redirect, url_for, render_template, request

import flask_login as login

from wtforms import form, fields, validators
from werkzeug.security import generate_password_hash, check_password_hash

import flask_admin as admin
from flask_admin import helpers
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from flask_admin.form import FileUploadInput

from flask_ckeditor import CKEditor, CKEditorField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.event import listens_for

import time
import os
import os.path as op

import db_operation as dn

app = Flask(__name__)
db = SQLAlchemy(app)
ckeditor = CKEditor(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/db_tjj_flask'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:linkage@54321@localhost:3306/db_tjj_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SECRET_KEY'] = '123456'
app.config['FLASK_ADMIN_SWATCH'] = 'Lumen'

file_path = op.join(op.dirname(__file__), 'files')
try:
    os.mkdir(file_path)
except OSError:
    pass


class t_work(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )


# 领导介绍
class t_leader(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    name = db.Column(db.String(), )
    leader_title = db.Column(db.String(), )
    intro = db.Column(db.Text(), )


# 江西省情
class t_circumstances(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )


# 组织结构/机构设置
class t_organization(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )
    cate = db.Column(db.String())

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


# 专题聚焦
class t_topic(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )


class t_fund(db.Model):  # 财政资金
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class t_law(db.Model):  # 法律法规
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )


class t_policy(db.Model):  # 政策解读
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )


class t_tax(db.Model):  # 减税降费
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )


class t_file(db.Model):  # 规范性文件
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )
    file = db.Column(db.String(), )


@listens_for(t_file, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_jx_data(db.Model):  # 本省数据
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )
    file = db.Column(db.String(), )
    graph = db.Column(db.String(), )


@listens_for(t_jx_data, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_cn_data(db.Model):  # 全国数据
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )
    file = db.Column(db.String(), )
    graph = db.Column(db.String(), )


@listens_for(t_cn_data, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_global_data(db.Model):  # 国际数据
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )
    file = db.Column(db.String(), )
    graph = db.Column(db.String(), )


@listens_for(t_global_data, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_org_qualificaton(db.Model):  # 涉外机构资格认证
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    file = db.Column(db.String(), )
    datetime = db.Column(db.DateTime(), )
    cate = db.Column(db.String(), )


@listens_for(t_org_qualificaton, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_proj_exam(db.Model):  # 涉外调查项目审批
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    proj_exam_file = db.Column(db.String(), )
    datetime = db.Column(db.DateTime(), )
    cate = db.Column(db.String(), )


@listens_for(t_proj_exam, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_proj_manage(db.Model):  # 地方统计调查项目管理
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    proj_manage_file = db.Column(db.String(), )
    datetime = db.Column(db.DateTime(), )
    cate = db.Column(db.String(), )


@listens_for(t_proj_manage, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_system(db.Model):  # 统计制度
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    file = db.Column(db.String(), )  # path
    datetime = db.Column(db.DateTime(), )


@listens_for(t_system, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_jx_statistics(db.Model):  # 江西省统计公报
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    file = db.Column(db.String(), )
    datetime = db.Column(db.DateTime(), )


@listens_for(t_jx_statistics, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_jx_survey(db.Model):  # 江西省普查公报
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )
    file = db.Column(db.String(), )


@listens_for(t_jx_survey, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_cn_statistics(db.Model):  # 国家统计公报
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )
    file = db.Column(db.String(), )


@listens_for(t_cn_statistics, 'after_delete')
def del_file(mapper, connection, target):
    if target.path:
        try:
            os.remove(op.join(file_path, target.path))
        except OSError:
            pass


class t_interview(db.Model):  # 在线访谈
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )


class t_consult(db.Model):  # 在线咨询
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    account = db.Column(db.Integer, )
    is_encrypt = db.Column(db.Integer, )
    asker = db.Column(db.String(), )
    phone = db.Column(db.String(), )
    email = db.Column(db.String(), )
    theme = db.Column(db.String(), )
    question = db.Column(db.Text(), )
    ask_time = db.Column(db.Date(), )
    answer = db.Column(db.Text(), )
    ans_time = db.Column(db.Date(), )


class t_report_letter(db.Model):  # 举报信箱
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    account = db.Column(db.Integer, )
    is_encrypt = db.Column(db.Integer, )
    asker = db.Column(db.String(), )
    phone = db.Column(db.String(), )
    email = db.Column(db.String(), )
    theme = db.Column(db.String(), )
    question = db.Column(db.Text(), )
    ask_time = db.Column(db.Date(), )
    answer = db.Column(db.Text(), )
    ans_time = db.Column(db.Date(), )


class t_mail(db.Model):  # 领导信箱
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    account = db.Column(db.Integer, )
    is_encrypt = db.Column(db.Integer, )
    asker = db.Column(db.String(), )
    phone = db.Column(db.String(), )
    email = db.Column(db.String(), )
    theme = db.Column(db.String(), )
    question = db.Column(db.Text(), )
    ask_time = db.Column(db.Date(), )
    answer = db.Column(db.Text(), )
    ans_time = db.Column(db.Date(), )


class t_survey_theme(db.Model):
    theme_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    theme_title = db.Column(db.String(), )
    theme_start = db.Column(db.Date(), )
    theme_finish = db.Column(db.Date(), )


class t_survey_ques(db.Model):
    ques_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ques_title = db.Column(db.String(), )
    ques_theme_id = db.Column(db.Integer(), )


class t_survey_ans(db.Model):
    ans_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    ans_title = db.Column(db.String(), )
    ans_ques_id = db.Column(db.Integer(), )


class t_fqa(db.Model):  # 常见问题
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = db.Column(db.String(), )
    content = db.Column(db.Text(), )
    datetime = db.Column(db.DateTime(), )


class fileInput(FileUploadInput):
    FileUploadInput.data_template = ('<div>'
                                     ' <input style="border:0" %(text)s>&nbsp;&nbsp;&nbsp;&nbsp;'
                                     ' <input type="checkbox" name="%(marker)s">Delete</input>'
                                     '</div>'
                                     '<input %(file)s>')


admin_ = admin.Admin(app, name=u"统计局管理系统", template_mode="bootstrap3")




class add_ckeditor(ModelView):
    """
        加富文本
    """
    form_overrides = dict(
        content=CKEditorField,
    )
    create_template = 'edit.html'
    edit_template = 'edit.html'


class FileView(add_ckeditor):
    """
        加文件框
    """
    widget = fileInput

    column_labels = {
        'file': u'文件路径',
        'id': u'序号',
        'title': u'标题',
        'content': u'正文',
        'datetime': u'发布时间',
        'leader_title': u'领导岗位',
        'account': u'查询编号',
        'is_encrypt': u'是否加密',
        'asker': u'提问者',
        'phone': u'预留手机号',
        'email': u'预留邮箱',
        'theme': u'提问主题',
        'question': u'提问正文',
        'ask_time': u'提问时间',
        'answer': u'回答',
        'ans_time': u'回答时间',
        'graph': u'图表',
    }

    form_overrides = dict(content=CKEditorField, file=FileUploadField)

    form_args = {
        'statistic_file': {
            'base_path': file_path,
            'allow_overwrite': False
        },
    }

admin_.add_views(  # 政务公开页面的管理
    FileView(t_work, db.session, name=u"工作动态", category=u"政务公开", endpoint="work"),
    FileView(t_circumstances, db.session, name=u"江西省情", category=u"政务公开", endpoint="circumstances"),
    FileView(t_leader, db.session, name=u"领导介绍", category=u"政务公开", endpoint="leader"),
    FileView(t_organization, db.session, name=u"组织结构", category=u"政务公开", endpoint="organazation"),
    #     add_ckeditor(t_topic, db.session, name=u"专题聚焦", category=u"政务公开", endpoint="topic"),
    FileView(t_fund, db.session, name=u"财政资金", category=u"政务公开", endpoint="fund"),
    FileView(t_law, db.session, name=u"法律法规", category=u"政务公开", endpoint="law"),
    FileView(t_policy, db.session, name=u"政策解读", category=u"政务公开", endpoint="policy"),
    FileView(t_tax, db.session, name=u"减税降费", category=u"政务公开", endpoint="tax"),
)

admin_.add_views(  # 统计数据页面的管理
    FileView(t_jx_data, db.session, name=u"本省数据", category=u"统计数据", endpoint="jx_data"),  # 新闻、文件、图表
    FileView(t_cn_data, db.session, name=u"全国数据", category=u"统计数据", endpoint="cn_data"),
    FileView(t_global_data, db.session, name=u"国际数据", category=u"统计数据", endpoint="global_data"),
    FileView(t_system, db.session, name=u"统计制度", category=u"统计数据", endpoint="system"),
    FileView(t_jx_statistics, db.session, name=u"江西省统计公报", category=u"统计数据", endpoint="jx_statistics"),  # pdf
    FileView(t_jx_survey, db.session, name=u"江西省普查公报", category=u"统计数据", endpoint="jx_survey"),  # pdf
    FileView(t_cn_statistics, db.session, name=u"国家统计公报", category=u"统计数据", endpoint="cn_statistics"),  # pdf
)

admin_.add_views(  # 网上办事页面的管理
    FileView(t_org_qualificaton, db.session, name=u"涉外调查机构资格认证", category=u"网上办事", endpoint="org_qualificaton"),  #
    FileView(t_proj_exam, db.session, name=u"涉外调查项目审批", category=u"网上办事", endpoint="proj_exam"),
    FileView(t_proj_manage, db.session, name=u"地方统计调查项目管理", category=u"网上办事", endpoint="proj_manage"),
)

admin_.add_views(  # 互动交流页面的管理
    FileView(t_interview, db.session, name=u"在线访谈", category=u"互动交流", endpoint="interview"),  #
    FileView(t_consult, db.session, name=u"在线咨询", category=u"互动交流", endpoint="consult"),
    FileView(t_fqa, db.session, name=u"常见问题", category=u"互动交流", endpoint="fqa"),
    FileView(t_mail, db.session, name=u"领导信箱", category=u"互动交流", endpoint="mail"),
    #     add_ckeditor(t_survey_theme, db.session, name=u"网上调查", category=u"互动交流", endpoint="tax"),  # 棘手啊
    #     add_ckeditor(t_survey_ques, db.session, name=u"网上调查", category=u"互动交流", endpoint="tax"),  # 棘手啊
    #     add_ckeditor(t_survey_ans, db.session, name=u"网上调查", category=u"互动交流", endpoint="tax"),  # 棘手啊
)


@app.route('/consult_list/')
def consult_list():
    consult_list = dn.get_all_consult()
    return render_template('consult_list.html', consult_list=consult_list)


@app.route('/consult_show/<id>')
def consult_show(id):
    con = dn.get_1_consult(id)
    return render_template('consult_show.html', con=con)


@app.route('/survey_theme/')
def survey_theme():
    theme = dn.get_all_theme()
    return render_template('survey_theme.html', theme=theme)


@app.route('/data/<cate>')
def data(cate):
    if cate == 'jx':
        return render_template('')
    elif cate == 'cn':
        return render_template('')
    elif cate == 'global':
        return render_template('')


@app.route('/fqa/')
def fqa():
    fqa = dn.get_all_fqa()
    return render_template('fqa.html', fqa=fqa)


@app.route('/interview_list/')
def interview_list():
    interview = dn.get_all_interview()
    return render_template("interview_list.html", interview=interview)


@app.route('/')
def home():
    work = dn.get_five_work()
    leader = dn.get_eight_leader()
    fund = dn.get_three_fund()
    fqa = dn.get_ten_fqa()
    work12 = dn.get_12_work()
    theme3 = dn.get_3_theme()
    int9 = dn.get_9_int()
    jx_data5 = dn.get_5_jx_data()
    system5 = dn.get_5_system()
    consult4 = dn.get_4_consult()
    return render_template("home.html", work=work, fund=fund, leader=leader, fqa=fqa, work12=work12, theme3=theme3,
                           int9=int9, jx_data5=jx_data5, system5=system5, consult4=consult4)


@app.route('/law_comprehension/<cate>', methods=['get', 'post'])
def law_comprehension(cate):
    if cate == "file":  # 规范性文件
        file = dn.get_all_file()
        return render_template("file_list.html", file=file)
    elif cate == "law":  # 相关法律法规
        law = dn.get_all_law()
        return render_template("law_list.html", law=law)
    elif cate == "policy":  # 政策解读
        policy = dn.get_all_policy()
        return render_template("policy_list.html", policy=policy)


@app.route("/main_responsibility/")
def main_responsibility():
    return render_template("main_responsibility.html")


@app.route("/work_list/")
def work_list():
    work = dn.get_all_work()
    return render_template("work_list.html", work=work)


@app.route("/organization_list/")
def organization_list():
    query1 = t_organization.query.filter_by(org_cate="行政单位")
    cate1 = t_organization.to_json(query1)
    query2 = t_organization.query.filter_by(org_cate="事业单位")
    cate2 = t_organization.to_json(query2)
    return render_template("organization_list.html", cate1=cate1, cate2=cate2)


@app.route("/leader_intro/")
def leader_intro():
    leader = dn.get_leader_intro()
    return render_template("leader_intro.html", leader=leader)


@app.route("/fund_list/")
def fund_list():
    query = t_fund.query.all()
    fund = t_fund.to_json(query)
    return render_template('fund_list.html', fund=fund)


@app.route('/consult/')
def consult():
    return render_template('consult.html')


@app.route('/report/')
def report():
    return render_template('report_letter.html')


@app.route('/mail/')
def mail():
    return render_template('mail.html')


@app.route('/news/<cate>/<data>', methods=['get', 'post'])
def news(cate, data):
    return_data = {}
    print(cate, data)
    if cate == "circumstance":
        return_data = dn.get_circumstances(data)
    elif cate == "work":
        return_data = dn.get_one_work(data)
    elif cate == 'organization':
        return_data = dn.get_one_organization(data)
    elif cate == 'fqa':
        return_data = dn.get_one_fqa(data)
    elif cate == 'interview':
        return_data = dn.get_1_interview(data)
    return render_template("news.html", data=return_data)


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5002,
    )
