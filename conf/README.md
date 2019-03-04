
### Описание конфигурационного файла
    
    WARNING: Система провералась исключительно на Debian 9
    
    static - Откуда копировать статику(медиа + static) 
    
    app - Где находится приложение которое необходимо задеплоить, 
    либо ссылка на git
    
    git - Дополнительные пакеты/приложения которое необходимо подтянуть с git'а
        local - Куда положить исходный код
        
    install - Какие пакеты необходимо установить на уровне ОС
    
    Пакеты внутри массива install имеют свойства
        1. name - название пакета
        2. version - версия пакета
    
    Изначально система реализовывалась для деплоя Python приложени, потому
    есть доп функционал:
    
    venv-settings - Настройка виртуального окружения
        1. name - Имя виртуального окружения
        2. Module - Имя модуля который поддерживается на данный момент
            
            2.1 У модулей есть особенная вложенность, к примеру 
                project - проект берется из git репозитория
                git - имеет свойства:
                    src - Ссылка на проект
                    user - Имя пользователя
                    password - Пароль
                    local - Куда склонировать репу
                
                package - Путь до файла req.txt с пакетами
            
            2.2. package - Перечисление пакетов и версии ввиде ключ - значение
            
            2.3. Глобальный package за пределами venv-settings 
            
        3. src - Где будет находится виртуальное окружение
        4. package - Какие пакеты необходимо установить