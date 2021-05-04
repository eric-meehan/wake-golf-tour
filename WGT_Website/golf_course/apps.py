from django.apps import AppConfig


class GolfCourseConfig(AppConfig):
    name = 'golf_course'
#ols.command.easy_install import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
