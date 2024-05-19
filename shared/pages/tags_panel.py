# -*- coding: utf-8 -*-
from objectmaphelper import *
from .names import *

class TagsPanel:
    
    @staticmethod
    def tag_name(occurrence: int):
        """
        occurrence:
        1. Name for 1st Tag
        2. Name for 2nd Tag
        ...
        10. Name for 10th Tag
        """
        return {"container": launcherQmlView_QQuickView, "id": "tagNameTextField", "occurrence": occurrence, "type": "TextFieldError", "unnamed": 1, "visible": False}