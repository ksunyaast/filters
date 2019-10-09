from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    now_time = datetime.now()
    pub_date = datetime.fromtimestamp(value)
    passed_time = now_time - pub_date
    passed_minutes = passed_time.seconds / 60
    passed_hours = passed_minutes / 60
    msg = ''
    if passed_minutes < 10:
        msg = 'только что'
    if passed_minutes >= 10 and passed_hours < 24:
        msg = f'{int(passed_hours)} часов назад'
    if passed_hours >= 24:
        msg = f'{datetime.strftime(pub_date, "%Y-%m-%d")}'
    # passed_time.days
    return msg

# необходимо добавить фильтр для поля `score`
@register.filter
def format_raiting(score):
    msg = ''
    if score:
        score = int(score)
        if score < -5:
            msg = 'все плохо'
        if score >= -5 and score <= 5:
            msg = 'нейтрально'
        if score > 5:
            msg = 'хорошо'
    return msg

@register.filter
def format_num_comments(value: int) -> str:
    # Ваш код
    msg = ''
    if value == 0:
        msg = 'Оставьте комментарий'
    if value > 0 and value < 50:
        msg = value
    if value >= 50:
        msg = '50+'
    return msg

@register.filter
def format_selftext (text):
    count = 5
    text_list = text.split(' ')
    if len(text_list) <= count * 2:
        new_text = text
    if len(text_list) > count * 2:
        begin_part = ' '.join(text_list[:count])
        end_part = ' '.join(text_list[len(text_list)-count:])
        new_text = f'{begin_part} ... {end_part}'
    return new_text

