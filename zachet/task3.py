def is_enough_rocket(rental_requests):
    # Сортируем заявки по времени начала аренды
    rental_requests.sort(key=lambda x: x[0])

    # Инициализируем переменную, хранящую время, когда ракета свободна после последней аренды
    end_time = 0

    # Проходим по всем заявкам
    for rental_request in rental_requests:
        start_time, finish_time = rental_request

        if start_time >= end_time:
            # Если время начала аренды текущей заявки больше или равно end_time, то мы можем использовать текущую ракету
            end_time = finish_time
        else:
            # Если время начала аренды текущей заявки меньше end_time, то нам нужна еще одна ракета
            end_time = max(end_time, finish_time)

    # Если значение end_time меньше или равно 24, значит, одной ракеты достаточно, иначе нужна еще одна ракета
    return end_time <= 24
