from fastapi import FastAPI


fastapi_instance = FastAPI()


@fastapi_instance.get()
def get_current_sallary():
    """ Получить по API текущую зарплату конкретного сотрудника, включая контроль доступа """
    pass


@fastapi_instance.get()
def up_sallary_incr():
    """ Получить по API дату и размер следующего повышения заработной платы конкретного сотрудника, включая контроль доступа """
    pass
