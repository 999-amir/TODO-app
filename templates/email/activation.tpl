{% extends 'mail_templated/base.tpl' %}

{% block subject %}
this is subject
{% endblock %}

{% block html %}
http://127.0.0.1:8000/accounts/api/v1/user/activation/confirm/{{ token }}
{% endblock %}