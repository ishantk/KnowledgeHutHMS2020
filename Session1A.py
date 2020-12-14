"""

	SBI puts an offer on its credit card over Amazon
	wish to know what kind of products are being purchased by the user on amazon

	Category
		SmartPhone
		HomAppliances

		SmartPhone
		day1 sales 	: 150 units
		day2 sales 	: 110 units
		day3 sales 	: 60 units
		day4 sales 	: 250 units
		day5 sales 	: 90 units

		HomAppliances
		day1 sales 	: 250 units
		day2 sales 	: 170 units
		day3 sales 	: 160 units
		day4 sales 	: 350 units
		day5 sales 	: 190 units


		For some offline marketing SBI can make it from this sales
		if they should come up with offline marketing in the local mobile stores
		or local home applicances stores

		As a human we can calculate number of units of the products sold everyday and sit back and add them and provide some stats

		Total Units sold, Total Profits Made, Total Discounts Provided
		1. TIME
		2. ACCURACY

		Architecture
		------------
		MODEL
			Data for Your Problem
		VIEW
			UI for the End User using your Software Solution
			I/O take data from user process it and show it back as result
			UI/UX
		CONTROLLER
			Logical Processing of Data
				Computation
				Conditional Decisions
				Iterations

"""

# Model: Represent the data
smart_phone_day1_sales = 250
smart_phone_day2_sales = 170
smart_phone_day3_sales = 160
smart_phone_day4_sales = 250
smart_phone_day5_sales = 90

home_appliance_day1_sales = 150
home_appliance_day2_sales = 110
home_appliance_day3_sales = 60
home_appliance_day4_sales = 550
home_appliance_day5_sales = 190

# Controller: Computation on Data
smart_phone_sales = smart_phone_day1_sales + smart_phone_day2_sales + smart_phone_day3_sales + smart_phone_day4_sales + smart_phone_day5_sales
home_appliance_sales = home_appliance_day1_sales + home_appliance_day2_sales + home_appliance_day3_sales + home_appliance_day4_sales + home_appliance_day5_sales

print("Smart Phone Sales", smart_phone_sales)
print("Home Appliance Sales", home_appliance_sales)

if smart_phone_sales > home_appliance_sales:
    print("SBI will market offline outside the Smart Phone Stores")
else:
    print("SBI will market offline outside the Home Appliance Stores")
    print("We will distribute some Coupons to Home Appliance Stores as Well")

# PEP Standard
# Syntaxes to be followed in Python
# Refer this link: https://pep8.org/

