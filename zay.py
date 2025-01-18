def print_all_user():
	"""print all users"""
	print("\n")
	i=1
	for detail in user_detail:
		print(f"{i}-{detail["name"]}")
		i+=1

user_detail=[{
	"name":"mg mg",
	"password":"111",
	"money":5000
	},{
	"name":"hla hla",
	"password":"222",
	"money":3000
	},{
	"name":"thura",
	"password":"333",
	"money":70000
	}
]
	
instock=[{
	"product":"apple",
	"amount":50,
	"sell":550},
	{
	"product":"book",
	"amount":30,
	"sell":1100}
]
login_status=""

while login_status=="":
	login_name= input("enter your name: ")
	login_passowrd= input("enter your passowrd: ")
	choose=0
	user_number=0
	#log in status check in user
	if login_name=="admin" and login_passowrd=="123":
		login_status="admin"
	else:
		for detail in user_detail:
			if login_name==detail["name"] and login_passowrd==detail["password"]:
				login_status="user"
				print(f"\nlog in success")
				break
			user_number+=1
	#wrong password
	if login_status=="":
		if not login_name or not login_passowrd:
			login_status=None
		else:
			print("wrong user name or password")
	#admin log in
	elif login_status=="admin":
		print("welcome admin")
		while login_status=="admin":
			print("\n1-add new user \n2-remove user \n3-add money to user \n4-add new product \n5-add product \n6-log out")
			choose=int(input("choose one number(1-5): "))
			#admin add user
			if choose==1:
				new_usr_name=input("new user name: ")
				new_usr_password=input("new user password: ")
				new_usr_money=int(input("new user money: "))

				user_detail.append({
					"name":new_usr_name,
					"password":new_usr_password,
					"money":new_usr_money})

			elif choose== 2:
				print_all_user()

				#remove user from user_detail
				remove_inp=int(input("enter to remove user number: "))
				user_detail.pop(remove_inp-1)
				
			elif choose==3:
				print_all_user()
				#add money to user
				add_money_user=int(input("enter user to add money: "))
				add_amount=int(input("enter amount to add: "))
				user_detail[add_money_user-1]["money"]+=add_amount

			elif choose==4:
				#add new product
				product=input("enter product name: ")
				amount=int(input("enter product amount: "))
				sell=int(input("enter sell price: "))
				instock.append({
					"product":product,
					"amount":amount,
					"sell":sell})
			elif choose==5:
				i=1
				print("\n")
				#show products
				for product in instock:	
					print(f"{i}-{product["product"]} ({product["amount"]})")
					i+=1
				add_product=int(input("enter product to add: "))
				add_amount=int(input("enter add amount: "))
				instock[add_product-1]["amount"]+=add_amount
			elif choose==6:
			#admin log out
				login_status=""
	#user login
	elif login_status=="user":
		while login_status=="user":
			print("\n1-buy something \n2-transfer money to other \n3-change password \n4-delete account \n5-log out")
			choose=int(input("choose one number(1-5): "))
			#buy something
			if choose==1:
				buy=True
				while buy:
					i=1
					print("\n")
					#show products
					for product in instock:	
						print(f"{i}-{product["product"]} ({product["amount"]}) ({product["sell"]} MMK)")
						i+=1
					print(f"{i}-pay")
					#choose product
					buy_product=int(input("enter product to buy: "))
					if not buy_product==i:
						buy_amount=int(input("enter amount: "))
						
						#check is product sufficient
						if instock[buy_product-1]["amount"]>= buy_amount :
							bill=0
							#check is bill sufficient
							bill=instock[buy_product-1]["sell"]*buy_amount
							if bill >user_detail[user_number]["money"]:
								print(f"your balance is {user_detail[user_number]["money"]}")
							else:
								instock[buy_product-1]["amount"]-=buy_amount
								user_detail[user_number]["money"]-=instock[buy_product-1]["sell"]*buy_amount
								if instock[buy_product-1]["amount"]==0:
									instock.pop(buy_product-1)
						#reply product is not sufficient
						else:
							print(f"{instock[buy_product-1]["product"]} is less than {buy_amount}")
							
					else:
						buy=False
			elif choose==2:
				i=0
				num=0
				can_transfer=False
				#print all users
				print("\n")
				for detail in user_detail:
					if not i==user_number:
						num+=1
						print(f"{num}-{detail["name"]}")
					i+=1

				user_to_transfer_money=int(input("user to to transfer money: "))
				if user_to_transfer_money>user_number:
					user_to_transfer_money+=1	
				while not can_transfer:
					transfer_amount=int(input("enter amount to transfer: "))	
					if transfer_amount==0:
						can_transfer=True
					elif transfer_amount<user_detail[user_number]["money"]:
						can_transfer=True
						user_detail[user_number]["money"]-=transfer_amount
						user_detail[user_to_transfer_money-1]["money"]+=transfer_amount
						print(f"\n{transfer_amount} is transfer to {user_detail[user_to_transfer_money-1]["name"]} successfully")
					else:
						print("you have not sufficient amount")
			elif choose==3:
				password_condition=False
				while not password_condition:
					old_password=input("enter your old password: ")
					if old_password==user_detail[user_number]["password"]:
						new_password=input("enter your new password: ")
						new_password2=input("enter your new password again: ")
						if new_password==new_password2 and not new_password=="":
							user_detail[user_number]["password"]=new_password
							password_condition=True
						else:
							print("your password doesn't match")
					elif old_password=="":
						password_condition=True
					else:
						print("your password is incorrect")
			elif choose==4:
				user_detail.pop(user_number)	
				login_status=""
			#log out
			elif choose==5:
				login_status=""
				

