class Router:
    def db_for_read(self, model, **hints):
        print('read', model, hints)
        return 'mysql_slave'

    def db_for_write(self, model, **hints):
        # model, hints：model对象，表创建的实例对象
        print('write', model, hints)
        return 'default'
