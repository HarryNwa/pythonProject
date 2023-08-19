def your_vat():
    while True:
        try:

            customer = float(input("What is the price? "))
            vat_rate = float(input("Hello kindly enter VAT. Kindly note that VAT rate is: "))

            vat = float(vat_rate / 100)
            if customer < 0 and vat_rate < 0:

                    print("Sorry, price and/or VAT cannot be less than zero. Kindly re-enter the amount")
                    your_vat()
            else:
                print("Thank You")
                current_vat = customer * vat
                price_vat = customer + current_vat
                print("Price plus VAT is: ", price_vat)
                print("VAT at 15% is: ", current_vat)

        except(ValueError, KeyboardInterrupt):
            print("Please enter correct input")
            your_vat()
        break


your_vat()