from .alter_space import AlterSpace
from .build_space import BuildSpace
from .certify_space import CertifySpace
from .decertify_space import DecertifySpace
from .deregister_user_from_space import DeregisterUserFromSpace
from .locate_space_by_id import LocateSpaceById
from .locate_user_spaces import LocateUserSpaces
from .query_space_by_key import QuerySpaceByKey
from .query_space_users import QuerySpaceUsers
from .register_user_to_space import RegisterUserToSpace
from .show_spaces import ShowSpaces

ALL_SPACE_TOOLS = [
    BuildSpace,
    AlterSpace,
    QuerySpaceByKey,
    LocateSpaceById,
    ShowSpaces,
    CertifySpace,
    DecertifySpace,
    RegisterUserToSpace,
    DeregisterUserFromSpace,
    QuerySpaceUsers,
    LocateUserSpaces,
]
