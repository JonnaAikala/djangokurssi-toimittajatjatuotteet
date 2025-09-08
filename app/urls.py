from django.urls import path

from .views import productlistview, supplierlistview, addsupplier, addproduct
from .views import deleteproduct, confirmdeleteproduct, edit_product_get, edit_product_post, searchsuppliers
from .views import products_filtered, deletesupplier, confirmdeletesupplier, edit_supplier_get, edit_supplier_post
from .views import loginview, login_action, logout_action

urlpatterns = [
    # LANDING PAGE AFTER LOGIN
    # path('landing/', landingview),

    # Loginview and authentication method
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),




    # Products url's
    path('products/', productlistview),
    path('add-product/', addproduct),
    path('delete-product/<int:id>/', deleteproduct),
    path('confirm-delete-product/<int:id>/', confirmdeleteproduct),
    path('edit-product-get/<int:id>/', edit_product_get),
    path('edit-product-post/<int:id>/', edit_product_post),
    path('products-by-supplier/<int:id>/', products_filtered),

    # Supplier url's
    path('suppliers/', supplierlistview),
    path('add-supplier/', addsupplier),
    path('search-suppliers/', searchsuppliers),
    path('delete-supplier/<int:id>/', deletesupplier),
    path('confirm-delete-supplier/<int:id>/', confirmdeletesupplier),
    path('edit-supplier-get/<int:id>/', edit_supplier_get),
    path('edit-supplier-post/<int:id>/', edit_supplier_post),
]
