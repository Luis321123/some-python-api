"""empty message

Revision ID: 52e8e39b2564
Revises: f42e8cfb91ba
Create Date: 2024-09-13 17:22:07.246245

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '52e8e39b2564'
down_revision: Union[str, None] = 'f42e8cfb91ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'churches', 'church_denominations', ['church_denomination_uuid'], ['uuid'])
    op.alter_column('users', 'name',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=150),
               existing_nullable=True)
    op.alter_column('users', 'email',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=100),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.String(length=100),
               type_=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('users', 'email',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.alter_column('users', 'name',
               existing_type=sa.String(length=150),
               type_=sa.VARCHAR(length=50),
               existing_nullable=True)
    op.drop_constraint(None, 'churches', type_='foreignkey')
    # ### end Alembic commands ###