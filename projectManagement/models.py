from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey
from systemModules.models import Company


class Project(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    bdate = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    edate = models.DateField(blank=True, null=True, verbose_name='Дата завершения')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания проекта')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления проекта')
    status = models.ForeignKey('Status', on_delete=models.CASCADE, verbose_name='Статус')
    status_tasks = models.ManyToManyField('Status', blank=True, verbose_name='Статусы для задач', related_name='status_tasks')
    priority_tasks = models.ManyToManyField('Priority', blank=True, verbose_name='Приоритеты для задач', related_name='priority_tasks')
    managers = models.ManyToManyField(User, blank=True, verbose_name='Руководители проекта', related_name='managers')
    moderators = models.ManyToManyField(User, blank=True, verbose_name='Модераторы проекта', related_name='moderators')
    participants = models.ManyToManyField(User, blank=True, verbose_name='Участники проекта', related_name='participants')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, verbose_name='Категория', related_name='category')
    photo = models.ImageField(upload_to='media/projects/%Y/%m/%d', verbose_name='Изображение', blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_company')

    class Meta:
        verbose_name = 'Проекты'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Tasks(MPTTModel):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')
    project = models.ForeignKey('Project', verbose_name='Проект', null=True, blank=True, on_delete=models.CASCADE, related_name='project')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    priority = models.ForeignKey('Priority', on_delete=models.PROTECT, null=True, blank=True, verbose_name='Приоритет', related_name='Priority')
    status = models.ForeignKey('Status', on_delete=models.PROTECT, default=1, verbose_name='Стаус', related_name='status')
    progress = models.IntegerField(default=0, null=True, blank=True, verbose_name='Прогресс')
    is_completed = models.BooleanField(default=False, blank=True, verbose_name='Исполнено')
    bdate = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    edate = models.DateField(blank=True, null=True, verbose_name='Срок')
    tdate = models.DateField(blank=True, null=True, verbose_name='Фактическая дата выполнения')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания задачи')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления задачи')
    estimated_time = models.FloatField(default=0, null=True, blank=True, verbose_name='Оценочное время')
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Автор', related_name='author')
    executor = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Исполнитель', related_name='executor')
    co_executor = models.ManyToManyField(User, blank=True, null=True, verbose_name='Со-исполнители', related_name='co_executor')
    viewers = models.ManyToManyField(User, blank=True, null=True, verbose_name='Наблюдатели', related_name='viewers')
    related_tasks = models.ManyToManyField('Tasks', blank=True, null=True, verbose_name='Связанные задачи', related_name='related_tasks_for')
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_task_company')

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']


class TimeTracking(models.Model):
    task = models.ForeignKey('Tasks', blank=True, on_delete=models.CASCADE, related_name='Задача')
    description = models.CharField(max_length=200, blank=True, verbose_name='Описание')
    track_date = models.DateField(blank=True, verbose_name='Дата')
    spent_time = models.FloatField(blank=True, default=0, null=True, verbose_name='Затраченное время')
    author = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='Пользователь')
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_timetracking_company')

    class Meta:
        verbose_name = 'Учет времени'
        verbose_name_plural = 'Учет времени'
        ordering = ['-pk']

    def __str__(self):
        return self.task.title


