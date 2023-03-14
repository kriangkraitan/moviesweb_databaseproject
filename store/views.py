from django.shortcuts import render , redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory

from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder, render_to_pdf

from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db import connection

import webbrowser

@login_required(login_url='login')
def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	#movie = data['movie']
	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store/store.html', context)


@login_required(login_url='login')
def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

@login_required(login_url='login')
def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

@login_required(login_url='login')
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

@login_required(login_url='login')
def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

@login_required(login_url='login')
def product(request, pk):
	product = Product.objects.get(id=pk)
	
	if request.method == 'POST':
		product = Product.objects.get(id=pk)
		#Get user account information
		try:
			customer = request.user.customer	
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
		orderItem.quantity=request.POST['quantity']
		orderItem.save()

		return redirect('cart')

	context = {'product':product}
	return render(request, 'store/product.html', context)

def searchMatch(query, product):
	if query in product.name or query in product.title :
		return True
	else:
		return False

#@login_required(login_url='login')
#def search(request,pk):
#	products = Product.objects.filter(name=pk)
#	if len(Product.objects.filter(name=pk)) != 0:
#		products = Product.objects.filter(name=pk)
#		print(pk)
		#print(len(Product.objects.filter(name=pk)))

	#elif len(Product.objects.filter(title=pk)) != 0:
	#	products = Product.objects.filter(title=pk)

#	else:
#		products = Product.objects.all()
		#print(len(Product.objects.filter(name=pk)))
#	context = {'products':products}
#	return render(request, 'store/search.html', context)
	
def searchbar(request):
	
	if request.method == 'GET':
		search = request.GET.get('search')
		#print(type(search))
		#search_upper = search.upper()
		#search_lower = search.lower()
		#products =Product.objects.all()
		
		if len(Product.objects.all().filter(name__icontains=search)) != 0:
			products =Product.objects.all().filter(name__icontains=search)
			context = {'products':products}

		#elif len(Product.objects.all().filter(title__icontains=search)) != 0:
		#	products =Product.objects.all().filter(title__icontains=search)
		#	context = {'products':products}
		
		elif len(Producer.objects.all().filter(name__icontains=search)) !=0:
			producer = Producer.objects.get(name__icontains=search)
			producer_id = producer.id
			products =Product.objects.all().filter(producer_id=producer_id)
			context = {'products':products}
			#context = {'msg': "Producer"}
			#products =Product.objects.all().filter(producer_id__icontains=Producer.id)

		elif len(Genre.objects.all().filter(name__icontains=search)) !=0:
			genre = Genre.objects.get(name__icontains=search)
			genre_id = genre.id
			products =Product.objects.all().filter(genre_id=genre_id)

			context = {'products':products}

		elif len(Actor.objects.all().filter(name__icontains=search)) !=0:

			actor = Actor.objects.get(name__icontains=search)
			actor_id = actor.id
			action = Perform.objects.filter(actor_id = actor_id)
			n = len(action)
			products = Product.objects.all().filter(id=0)
			for i in range(n):

				action_movie = action[i].movie_id
				
				movie2 = Product.objects.all().filter(id=action_movie)
				products = products.union(movie2)
				print(products)

				#products =Product.objects.all().filter(id=action_movie)
			context = {'products':products}
			#context = {'msg': "Actor"}

		else :
			context = {'msg': "Can not find the movie you were looking for."}
		
		if search == "report":
			webbrowser.open('http://127.0.0.1:8000/report/')

		return render(request, 'store/search.html', context)
	

@login_required(login_url='login')
def movie(request, pk):
	movie = Movie.objects.get(id=pk)

	if request.method == 'POST':
		movie = Movie.objects.get(id=pk)
		#Get user account information
		try:
			customer = request.user.customer	
		except:
			device = request.COOKIES['device']
			customer, created = Customer.objects.get_or_create(device=device)

		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		orderItem, created = OrderItem.objects.get_or_create(order=order, movie=movie)
		orderItem.quantity=request.POST['quantity']
		orderItem.save()

		return redirect('cart')

	context = {'movie':movie}
	return render(request, 'store/movie.html', context)

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CreateCustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = [ 'first_name', 'last_name', 'email']


def registerPage(request):
	if request.user.is_authenticated:
		return redirect('store')
		
	else:
		form = CreateUserForm()
		#form2 = CreateCustomerForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			#form2 = CreateCustomerForm(request.POST)

			
			
			if form.is_valid() :#and form2.is_valid():
				form.save()

				#form2.save()
				userform = User.objects.get(username=request.POST['username'])
				customer, created = Customer.objects.get_or_create(user = userform,  first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
				customer.save()				
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'store/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('store')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('store')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'store/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(), 
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf/receipt.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

def ReportListAllOrder(request):
    
    with connection.cursor() as cursor:
        cursor.execute("""SELECT c.first_name as "Customer Name", SUM(oit.quantity)*20 as "Pay"
					FROM store_customer c JOIN store_order o on c.id = o.customer_id
					JOIN store_orderitem oit on o.id = oit.order_id
					group by c.first_name""")
                            
        row = dictfetchall(cursor)
        column_name = [col[0] for col in cursor.description]

    data_report = dict()
    data_report['data'] = row
    data_report['column_name'] = column_name

    return render(request, 'store/report.html', data_report)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [name[0].replace(" ", "_").lower() for name in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def CursorToDict(data,columns):
    result = []
    fieldnames = [name.replace(" ", "_").lower() for name in columns]
    for row in data:
        rowset = []
        for field in zip(fieldnames, row):
            rowset.append(field)
        result.append(dict(rowset))
    return result