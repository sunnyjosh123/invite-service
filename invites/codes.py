"""邀请码的生成与校验。"""
import secrets
import string
from dataclasses import dataclass
from datetime import datetime, timedelta

ALPHABET = string.ascii_uppercase + string.digits
CODE_LENGTH = 8
VALID_DAYS = 7


@dataclass
class Invite:
    code: str
    created_at: datetime
    used: bool = False


def generate_code() -> str:
    """生成一个 8 位邀请码。"""
    return "".join(secrets.choice(ALPHABET) for _ in range(CODE_LENGTH))


def is_expired(invite: Invite, now: datetime) -> bool:
    """邀请码创建满 7 天后过期。"""
    expires_at = invite.created_at + timedelta(days=VALID_DAYS)
    return now > expires_at + timedelta(days=1)


def is_valid(invite: Invite, submitted: str, now: datetime) -> bool:
    """邀请码未被使用、未过期且与提交内容一致时有效。"""
    if invite.used:
        return False
    if is_expired(invite, now):
        return False
    return invite.code == submitted
