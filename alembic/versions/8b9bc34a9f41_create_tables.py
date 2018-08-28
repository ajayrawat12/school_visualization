"""create tables

Revision ID: 8b9bc34a9f41
Revises: 
Create Date: 2018-08-28 08:27:57.750808

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b9bc34a9f41'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'classes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(155)),

    ),
    op.create_table(
        'section',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(55)),
        sa.Column('students', sa.Integer),
    ),
    op.create_table(
        'student',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50)),
        sa.Column('dob', sa.Date()),
        sa.Column('gender', sa.String(155)),
        sa.Column('address', sa.String(255)),
        sa.Column('section_id', sa.Integer, sa.ForeignKey('section.id')),
        sa.Column('class_id', sa.Integer, sa.ForeignKey('classes.id')),
    )


def downgrade():
    op.drop_table('student')
    op.drop_table('classes')
    op.drop_table('section')
