from django.urls import include, path
from rest_framework import routers
from invoice_app.views import InvoiceViewSet

router = routers.DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # Remove other URL patterns if not needed for your project
]

# Add a catch-all pattern to redirect the root URL to the API endpoint
urlpatterns += [
    path('', include(router.urls)),
]
