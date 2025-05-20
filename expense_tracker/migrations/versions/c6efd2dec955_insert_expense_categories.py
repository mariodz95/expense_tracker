"""Insert expense categories

Revision ID: c6efd2dec955
Revises: 933631f282e0
Create Date: 2025-05-20 14:27:42.286257

"""

from alembic import op
import sqlalchemy as sa
import sqlmodel  # NEW
import uuid
from datetime import datetime, timezone


# revision identifiers, used by Alembic.
revision = "c6efd2dec955"
down_revision = "933631f282e0"
branch_labels = None
depends_on = None


def upgrade():
    # Create a reference to the expense_category table
    expense_category_table = sa.Table(
        "expense_category",
        sa.MetaData(),
        sa.Column("id", sa.UUID(), primary_key=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("date_created_at", sa.DateTime(), nullable=False),
        sa.Column("date_updated_at", sa.DateTime(), nullable=False),
        sa.Column("created_by", sa.String(), nullable=False),
        sa.Column("updated_by", sa.String(), nullable=True),
        sa.Column("soft_deleted", sa.Boolean(), default=False),
    )

    # Insert predefined categories into the 'expense_category' table
    current_time = datetime.now(timezone.utc).replace(tzinfo=None)  # current UTC time
    categories = [
        {
            "id": uuid.uuid4(),
            "name": "Food",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
        {
            "id": uuid.uuid4(),
            "name": "Transport",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
        {
            "id": uuid.uuid4(),
            "name": "Utilities",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
        {
            "id": uuid.uuid4(),
            "name": "Entertainment",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
        {
            "id": uuid.uuid4(),
            "name": "Healthcare",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
        {
            "id": uuid.uuid4(),
            "name": "Groceries",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
        {
            "id": uuid.uuid4(),
            "name": "Rent",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
        {
            "id": uuid.uuid4(),
            "name": "Insurance",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
        {
            "id": uuid.uuid4(),
            "name": "Savings",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
        {
            "id": uuid.uuid4(),
            "name": "Education",
            "date_created_at": current_time,
            "date_updated_at": current_time,
            "created_by": "SYSTEM",
            "updated_by": "SYSTEM",
            "soft_deleted": False,
        },
    ]

    # Bulk insert the categories into the 'expense_category' table using the Table object
    op.bulk_insert(expense_category_table, categories)


def downgrade():
    # Remove the categories in case of downgrade (if needed)
    op.execute(
        "DELETE FROM expense_category WHERE name IN ('Food', 'Transport', 'Utilities', 'Entertainment', 'Healthcare', 'Groceries', 'Rent', 'Insurance', 'Savings', 'Education')"
    )
