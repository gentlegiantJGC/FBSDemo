from fbs_runtime.application_context.PySide2 import ApplicationContext
from fbs_runtime import application_context


def get_context():
    return application_context.get_application_context(
        application_context.PySide2.ApplicationContext
    )
