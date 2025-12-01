from fgo_app.ui.BaseDescriptionDialog import BaseDescriptionDialog

class ArmamentDescriptionDialog(BaseDescriptionDialog):
    def __init__(self, data, unlock_callback, can_unlock, parent=None):
        title = data.get("name")
        description = data.get("description", "")
        effects = data.get("effects", [])
        is_unlocked = data.get("is_unlocked", False)
        extra_fields = {
            "Type": data.get("type"),
        }

        super().__init__(
            title=title,
            description=description,
            effects=effects,
            extra_fields=extra_fields,
            unlock_callback=unlock_callback,
            can_unlock=can_unlock,
            is_unlocked=is_unlocked,
            parent=parent
        )
