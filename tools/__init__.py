from .create_space import CreateSpace
from .update_space import UpdateSpace
from .delete_space import DeleteSpace
from .get_space_by_key import GetSpaceByKey
from .get_space_by_id import GetSpaceById
from .list_spaces import ListSpaces
from .approve_space import ApproveSpace
from .unapprove_space import UnapproveSpace
from .add_user_to_space import AddUserToSpace
from .remove_user_from_space import RemoveUserFromSpace
from .get_space_users import GetSpaceUsers
from .get_user_spaces import GetUserSpaces


ALL_SPACE_TOOLS = [
    CreateSpace,
    UpdateSpace,
    DeleteSpace,
    GetSpaceByKey,
    GetSpaceById,
    ListSpaces,
    ApproveSpace,
    UnapproveSpace,
    AddUserToSpace,
    RemoveUserFromSpace,
    GetSpaceUsers,
    GetUserSpaces
]