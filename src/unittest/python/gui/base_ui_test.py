import unittest
from PySide2.QtUiTools import QUiLoader

from demo.app import get_context


class BaseUITest:
    class BaseUITest(unittest.TestCase):
        RequiredAttributes = ()
        ui_file = None

        def test_attributes(self):
            self.assertIsNot(None, self.ui_file)
            ui = QUiLoader().load(get_context().get_resource(self.ui_file), None)
            for attr_name, attr_cls in self.RequiredAttributes:
                self.assertTrue(
                    hasattr(ui, attr_name),
                    msg=f"Expected ui file {self.ui_file} to have the attribute {attr_name}"
                )
                attr = getattr(ui, attr_name)
                self.assertIsInstance(
                    attr,
                    attr_cls,
                    msg=f"Expected attribute {attr_name} to be of type {attr_cls} but got {type(attr)}"
                )
