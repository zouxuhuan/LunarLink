# Generated by Django 3.2.1 on 2023-08-28 14:58

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.CharField(help_text='创建人', max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(help_text='更新人', max_length=20, null=True, verbose_name='更新人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=100, verbose_name='用例名称')),
                ('relation', models.IntegerField(verbose_name='节点id')),
                ('length', models.IntegerField(verbose_name='API个数')),
                ('tag', models.IntegerField(choices=[(1, '冒烟用例'), (2, '集成用例'), (3, '监控用例'), (4, '核心用例')], default=2, verbose_name='用例标签')),
            ],
            options={
                'verbose_name': '用例信息',
                'db_table': 'case',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.CharField(help_text='创建人', max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(help_text='更新人', max_length=20, null=True, verbose_name='更新人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(help_text='项目名称', max_length=100, verbose_name='项目名称')),
                ('desc', models.CharField(help_text='简要介绍', max_length=100, verbose_name='简要介绍')),
                ('responsible', models.CharField(help_text='负责人', max_length=20, verbose_name='负责人')),
                ('yapi_base_url', models.CharField(blank=True, default='', help_text='yapi的openapi url', max_length=100, verbose_name='yapi的openapi url')),
                ('yapi_openapi_token', models.CharField(blank=True, default='', help_text='yapi openapi的token', max_length=128, verbose_name='yapi openapi的token')),
                ('jira_project_key', models.CharField(blank=True, default='', help_text='jira项目key', max_length=30, verbose_name='jira项目key')),
                ('jira_bearer_token', models.CharField(blank=True, default='', help_text='jira bearer_token', max_length=45, verbose_name='jira bearer_token')),
            ],
            options={
                'verbose_name': '项目信息',
                'verbose_name_plural': '项目信息',
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.CharField(help_text='创建人', max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(help_text='更新人', max_length=20, null=True, verbose_name='更新人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=100, verbose_name='报告名称')),
                ('type', models.IntegerField(choices=[(1, '调试'), (2, '异步'), (3, '定时'), (4, '部署')], verbose_name='报告类型')),
                ('status', models.BooleanField(blank=True, choices=[(0, '失败'), (1, '成功')], verbose_name='报告状态')),
                ('summary', models.TextField(verbose_name='报告基础信息')),
                ('ci_metadata', jsonfield.fields.JSONField(default=dict)),
                ('ci_project_id', models.IntegerField(db_index=True, default=0, null=True, verbose_name='gitlab的项目id')),
                ('ci_job_id', models.CharField(db_index=True, default=None, max_length=15, null=True, unique=True, verbose_name='gitlab的项目id')),
                ('project', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.project')),
            ],
            options={
                'verbose_name': '测试报告',
                'db_table': 'report',
            },
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(db_index=True, max_length=100, verbose_name='访问url的用户名')),
                ('ip', models.CharField(db_index=True, max_length=20, verbose_name='用户的ip')),
                ('project', models.CharField(db_index=True, default=0, max_length=4, verbose_name='项目id')),
                ('url', models.CharField(db_index=True, max_length=255, verbose_name='被访问的url')),
                ('path', models.CharField(db_index=True, default='', max_length=100, verbose_name='被访问的接口路径')),
                ('request_params', models.CharField(db_index=True, default='', max_length=255, verbose_name='请求参数')),
                ('request_method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('PATCH', 'PATCH'), ('DELETE', 'DELETE'), ('OPTION', 'OPTION')], db_index=True, max_length=7, verbose_name='请求方法')),
                ('request_body', models.TextField(verbose_name='请求体')),
                ('create_time', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='创建时间')),
            ],
            options={
                'db_table': 'visit',
            },
        ),
        migrations.CreateModel(
            name='Variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.CharField(help_text='创建人', max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(help_text='更新人', max_length=20, null=True, verbose_name='更新人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('key', models.CharField(max_length=100, verbose_name='变量名')),
                ('value', models.CharField(max_length=1024, verbose_name='变量值')),
                ('description', models.CharField(max_length=100, null=True, verbose_name='全局变量描述')),
                ('project', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.project')),
            ],
            options={
                'verbose_name': '全局变量',
                'db_table': 'variables',
            },
        ),
        migrations.CreateModel(
            name='ReportDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_detail', models.TextField(verbose_name='报告详细信息')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('report', models.OneToOneField(db_constraint=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.report')),
            ],
            options={
                'verbose_name': '测试报告详情',
                'db_table': 'report_detail',
            },
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tree', models.TextField(default=[], verbose_name='结构主体')),
                ('type', models.IntegerField(default=1, verbose_name='树类型')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('project', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.project')),
            ],
            options={
                'verbose_name': '树形结构关系',
                'db_table': 'relation',
            },
        ),
        migrations.CreateModel(
            name='HostIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.CharField(help_text='创建人', max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(help_text='更新人', max_length=20, null=True, verbose_name='更新人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=100, verbose_name='host名称')),
                ('value', models.TextField(verbose_name='值')),
                ('project', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.project')),
            ],
            options={
                'verbose_name': 'HOST配置',
                'db_table': 'host_ip',
            },
        ),
        migrations.CreateModel(
            name='Debugtalk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.CharField(help_text='创建人', max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(help_text='更新人', max_length=20, null=True, verbose_name='更新人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('code', models.TextField(default='# write you code', help_text='python代码', verbose_name='python代码')),
                ('project', models.OneToOneField(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.project')),
            ],
            options={
                'verbose_name': '驱动库',
                'db_table': 'debugtalk',
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.CharField(help_text='创建人', max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(help_text='更新人', max_length=20, null=True, verbose_name='更新人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=100, verbose_name='环境名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('base_url', models.CharField(max_length=100, verbose_name='请求地址')),
                ('is_default', models.BooleanField(default=False, verbose_name='默认配置')),
                ('project', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.project')),
            ],
            options={
                'verbose_name': '环境信息',
                'db_table': 'config',
            },
        ),
        migrations.CreateModel(
            name='CaseStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.CharField(help_text='创建人', max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(help_text='更新人', max_length=20, null=True, verbose_name='更新人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(max_length=100, verbose_name='用例名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('url', models.CharField(max_length=255, verbose_name='请求地址')),
                ('method', models.CharField(max_length=10, verbose_name='请求方式')),
                ('step', models.IntegerField(verbose_name='顺序')),
                ('source_api_id', models.IntegerField(verbose_name='api来源')),
                ('case', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.case')),
            ],
            options={
                'verbose_name': '用例信息 Step',
                'db_table': 'case_step',
            },
        ),
        migrations.AddField(
            model_name='case',
            name='project',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.project'),
        ),
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.CharField(help_text='创建人', max_length=20, null=True, verbose_name='创建人')),
                ('updater', models.CharField(help_text='更新人', max_length=20, null=True, verbose_name='更新人')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='接口名称')),
                ('body', models.TextField(verbose_name='主体信息')),
                ('url', models.CharField(db_index=True, max_length=255, verbose_name='请求地址')),
                ('method', models.CharField(max_length=10, verbose_name='请求方式')),
                ('relation', models.IntegerField(verbose_name='节点id')),
                ('rig_id', models.IntegerField(db_index=True, null=True, verbose_name='网关API_id')),
                ('rig_env', models.IntegerField(choices=[(0, '测试环境'), (1, '生产环境'), (2, '预发布环境')], default=0, verbose_name='网关环境')),
                ('tag', models.IntegerField(choices=[(0, '未知'), (1, '成功'), (2, '失败'), (3, '自动成功'), (4, '废弃')], default=0, verbose_name='API标签')),
                ('yapi_catid', models.IntegerField(default=0, null=True, verbose_name='yapi的分组id')),
                ('yapi_id', models.IntegerField(default=0, null=True, verbose_name='yapi的id')),
                ('yapi_add_time', models.CharField(default='', max_length=10, null=True, verbose_name='yapi创建时间')),
                ('yapi_up_time', models.CharField(default='', max_length=10, null=True, verbose_name='yapi更新时间')),
                ('yapi_username', models.CharField(default='', max_length=30, null=True, verbose_name='yapi的原作者')),
                ('project', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='lunarlink.project')),
            ],
            options={
                'verbose_name': '接口信息',
                'db_table': 'api',
            },
        ),
    ]
