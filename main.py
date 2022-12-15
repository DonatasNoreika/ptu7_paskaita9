from modules import elektromobilis
import django

automobilis1 = elektromobilis.Automobilis(2019, "Toyota Corolla", 'hibridas')
automobilis2 = elektromobilis.Elektromobilis(2022, "Tesla Model S Plaid", 'elektra')

print(automobilis1)
automobilis1.stoveti()
automobilis1.vaziuoti()
automobilis1.pildyti_degalu()
automobilis2.stoveti()
automobilis2.vaziuoti()
automobilis2.pildyti_degalu()
automobilis2.vaziuoti_autonomiskai()
