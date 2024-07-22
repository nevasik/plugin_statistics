# constants.py

START_MESSAGE = (
    "Добро пожаловать! Вот список доступных команд:\n\n"
    "/total_turnover_and_margin - Получить общий оборот и маржу.\n"
    "/turnover_and_margin_by_period <start_date> <end_date> - Получить оборот и маржу за указанный период.\n"
    "/claim_status_by_external_id <external_id> - Узнать статус заявки по внешнему ID.\n"
    "/total_turnover_and_margin_general - Получить общий оборот и маржу по всем заявкам.\n\n"
    "Используйте команды, чтобы получить нужную информацию."
)

NOT_FOUND = "Записей пока нет."
NO_ACCESS = "Извините, у вас нет доступа к этому боту."
