from fabric.api import env, run

from coat.django.settings import DjangoSettings, VirtualEnvSettings
from coat.django import commands

env.django_settings = DjangoSettings()
env.virtualenv_settings = VirtualEnvSettings()


def env_test():
    env.hosts = [""]
    env.user = "{{ project_name }}"
    env.base_dir = ""

    env.django_settings.update(
        settings_file="localsettings_test.py",
        django_appname="{{ project_name }}",
        management_commands=(
            'syncdb --migrate --noinput',
            'collectstatic --noinput'
        ),
        versions_dir="versions",
        wsgi_file="wsgi/django.wsgi",
    )

    env.virtualenv_settings.update(
        env_dir="env",
        commands=[
            ('pip -q install '
             '-r django/requirements/base.txt '
             '-r django/requirements/test.txt'),
        ],
    )


def env_live():
    pass
