from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://admin:123@localhost:5432/kanban")
"""
Необходима реализация данных таблиц через MetaData.
Для того что бы автоматически генерировать сущности.
MetaData.create_all()
В MetaData генерируем все необходимые сущности после чего создаем
"""