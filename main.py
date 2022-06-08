import argparse
import math
parser = argparse.ArgumentParser()
parser.add_argument("--type", type=str,
                    help="Enter the type of operation")
#parser.add_argument("--operation_1",
#                    type=float,
#                    help="Choose three parameters")
#parser.add_argument("--operation_2",
#                    choices=["loan_principal", "periods", "interest", "payment"],
#                    type=float,
#                    help="Choose three parameters")
#parser.add_argument("--operation_3",
#                    choices=["loan_principal", "periods", "interest", "payment"],
#                    type=float,
#                    help="Choose three parameters")
parser.add_argument("--principal", type=float,
                   help="Enter the loan principal")
parser.add_argument("--periods", type=float,
                   help="Enter the number of periods:")
parser.add_argument("--interest", type=float,
                    help="Enter the loan interest")
parser.add_argument("--payment", type=float,
                   help="Enter the month payment")

args = parser.parse_args()
#пропустила Example3
if args.interest is None:
            print('Incorrect parameters')
elif args.interest is not None:
    if args.type == 'diff':
        #Example1 and Example4
        i = args.interest/(12*100)
        m = 1
        final_payment = 0
        while m <= args.periods:
            dif_payment = (args.principal / args.periods + i * (args.principal - (args.principal * (m - 1) / args.periods)))
            final_payment += math.ceil(dif_payment)
            print(f"Month {m}: payment is {math.ceil(dif_payment)}")
            m += 1
        print(f"""
    Overpayment = {math.ceil(final_payment - args.principal)}""")

    #если заданы loan_principal, periods, interest + тип annuity
    #ДОДЕЛАТЬ ТИП
    if args.type == 'annuity':
        i = args.interest / (12 * 100)
        final_payment = 0
        #Example2
        if args.principal and args.periods:
            annuity_payment = math.ceil((-i*args.principal*(i+1)**args.periods)/(1-(i+1)**args.periods))
            print(f"Your annuity payment = {annuity_payment}!")
            final_payment = annuity_payment * args.periods
            print(f"Overpayment = {math.ceil(final_payment - args.principal)}")
        #Example5
        if args.payment and args.periods:
            loan_principall = (-args.payment * (1 - (i + 1) ** args.periods)) / (i * (i + 1) ** args.periods)
            print(f"Your loan principal = {math.floor(loan_principall)}!")
            final_payment = args.payment * args.periods
            print(f"Overpayment = {math.ceil(final_payment - loan_principall)}")
        #Example6
        if args.principal and args.payment:
            n = math.log((args.payment / (args.payment - i * args.principal)), (1 + i))
            years, month = divmod(n, 12)
            if math.ceil(month) == 12:
                years = years + 1
                print(f"It will take {math.ceil(years)} years to repay this loan!")
            elif years == 0:
                print(f"It will take {math.ceil(month)} months to repay this loan!")
                # elif years > 0 and month == 12:
                #   print(f"It will take {math.ceil(years)+1} years to repay this loan!")
            elif years == 0 and month == 1:
                print(f"It will take {math.ceil(month)} month to repay this loan!")
            elif years == 1:
                print(f"It will take {math.ceil(years)} year and {math.ceil(month)} months to repay this loan!")
            elif month == 0 and years == 1:
                print(f"It will take {math.ceil(years)} year to repay this loan!")
            elif month == 0:
                print(f"It will take {math.ceil(years)} years to repay this loan!")
            elif month == 1:
                print(f"It will take {math.ceil(years)} years and {math.ceil(month)} month to repay this loan!")
            else:
                print(f"It will take {math.ceil(years)} years and {math.ceil(month)} months to repay this loan!")
            time = years*12 + month
            final_payment = args.payment * round(n)
            print(f"Overpayment = {math.ceil(final_payment - args.principal)}")