class Status(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование', blank=True)
    title_tech = models.CharField(max_length=100, verbose_name='Техническое наименование', blank=True)
    html_color = models.CharField(max_length=100, verbose_name='Цвет HTML', blank=True)
    css_color = models.CharField(max_length=100, verbose_name='CSS класс', blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_status_company')

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'
        ordering = ['-pk']

    def __str__(self):
        return self.title


class Priority(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование', blank=True)
    title_tech = models.CharField(max_length=100, verbose_name='Техническое наименование', blank=True)
    html_color = models.CharField(max_length=100, verbose_name='Цвет HTML', blank=True)
    css_color = models.CharField(max_length=100, verbose_name='CSS класс', blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_priority_company')

    class Meta:
        verbose_name = 'Приоритет'
        verbose_name_plural = 'Приоритет'
        ordering = ['-pk']

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование', blank=True)
    title_tech = models.CharField(max_length=100, verbose_name='Техническое наименование', blank=True)
    html_color = models.CharField(max_length=100, verbose_name='Цвет HTML', blank=True)
    css_color = models.CharField(max_length=100, verbose_name='CSS класс', blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_category_company')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['-pk']

    def __str__(self):
        return self.title


class UserSelfCategory(models.Model):
    category = models.ForeignKey('UserSelfCategoryDictionary', on_delete=models.CASCADE, verbose_name='Категория', blank=True, related_name='user_self_category')
    task = models.ForeignKey('Tasks', blank=True, verbose_name='Задача', on_delete=models.CASCADE, related_name='user_self_category_task')
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_userselfcategory_company')

    class Meta:
        verbose_name = 'Пользовательская категория'
        verbose_name_plural = 'Пользовательская категория'
        ordering = ['-pk']

    def __str__(self):
        return self.category.title


class UserSelfCategoryDictionary(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование', blank=True)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Пользователь', related_name='user_self_category_dictionary')
    html_color = models.CharField(max_length=100, verbose_name='Цвет', blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_userself_category_dictionary_company')

    class Meta:
        verbose_name = 'Пользовательская категория справочник'
        verbose_name_plural = 'Пользовательская категория справочник'
        ordering = ['-pk']

    def __str__(self):
        return self.title


class UserSelfSavedTasks(models.Model):
    task = models.ForeignKey('Tasks', blank=True, verbose_name='Задача', on_delete=models.CASCADE, related_name='user_self_saved_task')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Пользователь', related_name='user_self_pk_saved_task')
    save_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания задачи')
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_userself_saved_tasks_company')

    class Meta:
        verbose_name = 'Сохраненные записи'
        verbose_name_plural = 'Сохраненные записи'
        ordering = ['pk']

    def __str__(self):
        return self.task.title


class TaskChangeHistory(models.Model):
    task_change_action = models.ForeignKey('TaskChangeHistoryAction', verbose_name='Сведения об изменении задачи', on_delete=models.CASCADE, related_name='task_change')
    column = models.CharField(max_length=100, verbose_name='Строка изменения', blank=True)
    first_value = models.CharField(default='', max_length=200, blank=True, null=True, verbose_name='Первоначальное значение')
    finish_value = models.CharField(default='', max_length=200, blank=True, null=True, verbose_name='Конечное значение')
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_task_change_history_company')

    class Meta:
        verbose_name = 'История изменения задачи'
        verbose_name_plural = 'История изменения задачи'
        ordering = ['pk']

    def __str__(self):
        return self.task_change_action.task.title


class TaskChangeHistoryAction(models.Model):
    task = models.ForeignKey('Tasks', blank=True, verbose_name='Задача', on_delete=models.CASCADE, related_name='change_action_task')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.PROTECT, verbose_name='Пользователь', related_name='user_change_task_action')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата изменения задачи')
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_task_change_history_action_company')

    class Meta:
        verbose_name = 'Сведения об изменении задачи'
        verbose_name_plural = 'Сведения об изменении задачи'
        ordering = ['pk']

    def __str__(self):
        return self.task.title


class TaskApproveStatus(models.Model):
    id_status = models.IntegerField(default=0, verbose_name='ID', blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name='Название статуса', blank=True)
    description = models.CharField(max_length=100, verbose_name='Описание статуса', blank=True)
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_task_approve_status_company')

    class Meta:
        verbose_name = 'Статус исполенности задачи'
        verbose_name_plural = 'Статус исполенности задачи'
        ordering = ['pk']

    def __str__(self):
        return self.description


class TaskApproveStatusActions(models.Model):
    task = models.ForeignKey('Tasks', verbose_name='Задача', on_delete=models.CASCADE, null=True, blank=True)
    approve_status = models.ForeignKey('TaskApproveStatus', verbose_name='Статус исполненности задачи', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')
    user_sent_at = models.DateField(blank=True, null=True, verbose_name='Время исполнения задачи')
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_task_approve_status_actions_company')

    class Meta:
        verbose_name = 'Текущий статус исполненности задачи'
        verbose_name_plural = 'Текущий статус исполненности задачи'
        ordering = ['pk']

    def __str__(self):
        return self.task.title


class TaskAnswerByExecutors(models.Model):
    task = models.ForeignKey('Tasks', blank=True, on_delete=models.CASCADE, related_name='task_answer', verbose_name='Задача')
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Автор', related_name='task_answer_author')
    approve_action = models.ForeignKey('TaskApproveStatusActions', verbose_name='Статус исполненности задачи', on_delete=models.CASCADE, null=True, blank=True)
    answer_description = models.TextField(blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата ответа')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.PROTECT, verbose_name='Компания',
                                related_name='project_task_answer_by_executors_company')

    class Meta:
        verbose_name = 'Ответ исполнителя'
        verbose_name_plural = 'Ответ исполнителя'
        ordering = ['pk']

    def __str__(self):
        return self.task.title


class ProjectPosition(models.Model):
    title = models.CharField(max_length=100, verbose_name='Наименование позиции', blank=True)
    project = models.ForeignKey('Project', verbose_name='Проект', null=True, blank=True, on_delete=models.CASCADE)
    skills = models.ManyToManyField('Skills', blank=True, verbose_name='Навыки',
                                    related_name='project_position_skill')
    access_lvl = models.IntegerField(default=0, verbose_name='Процент доступа', blank=True, null=True)

    class Meta:
        verbose_name = 'Skill Позиция в проекте'
        verbose_name_plural = ' Skill Позиция в проекте'
        ordering = ['pk']

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=250, verbose_name='Навык', blank=True)
    questions = models.ManyToManyField('SkillQuestion', blank=True, verbose_name='Вопросы',
                                    related_name='question_skills_no')

    class Meta:
        verbose_name = 'Skill Навыки'
        verbose_name_plural = 'Skill Навыки'
        ordering = ['pk']

    def __str__(self):
        return self.title


class SkillQuestion(models.Model):
    title = models.CharField(max_length=250, verbose_name='Вопрос по навыку', blank=True)
    right_answer = models.ForeignKey('SkillQuestionAnswers', verbose_name='Ответ к вопросу', null=True, blank=True, on_delete=models.CASCADE)
    answers = models.ManyToManyField('SkillQuestionAnswers', blank=True, verbose_name='Список ответов',
                                    related_name='skill_question_answers_on')

    class Meta:
        verbose_name = 'Skill Вопрос по навыку'
        verbose_name_plural = 'Skill Вопрос по навыку'
        ordering = ['pk']

    def __str__(self):
        return self.title


class SkillQuestionAnswers(models.Model):
    title = models.CharField(max_length=250, verbose_name='Ответ по вопросу навыка', blank=True)

    class Meta:
        verbose_name = 'Skill Ответы по навыку'
        verbose_name_plural = 'Skill Ответы по навыку'
        ordering = ['pk']

    def __str__(self):
        return self.title


class ProjectPositionUsers(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Сотрудник',
                               related_name='project_position_user')
    project_position = models.ForeignKey('ProjectPosition', verbose_name='Позиция', null=True, blank=True, on_delete=models.CASCADE)
    is_access = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        verbose_name = 'Skill Позиция пользователя в проекте'
        verbose_name_plural = 'Skill Позиция пользователя в проекте'
        ordering = ['pk']

    def __str__(self):
        return self.user.first_name


class SkillUserAnswers(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Сотрудник',
                             related_name='skill_user_answer')
    project = models.ForeignKey('Project', verbose_name='Проект', null=True, blank=True, on_delete=models.CASCADE)
    questions = models.ForeignKey('SkillQuestion', blank=True, on_delete=models.CASCADE, verbose_name='Вопросы',
                                                related_name='skill_user_question')
    skill = models.ForeignKey('Skills', blank=True, null=True, on_delete=models.CASCADE, verbose_name='Навык',
                             related_name='skill_answer_user')
    user_answer = models.ForeignKey('SkillQuestionAnswers', verbose_name='Ответ к вопросу', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Skill Ответ сотрудника'
        verbose_name_plural = 'Skill Ответ сотрудника'
        ordering = ['pk']

    def __str__(self):
        return self.user.first_name + ' - ' +self.questions.title