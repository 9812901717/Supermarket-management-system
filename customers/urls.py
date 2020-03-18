from django.urls import path

from customers import views



app_name='customer_app'

urlpatterns=[
    # path('create/',views.create,name='create'),
    # path('',views.CustomerPagination.as_view(),name="customer_pagination"),#it assists to show page
    path('list/',views.index,name='list'),#assists to show data
    path('edit/<int:cid>/',views.edit,name='edit'),#here i pass primary key
    path('delete/<int:cid>/',views.delete,name='delete'),
    path('order/<int:cid>',views.cus_ord_view,name = 'view')    
]
