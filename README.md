## Система автодеплоя

Система служить для автодеплоинга проектов(пока что ориентация на python проекты), все что необходимо
это создать json файл в папке conf и указать все необходимые конфигурации, пока что данная система
сырая и возможны проблемы ввиде ошибок. Логирование находится в папке log/*

Пока что возможности ограничываются установкой пакетов(с возможностью указания версии пакетов),
деплой приложении через git(клонированеи и установка зависимостей по req.txt), установки
пакетов для виртуального(и глобального) окружения Python.

    Аргументы которые можно передать:
        os - Операционная система которая используется на сервере
        serv - Перечисление конфигурационных файлов через запятую которые необходимо 
        обработать для автодеплоинга
        dir - Название категории где находятся ваши конфигурационные файлы

Документация по этой ссылке:
    https://github.com/Rinat93/autodeploing/tree/master/conf