#!/bin/bash
set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE "test_expense_tracker";
    CREATE DATABASE "expense_tracker";
EOSQL
