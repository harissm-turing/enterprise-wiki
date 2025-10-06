from .acquire_space_by_id import AcquireSpaceById
from .acquire_user_spaces import AcquireUserSpaces
from .attach_user_to_space import AttachUserToSpace
from .catalog_spaces import CatalogSpaces
from .detach_user_from_space import DetachUserFromSpace
from .initiate_space import InitiateSpace
from .invalidate_space import InvalidateSpace
from .obtain_space_by_key import ObtainSpaceByKey
from .obtain_space_users import ObtainSpaceUsers
from .revise_space import ReviseSpace
from .validate_space import ValidateSpace

ALL_SPACE_TOOLS = [
    InitiateSpace,
    ReviseSpace,
    ObtainSpaceByKey,
    AcquireSpaceById,
    CatalogSpaces,
    ValidateSpace,
    InvalidateSpace,
    AttachUserToSpace,
    DetachUserFromSpace,
    ObtainSpaceUsers,
    AcquireUserSpaces,
]
