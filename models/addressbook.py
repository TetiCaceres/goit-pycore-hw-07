from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    """Stores and manages contact records."""

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "Record deleted."
        return "Record not found."

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming = []

        for record in self.data.values():
            if not record.birthday:
                continue

            bday_this_year = record.birthday.value.replace(year=today.year)
            if bday_this_year < today:
                bday_this_year = bday_this_year.replace(year=today.year + 1)

            delta_days = (bday_this_year - today).days
            if 0 <= delta_days <= 7:
                congrat_date = bday_this_year
                if bday_this_year.weekday() == 5:  # Saturday
                    congrat_date += timedelta(days=2)
                elif bday_this_year.weekday() == 6:  # Sunday
                    congrat_date += timedelta(days=1)
                upcoming.append({
                    "name": record.name.value,
                    "congratulation_date": congrat_date.strftime("%d.%m.%Y")
                })

        return upcoming