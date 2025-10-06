from .add_user_to_space import AddUserToSpace
from .approve_space import ApproveSpace
from .create_space import CreateSpace
from .get_space_by_id import GetSpaceById
from .get_space_by_key import GetSpaceByKey
from .get_space_users import GetSpaceUsers
from .get_user_spaces import GetUserSpaces
from .list_spaces import ListSpaces
from .remove_user_from_space import RemoveUserFromSpace
from .unapprove_space import UnapproveSpace
from .update_space import UpdateSpace

ALL_SPACE_TOOLS = [
    CreateSpace,
    UpdateSpace,
    GetSpaceByKey,
    GetSpaceById,
    ListSpaces,
    ApproveSpace,
    UnapproveSpace,
    AddUserToSpace,
    RemoveUserFromSpace,
    GetSpaceUsers,
    GetUserSpaces,
]
