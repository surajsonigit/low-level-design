from typing import List, Optional
from models.group import Group
from models.user import User

class GroupController:
    def __init__(self):
        self.group_list: List[Group] = []

    def create_new_group(self, group_id: str, group_name: str, created_by_user: User) -> None:
        group = Group()
        group.set_group_id(group_id)
        group.set_group_name(group_name)
        group.add_member(created_by_user)
        self.group_list.append(group)

    def get_group(self, group_id: str) -> Optional[Group]:
        for group in self.group_list:
            if group.get_group_id() == group_id:
                return group
        return None
