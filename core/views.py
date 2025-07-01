from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    html = """
    <html>
        <head>
            <title>Python Full Test</title>
            <style>
                body { font-family: Arial, sans-serif; background: #f7fafc; color: #222; text-align: center; padding-top: 10vh; }
                .card { display: inline-block; background: #fff; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.08); padding: 2em 3em; }
                h1 { color: #2b6cb0; }
                p { color: #4a5568; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>🎉 Всё работает!</h1>
                <p>Ваш Django-проект успешно запущен.</p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html)