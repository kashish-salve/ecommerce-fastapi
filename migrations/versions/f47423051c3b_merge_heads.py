"""merge heads

Revision ID: f47423051c3b
Revises: 671fb2b16e3f, f03686c1211c
Create Date: 2026-05-25 14:34:41.841901

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f47423051c3b'
down_revision: Union[str, Sequence[str], None] = ('671fb2b16e3f', 'f03686c1211c')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
