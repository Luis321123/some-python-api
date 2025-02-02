"""empty message

Revision ID: 0ad336d86c22
Revises: 81859b10da45
Create Date: 2024-09-25 17:02:01.056822

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ad336d86c22'
down_revision: Union[str, None] = '81859b10da45'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'churches', 'cities', ['city_uuid'], ['uuid'])
    op.add_column('regions', sa.Column('country_uuid', sa.UUID(as_uuid=200), nullable=True))
    op.create_foreign_key(None, 'regions', 'countries', ['country_uuid'], ['uuid'])
    op.alter_column('user_session', 'token',
               existing_type=sa.TEXT(),
               type_=sa.String(length=255),
               existing_nullable=True)
    op.alter_column('user_session', 'firebase_token',
               existing_type=sa.VARCHAR(length=250),
               type_=sa.Text(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_session', 'firebase_token',
               existing_type=sa.Text(),
               type_=sa.VARCHAR(length=250),
               existing_nullable=True)
    op.alter_column('user_session', 'token',
               existing_type=sa.String(length=255),
               type_=sa.TEXT(),
               existing_nullable=True)
    op.drop_constraint(None, 'regions', type_='foreignkey')
    op.drop_column('regions', 'country_uuid')
    op.drop_constraint(None, 'churches', type_='foreignkey')
    # ### end Alembic commands ###