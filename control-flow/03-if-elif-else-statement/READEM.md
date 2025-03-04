# آموزش ساختار `if-elif-else` در پایتون

در این مستند به بررسی و توضیح ساختار شرطی `if-elif-else` در زبان برنامه‌نویسی پایتون می‌پردازی

## معرفی ساختار شرطی

ساختار شرطی به برنامه اجازه می‌دهد تصمیم‌گیری کرده و بر اساس شرایط مختلف، بخش‌های متفاوتی از کد را اجرا کند. در پایتون، از کلمات کلیدی `if`، `elif` و `else` برای ایجاد این ساختار استفاده می‌شود.

---

### ساختار `if`

شرط `if` برای بررسی یک شرط خاص استفاده می‌شود. اگر شرط درست باشد (True)، کدی که در بلاک `if` قرار دارد اجرا خواهد شد.

#### مثال:

```python
x = 10
if x > 5:
    print("x بزرگ‌تر از ۵ است")
```

```py
x = 3

if x > 5:
    print("x بزرگ‌تر از ۵ است")
elif x == 5:
    print("x برابر با ۵ است")
else:
    print("x کوچک‌تر از ۵ است")

```
