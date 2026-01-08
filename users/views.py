from django.http import HttpRequest
from django.shortcuts import render


def calculators_view(request: HttpRequest):
    query_params = request.GET
    result = None
    error = None

    if query_params:
        num1_raw = query_params.get("num1")
        num2_raw = query_params.get("num2")
        op = query_params.get("op")

        if not num1_raw or not num2_raw:
            error = "Iltimos, barcha sonlarni kiriting."
        elif op not in ["add", "sub", "mul", "div"]:
            error = "Noto'g'ri operator."
        else:
            try:
                n1 = float(num1_raw)
                n2 = float(num2_raw)
                if op == "add":
                    result = n1 + n2
                elif op == "sub":
                    result = n1 - n2
                elif op == "mul":
                    result = n1 * n2
                elif op == "div":
                    if n2 == 0:
                        error = "Nolga bo'lish mumkin emas!"
                    else:
                        result = round(n1 / n2, 2)
            except ValueError:
                error = "Faqat son kiriting!"

    return render(request, "calculator.html", {"result": result, "error": error})