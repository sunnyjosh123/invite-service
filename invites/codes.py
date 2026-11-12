"""邀请码的生成与校验。"""
import secrets
import string
from dataclasses import dataclass

ALPHABET = string.ascii_uppercase + string.digits
CODE_LENGTH = 8


@dataclass
class Invite:
    code: str
    used: bool = False


def generate_code() -> str:
    """生成一个 8 位邀请码。"""
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LENGTH))


def is_valid(invite: Invite, submitted: str) -> bool:
    """邀请码未被使用且与提交内容一致时有效。"""
    if invite.used:
        return False
    return invite.code == submitted
