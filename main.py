from modules import elektromobilis
import django

automobilis1 = elektromobilis.Automobilis(2019, "Toyota Corolla", 'hibridas')
automobilis2 = elektromobilis.Elektromobilis(2022, "Tesla Model S Plaid", 'elektra')
automobilis3 = elektromobilis.Elektromobilis(2022, "MB EQS", 'elektra')

print(automobilis1)
automobilis1.stoveti()
automobilis1.vaziuoti()
automobilis1.pildyti_degalu()
print(automobilis3.stoveti())
print(automobilis3.pildyti_degalu())