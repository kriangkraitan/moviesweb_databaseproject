from django.urls import path

from . import views

urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
	
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('product/<str:pk>/', views.product, name="product"),
	#path('movie/<str:pk>/', views.movie, name="movie"),

	path('movie/<str:pk>/', views.movie, name="movie"),
	path('pdf/', views.GeneratePdf, name="pdf"),

	path('search/', views.searchbar, name="Search"),
	path('report/', views.ReportListAllOrder, name="Report"),
]