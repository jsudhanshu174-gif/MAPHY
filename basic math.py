class MAPHY:
    def __init__(self):
      pass

    def sum(self,data):
       total_sum=0;
       for x in data:
          total_sum=total_sum+x

       return total_sum  

    def add(self,a,b):
       return a+b
    def sub(self,a,b):
       return a-b
    def mul(self,a,b):
       return a*b
    def div(self,a,b):
       
       return a/b
    def rem(self,a,b):
       return a%b
    def product(self,data):
       total_product=1;
       for x in data:
          total_product=total_product*x
       return total_product    
    def power(self,a,b):
       if b==0:
          return 1
       ans=1
       while(b>0):
          ans=ans*a
          b=b-1
       return  ans
    def root(self,a,n=2):
       if a<0 and n%2==0:
          raise ValueError("NO REAL ROOT (┬┬﹏┬┬)")
       if a<0:
          return -((-a)**1/n)
       return a**1/n
    def abs(self,a):
       if a<0:
          return -a
       return a
    def fact(self,a):
       if a==0 or a==1:
        return 1
       return a*self.fact(a-1)
    def gcd(self, *args):
      
      if not args:
        return 0

      def two_gcd(a, b):
        while b != 0:
          a, b = b, a % b
        return self.abs(a)

      result = self.abs(args[0])
      for num in args[1:]:
        result = two_gcd(result, self.abs(num))
      return result

    def lcm(self, *args):
      
      if not args:
        return 0

      def two_lcm(a, b):
        if a == 0 or b == 0:
          return 0
        return self.abs(a * b) // self.gcd(a, b)

      result = self.abs(args[0])
      for num in args[1:]:
        result = two_lcm(result, self.abs(num))
      return result
    def max(self,data):
       max=data[0]
       for x in data[1:]:
          if max<x:
             max=x 
       return max     
    def min(self,data):
       Min=data[0]
       for x in data[1:]:
          if Min>x:
             Min=x  
       return Min
    def per(self,a,b):
       if b>a:
          return 0
       if a<0 or b<0:
          raise ValueError("possbilites can't negative ^_____^")
       return (self.fact(a))//(self.fact(a-b))
    def combination(self,a,b):
       if b>a:
          return 0
       if a<0 or b<0:
          raise ValueError("possbilites can't negative ^_____^")
       return (self.fact(a))//(self.fact(b)*(self.fact(a-b)))
    def primecheck(self,a):
       count=0
       i=1
       while(i*i<=a):
          if a%i==0:
             count=count+1
          if a/i !=i :
             count =count+1

          i=i+1    
               
       if count ==2:
          return True
       else:
          return False
    def exp(self, x):
      #e^x = 1 + x + {x^2}/{2!} + {x^3}/{3!} + \dots + {x^n}/{n!}
      sum_val = 1.0
      term = 1.0
      i = 1

      # Jab tak term ki value ekdum choti na ho jaye (precision achieve na ho jaye)
      while self.abs(term) > 1e-15:
        term = (term * x) / i
        sum_val += term
        i += 1
        # Infinite loop se bachne ke liye safety limit laga sakte hain
        if i > 500:
          break

      return sum_val

    def degree_to_radian(self, x):
      return x * (3.141592653589793 / 180.0)

    def radian_to_degree(self, x):
      return x * (180.0 / 3.141592653589793)

    def sin(self, x, is_degree=False):
      if is_degree:
        x = self.degree_to_radian(x)
      ans = x  # i = 0 ke liye pehla term x hota hai
      for i in range(1, 100):
        y = (((-1) ** i) * (x ** (2 * i + 1))) / self.fact(2 * i + 1)
        if self.abs(y) > 0.00001:
          ans = ans + y
        else:
          break
      return ans

    def cos(self, x, is_degree=False):
      if is_degree:
        x = self.degree_to_radian(x)
      ans = 1.0  # i = 0 ke liye pehla term 1 hota hai
      for i in range(1, 100):
        y = (((-1) ** i) * (x ** (2 * i))) / self.fact(2 * i)
        if self.abs(y) > 0.00001:
          ans = ans + y
        else:
          break
      return ans

    def tan(self, x, is_degree=False):
      # is_degree ko sin/cos handle kar lenge
      return self.sin(x, is_degree) / self.cos(x, is_degree)

    def cosec(self, x, is_degree=False):
      return 1 / self.sin(x, is_degree)

    def sec(self, x, is_degree=False):
      return 1 / self.cos(x, is_degree)

    def cot(self, x, is_degree=False):
      return self.cos(x, is_degree) / self.sin(x, is_degree)

    def sin_inverse(self, x):
      ans = x
      for i in range(1, 100):
        y = (
            self.fact(2 * i)
            / ((4**i) * ((self.fact(i)) ** 2) * (2 * i + 1))
        ) * (x ** (2 * i + 1))
        if self.abs(y) > 0.0000001:
          ans = ans + y
        else:
          break
      return ans

    def cos_inverse(self, x):
      return (3.141592653589793 / 2) - self.sin_inverse(x)

    def tan_inverse(self, x):
      return self.sin_inverse(x / (((x**2) + 1) ** 0.5))

    def sec_inverse(self, x):
      return self.cos_inverse(1 / x)

    def cosec_inverse(self, x):
      return self.sin_inverse(1 / x)

    def cot_inverse(self, x):
      return (3.141592653589793 / 2) - self.tan_inverse(x)
    def floor(self, x):
     
      int_val = int(x)
      if x < 0 and x != int_val:
        return int_val - 1
      return int_val

    def ceil(self, x):
    
      int_val = int(x)
      if x > 0 and x != int_val:
        return int_val + 1
      return int_val

    def round(self, x):
    
      if x >= 0:
        return self.floor(x + 0.5)
      else:
        return self.ceil(x - 0.5)
    def log(self,x):
     if x <= 0:
        raise ValueError("x must be greater than 0")

     z = (x - 1) / (x + 1)

     result = 0.0
     term = z

     for n in range(100):
        result += term / (2 * n + 1)
        term *= z * z

     return 2 * result


lo=MAPHY()
print(lo.log(10))