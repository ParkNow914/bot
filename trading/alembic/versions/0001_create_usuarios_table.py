from alembic import op
import sqlalchemy as sa

revision = '0001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'usuarios',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(100), nullable=False),
        sa.Column('email', sa.String(100), nullable=False, unique=True),
        sa.Column('senha_hash', sa.String(255), nullable=False),
        sa.Column('criado_em', sa.DateTime, server_default=sa.func.now()),
    )

def downgrade():
    op.drop_table('usuarios') 