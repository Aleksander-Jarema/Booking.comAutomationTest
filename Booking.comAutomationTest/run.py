from booking.booking import Booking
from datetime import date, timedelta

today = date.today()
check_in_date = today.isoformat()
check_out_date = (today + timedelta(days=4)).isoformat()

with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go('New York')
    bot.select_dates(check_in_date, check_out_date)
    bot.select_adults()
    bot.select_final_results()

    input("Press ENTER to exit...")



