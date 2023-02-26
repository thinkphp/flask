
# A very simple Flask App

from flask import Flask
from flask import render_template
from flask import redirect, url_for, request
import math
import random


app = Flask(__name__)

@app.route('/')

def index():

    out = "<h1 style='font-size: 70px;'>Web Development - <mark>Flask</mark></h1>"

    out += "<div style='color: lightgreen;font-size: 40px'><a href='/home'>Home</a> | <a href='/about'>About</a> | <a href='/projects'>Projects</a> | <a href='/github'>GitHub</a> | <a href='/contact'>Contact</a> </div>"

    out += "<h3>from flask import Flask</h3>"

    out += "<h3>from flask import render_template</h3>"

    out += "<h3>app = Flask(__name__)</h3>"

    out += "<h3>@app.route('/')</h3>"

    out += "<h3>def index():</h3>"

    out += "<h3>return 'Web App with Python Flask!'</h3>"

    out += "<h3>app.run(host='0.0.0.0', port=81)</h3>"

    out += ""

    return out

@app.route('/github')

def git():

    return "<h1 style='background-color: yellow; font-size: 100px'>http://thinkphp.github.io</h1>"

@app.route('/home')

def home():

    name = 'Adrian'

    return render_template('ironman.html', title='Welcome', username=name)

@app.route('/projects/golden/<int:num>')

def Golden_Ratio(num):

    ret = []

    N = num

    a, b = 0, 1

    ret.append(a)

    for i in range(2, N + 1):

        c = a + b

        ret.append( b / c )

        a, b = b, c

    out = "<h1 style='font-size: 100px'>Golden Ratio</h1><h1 style='background-color: yellow; font-size: 70px'>"

    out += '<br/> '.join(str(i) for i in ret)

    out += '</h1>'

    return out



@app.route('/projects/fib/<int:num>')

def fib(num):

    ret = []

    N = num

    a, b = 0, 1

    ret.append(a)

    i = 2

    while i <= N:

          ret.append(b)

          a, b = b, a + b

          i += 1

    out = "<h1 style='font-size: 100px'>Fibonacci Sequence</h1><h1 style='background-color: yellow; font-size: 70px'>"

    out += ', '.join(str(i) for i in ret)

    out += '</h1>'

    return out


@app.route('/projects')

def projects():

    return "<div style='font-size: 50px; padding: 20px; margin-left: 20px'><h1 style='background-color: yellow'>Algorithms Basics</h1><ol><li><a href='projects/insertsort/1234321'><mark>Insertion Sort</mark></li> <li><a href='projects/shellsort/38765213'><mark>ShellSort</mark></li> <li><a href='projects/bubblesort/100'><mark>Bubblesort</mark></a></li> <li><a href='projects/selectionbymin/100'><mark>Selectionbymin</mark></a></li>  <li><a href='projects/mergesort/100'><mark>Mergesort</mark></a></li> <li><a href='projects/golden/100'>Golden Ratio</a></li> <li><a href='projects/fib/1000'>Fibonacci</a></li><li><a href='projects/gcd/10/3'>Greater Common Divisor</a></li><li> <a href='projects/fta/10'>Fundamental Theorem of Arithmetic</a></li><li><a href='projects/lcm/88/12'>Lower Common Multiple</a></li> <li><a href='/projects/bisect/64'>Bisection Method</a></li><li><a href='projects/eratosthenes/1000'>Sieve of Eratosthenes</li> <li><a href='projects/permutation/3'>Permutation</li> <li><a href='projects/partition/4'>Partitions</li> <li><a href='projects/subsets/3'>Subsets</li> <li><a href='projects/bin/8'>toBin</li> <li><a href='projects/dec/1000'>toDec</li> <li><a href='projects/combinations/4/2'>Combinations</li> <li><a href='projects/arrangements/4/2'>Arrangements</li> <li><a href='projects/partitionNumber/4'>Partitions Number</li>  <li><a href='projects/cartesian/2/3/3'>Cartesian Product A x B x C</li> <li><a href='projects/cartesian/2/3'>Cartesian Product A x B</li>  <li><a href='projects/cartesian/3'>Cartesian Product A x A</li>  <li><a href='projects/goldbach/100'>Goldbach</li> <li><a href='projects/collatz/1234'>Collatz Sequence</li> <li><a href='projects/queens/5'>N Queens Puzzle</li> <li><a href='projects/quicksort'><mark>QuickSort</mark></li>  <li><a href='projects/knight'>Knight Puzzle</li> <li><a href='projects/maze'>Maze Puzzle</li> <li><a href='projects/iterator/spam'>IteratorReverse</li> <li><a href='projects/primes/100'>IteratorPrimes</li> <li><a href='projects/mountain/1234321'>Mountain</li> <li><a href='projects/checkorder/1234321'>Check Order Arr</li> <li><a href='projects/countingsort/1234321'><mark>Sorting By Counting</mark></li>  <li><a href='projects/depressionForm/54321234'>Depression Form Relief</li> <li><a href='projects/freq/38765213'>Frequency</li>  <li><a href='projects/jumpsearch/38765213'><mark>Jump Search</mark></li><li><a href='projects/heapsort/38765213'><mark>HeapSort</mark></li><li><a href='projects/bst/38765213'>Binary Search Tree</li> <li><a href='projects/linkedlist/38765213'>Singly Linked List</li> <li><a href='projects/lis/123456'>Longest Increasing Subsequence - O(n^2) DynamicP</li>  <li><a href='projects/lis2/123456'>Longest Increasing Subsequence - O(n log n) </li> <li><a href='projects/babyloniansqrt/4'>Babylonian Square Root</li> <li><a href='projects/binarysearch/7'>Binary Search (Divide and Conquer)</li> <li><a href='projects/hanoi/3'>Towers of Hanoi (Divide et impera)</li> <li><a href='projects/longestconsecutive/5'>Longest Consecutive Subsequence</li> <li><a href='projects/knapsack/5'>Knapsack problem (Greedy) </li> <li><a href='projects/colormap/5'>Color Map problem (Greedy)</li> <li><a href='projects/picturecolor/5'>Photo Coloring (backtracking)</li> <li><a href='projects/collinearity/3'>Collinearity</li><li><a href='projects/areaoftriangle/3'> Area of Triangle Method</li> <li><a href='projects/equationline/-5/7/1/3'>Equation Of the Line Through 2 Points</li> </ol></div>"

@app.route('/about')

def about():

    return "<h1 style='background-color: yellow;font-size: 90px'>Adrian Statescu - Full Stack Developer</h1>"

@app.route('/contact')

def contact():

    return "<h1 style='background-color: yellow; font-size: 100px'>Contact: adrian@ironman.com</h1>"

@app.route('/projects/bisect/<int:num>')

def apps(num):

    result = bisection(0, num + 5, num)

    out = '<h1 style="background-color: orange;color: #fff; font-size: 170px">Bisection Method</h1><h1 style="font-size: 150px; color: mediumseagreen">sqrt (%d) = ' % num + '<mark>%f</mark></h1>' % result

    out += '<p>def bisection(lo, hi, a):</p>'

    out += '<p>EPS = 0.00001</p>'

    out += '<p>while not hi - lo <= EPS:</p>'

    out += '<p>m = (lo + hi) / 2.0</p>'

    out += '<p>x = lo * lo - a</p>'

    out += '<p>y = m * m - a</p>'

    out += '<p>if x > 0 and y < 0 or x < 0 and y > 0:</p>'

    out += '<p>hi = m</p>'

    out += '<p>else:</p>'

    out += '<p>lo = m</p>'

    out += '<p>return m</p>'

    out += '<style>p{background-color: mediumseagreen; color: #fff;font-size: 70px}</style>'

    return out

def bisection(lo, hi, a):

    EPS = 0.00001

    while not hi - lo <= EPS:

        m = (lo + hi) / 2.0

        x = lo * lo - a

        y = m * m - a

        if x > 0 and y < 0 or x < 0 and y > 0:

            hi = m

        else:

            lo = m

    return hi

@app.route('/projects/eratosthenes/<int:num>')

def primes(num):

    ret = eratosthenes(num)

    res = '<h1 style="color: white; background-color: mediumseagreen; font-size: 150px">Sieve of Eratosthenes</h1>'

    res += '<h2 style="font-size: 100; background-color: yellow">'

    res += ', '.join(str(i) for i in ret)

    res += '</h2>'

    return res;


def eratosthenes( n ):

    sieve = [True for i in range(0, n + 1)]

    i = 2

    while i * i <= n:

         if sieve[ i ] is True:

             j = 2

             while i * j <= n:

                   multiply = i * j

                   sieve[ multiply ] = False

                   j += 1
         i += 1

    list = []

    for i in range(2, n + 1):

        if sieve[ i ] is True:

           list.append(i)

    return list

@app.route('/projects/partition/<int:num>')

def partition(num):

    global stack, ret, n

    n = num

    stack = [0] * (n + 1)

    ret = []

    _bk()

    out = '<h2 style="font-size: 100px; color: blue; font-family: Verdana">Partitions of a set</h2><h1 style="background-color: mediumseagreen; font-size: 80px;color: yellow">'

    out += '<br/>'.join(str(i) for i in ret)

    out += '<h1>'

    return out


@app.route('/projects/permutation/<int:num>')

def permutation(num):

    global stack, ret, n

    n = num

    stack = [0] * (n + 1)

    ret = []

    bk()

    out = '<h2 style="font-size: 100px; color: blue; font-family: Verdana">Permutation of a set</h2><h1 style="background-color: yellow; font-size: 80px">'

    out += '<br/>'.join(str(i) for i in ret)

    out += '<h1>'

    return out

def init():

    global stack, level

    stack[ level ] = 0

def succ():

    global level, stack, n

    if stack[level] < n:

       stack[level] += 1
       return True

    return False

def _succ():

    global level, stack, n

    if stack[level] < stack[level - 1] + 1:

       stack[level] += 1
       return True

    return False


def _valid():

    return True

def valid():

    global level, stack, n

    for i in range(1, level):

        if stack[i] == stack[level]:

           return False

    return True

def sol():

    global level, n

    return level == n

def _printf():

    global stack, n, ret

    out = ''

    mx = max(stack)

    for i in range(1, mx + 1):

        out += '{'

        for j in range(1, n + 1):

            if stack[j] == i:

                out += str(j) + ','

        out = out[:-1]
        out += '}'

    ret.append(out)

def printf():

    global stack, n, ret

    output = []

    for i in range(1, n + 1):

        output.append(stack[i])

    ret.append(output)


def bk():

    global level

    level = 1

    init()

    while level > 0:

        hs = True
        iv = False

        while hs is True and iv is False:

            hs = succ()

            if hs is True:

               iv = valid()

        if hs is True:

            if sol() is True:

               printf()

            else:

               level += 1
               init()

        else:

            level -= 1


def _bk():

    global level

    level = 1

    init()

    while level > 0:

        hs = True
        iv = False

        while hs is True and iv is False:

            hs = _succ()

            if hs is True:

               iv = _valid()

        if hs is True:

            if sol() is True:

               _printf()

            else:

               level += 1
               init()

        else:

            level -= 1

@app.route('/projects/subsets/<int:n>')

def subsets( n ):

    vec = [0] * ( n + 1 )

    s = 0

    sol = []

    sol.append('<h1 style="font-size: 100px;background-color: lightgreen">Subsets of a Set</h1><pre style="background-color: yellow;font-size: 80px">')

    while not s == n:

        vec[ n - 1 ] += 1

        for i in range(n - 1, -1, -1):

            if vec[ i ] > 1:

               vec[ i ] -= 2

               vec[ i - 1 ] += 1

        out = ''

        s = 0

        for i in range(0, n):

            if vec[ i ] == 1:

               s += 1

               out += str(i + 1) + ' '

        sol.append(out)

    sol.append('</pre>')

    return '<br/>'.join(str(i) for i in sol)

@app.route('/projects/bin/<int:n>')

def bin( n ):

    out = ['<h2 style="font-size: 140px;background-color: yellow">Decimal to Binary</h2><h1 style="font-size: 100px; color: mediumseagreen">']

    num = '%d (10) = ' % n

    out.append( num )

    for i in range(15, -1, -1):

        out.append((n>>i)&1)

    out.append('(2)</h1>')

    return ''.join(str(i) for i in out)

def _pow(a, b):
    p = 1
    for i in range(1, b + 1):
        p *= a
    return p

@app.route('/projects/dec/<int:n>')

def dec( n ):

    out = ['<h2 style="font-size: 140px;background-color: yellow">Binary to Decimal</h2><h1 style="font-size: 100px; color: mediumseagreen">']

    num = '%d (2) = ' % n

    out.append( num )

    base = 0

    dec = 0

    while n > 0:

        dec += n % 10 * _pow(2, base)

        base += 1

        n //= 10

    out.append( dec )

    out.append('(10)</h1>')

    return ''.join(str(i) for i in out)

def i():
    global s, l
    s[l] = s[l-1]

def su():
    global s, n, k, l
    if s[l] < n - k + l:
       s[l] += 1
       return True
    return False
def s_l():
    global l, k
    return l == k
def v():
    return True
def p():
    global s, l, r
    out = ''
    for i in range(1, l + 1):
        out += str(s[i]) + ' '
    r.append(out)
def b():
    global l
    l = 1
    i()
    while not l == 0:
        hs = True
        iv = False
        while hs is True and iv is False:
              hs = su()
              if hs is True:
                 iv = v()
        if hs is True:
            if s_l():
               p()
            else:
               l += 1
               i()
        else:
            l -= 1



@app.route('/projects/combinations/<int:N>/<int:K>')

def combinations( N, K ):
    global s, n, k, r
    n = N
    k = K
    r = []
    r1 = '<span style="background-color: yellow; font-size: 100px">Comb(%d, ' % n
    r2 = '%d)</span>' % k
    r3 = r1 + r2
    r.append(r3)
    r.append('<h1 style="background-color: lightgreen;font-size: 80px">')
    s = [0] * (k + 1)
    b()
    r.append('</h1>')
    return '<br/>'.join(str(i) for i in r)

# next Arrangements

def _i():
    global s, l
    s[l] = 0

def _su():
    global s, n, k, l
    if s[l] < n:
       s[l] += 1
       return True
    return False

def _v():
    global s, l
    for i in range(1, l):
        if s[i] == s[l]:
           return False
    return True
def _b():
    global l
    l = 1
    _i()
    while not l == 0:
        hs = True
        iv = False
        while hs is True and iv is False:
              hs = _su()
              if hs is True:
                 iv = _v()
        if hs is True:
            if s_l():
               p()
            else:
               l += 1
               _i()
        else:
            l -= 1

# Generate all arrangements
@app.route('/projects/arrangements/<int:N>/<int:K>')

def arrangements( N, K ):

    global s, n, k, r
    n = N
    k = K
    r = []
    r1 = '<span style="background-color: yellow; font-size: 100px">Arrange(%d, ' % n
    r2 = '%d)</span>' % k
    r3 = r1 + r2
    r.append(r3)
    r.append('<h1 style="background-color: lightgreen;font-size: 80px">')
    s = [0] * (k + 1)
    _b()
    r.append('</h1>')
    return '<br/>'.join(str(i) for i in r)

# Greatest Common Divisor using Euclid's Algorithm
@app.route('/projects/gcd/<int:a>/<int:b>')

def euclid(a, b):
    def _euclid(a, b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a
    ret = _euclid(a, b)
    ret1 = "<h1 style='color: #888; background-color: orange;font-size: 90px'>Greatest Common Divisor(%d ," % a
    ret2 = "%d) = " % b
    return ret1 + ret2 + str(ret) + "</h1>"

# Lowest Common Multiple using loop
@app.route('/projects/lcm/<int:a>/<int:b>')

def lcm(a, b):

    def euclid(a,b):
        while b != 0:
            r = a % b
            a = b
            b = r
        return a

    def _lcm(a, b):
        mx = max(a,b)
        lcm = mx
        while True:
            if lcm % a == 0 and lcm % b == 0:
                break
            lcm += 1

        return lcm

    #for debug
    #ret = (a * b) // euclid(a, b)
    ret = _lcm(a, b)
    ret1 = "<h1 style='color: #888; background-color: orange;font-size: 90px'>Lowest Common Multiple(%d, " % a
    ret2 = "%d) = " % b
    return ret1 + ret2 + str(ret) + "</h1>"


# generates all unique partitions of an integer.
# https://leetcode.com/discuss/interview-question/414064/google-count-integer-partitions
@app.route('/projects/partitionNumber/<int:number>')

def partitionsOfNumber( number ):

    global level, N, stack, sum, ret
    ret = []
    N = number
    sum = 0
    stack = [0] * (N + 1)

    def init():
        global stack, level

        if level == 1:
            stack[level] = 0
        else:
            stack[level] = stack[level-1] - 1

    def succ():
        global stack, level, N, sum

        if stack[level] < N - sum:
            stack[level] += 1
            return True
        else:
            sum -= stack[level-1]
            return False


    def valid():

        global stack, level, N, sum
        if stack[level] <= N - sum:
           sum += stack[level]
           return True
        else:
           return False

    def printf():
        global stack, level, ret, sum
        out = ""
        for i in range(1, level + 1):
            out += str(stack[i]) + " + "
        sum -= stack[level]
        out = out[:-2]
        ret.append(out)

    def sol():
        global sum, N
        return sum == N

    def bk():
        global level
        level = 1
        init()
        while not level == 0:

            hs = True
            iv = False

            while hs is True and iv is False:

                hs = succ()

                if hs is True:
                    iv = valid()

            if hs is True:
                if sol() is True:
                    printf()
                else:
                    level += 1
                    init()
            else:
                level -= 1

    bk()
    out = "<p style='font-size: 50px'>Count Integer Partitions. Given a positive integer n, find out how many ways of writing n as a sum of positive integers (Google Interview).</p><h1 style='font-size: 100px'>"
    out += '<br/>'.join(str(i) for i in ret)
    out += "</h1><p>created with Passion by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>"
    return out

# Fundamental Theorem of Arithmetic
@app.route('/projects/fta/<int:number>')

def fta( number ):

    i = 2

    N = number

    res = []

    res.append("<h1 style='font-size: 90px; background-color: cyan'>Fundamental Theorem of Arithmetic</h1><h1 style='font-size: 80px; background-color: yellow'>")

    num = "%d = " % number

    res.append(num)

    while not N == 1:

          fm = 0

          out = ""

          while N % i == 0:

                fm += 1

                N //= i

          if fm != 0:

             out += str(i) + "^" + str(fm) + " * "

          if N == 1:
                out = out[:-2]

          res.append(out)

          i += 1

    res.append("</h1>")

    res.append("<p>Created with PASSION by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>")

    return ''.join(str(i) for i in res)

# Collatz Sequence
@app.route('/projects/collatz/<int:number>')

def collatz( number ):

    N = number

    out = []

    first_out = "<h2 style='font-size: 100px; color: mediumseagreen; background-color: yellow'>Collatz Sequence</h2><h1 style='font-size: 120px'>%d" % number

    out.append(first_out)


    while not N == 1:

        if N & 1 != 0:

            N = 3 * N + 1

        else:

            N //= 2

        out.append(N)

    out.append("<p>Created with PASSION by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>")

    ret = ', '.join(str(i) for i in out)

    return ret

# Goldbach's conjecture
@app.route('/projects/goldbach/<int:number>')

def goldbach( number ):

    def isPrime(n):

        prime = True

        i = 2

        while i * i <= n and prime is True:

              prime = n % i != 0

              i +=1

        return prime

    middle = number // 2

    out = "<h1 style='font-size: 120px; color: mediumseagreen; background-color: yellow'>Goldbach's conjecture</h1><h2 style='font-size: 100px'>"

    for i in range(2, middle + 1):

        if isPrime(i) is True and isPrime(number - i) is True:

           out += str(i) + ' + ' + str(number-i) +' </br> '

    out += "</h1><p>Created with PASSION by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>"

    return out

# Cartesian
@app.route('/projects/cartesian/<int:A>/<int:B>/<int:C>')

def cartesian( A, B, C ):

    global N, vec, stack, ret

    vec = [0,A,B,C]
    N = 3
    stack = [0] * (N + 1)
    ret = ["<h2 style='font-size: 100px; background-color: yellow;color: mediumseagreen'>Cartesian Product N Sets A x B x C</h2><h1 style='font-size: 80px'> {"]

    def init():
        global stack, level
        stack[level] = 0

    def succ():
        global stack, level, vec
        if stack[level] < vec[level]:
           stack[level] +=1
           return True
        else:
           return False

    def valid():
        return True

    def sol():
        global N, level
        return N == level

    def printf():
        global stack, level, ret
        out = "("
        for i in range(1, level + 1):
            out += str(stack[i]) + ","
        out = out[:-1]
        out += ")"
        ret.append(out)

    def bk():
        global level

        level = 1
        init()

        while not level == 0:
            hs = True
            iv = False
            while hs is True and iv is False:
                  hs = succ()
                  if hs is True:
                     iv = valid()

            if hs is True:
                if sol() is True:
                   printf()
                else:
                   level += 1
                   init()
            else:
                level -= 1

    bk()
    ret.append("}")
    return ''.join(str(i) for i in ret)


@app.route('/projects/cartesian/<int:A>/<int:B>')

def productcartesian( A, B ):

    global N, vec, stack, ret

    vec = [0,A,B]
    N = 2
    stack = [0] * (N + 1)
    ret = ["<h2 style='font-size: 100px; background-color: yellow;color: mediumseagreen'>Cartesian Product A x B</h2><h1 style='font-size: 80px'> {"]

    def init():
        global stack, level
        stack[level] = 0

    def succ():
        global stack, level, vec
        if stack[level] < vec[level]:
           stack[level] +=1
           return True
        else:
           return False

    def valid():
        return True

    def sol():
        global N, level
        return N == level

    def printf():
        global stack, level, ret
        out = "("
        for i in range(1, level + 1):
            out += str(stack[i]) + ","
        out = out[:-1]
        out += ")"
        ret.append(out)

    def bk():
        global level

        level = 1
        init()

        while not level == 0:
            hs = True
            iv = False
            while hs is True and iv is False:
                  hs = succ()
                  if hs is True:
                     iv = valid()

            if hs is True:
                if sol() is True:
                   printf()
                else:
                   level += 1
                   init()
            else:
                level -= 1

    bk()
    ret.append("}")
    return ''.join(str(i) for i in ret)

@app.route('/projects/cartesian/<int:A>')

def product_cartesian( A ):

    global N, vec, stack, ret

    vec = [0,A,A]
    N = 2
    stack = [0] * (N + 1)
    ret = ["<h2 style='font-size: 100px; background-color: yellow;color: mediumseagreen'>Cartesian Product A x A</h2><h1 style='font-size: 80px'> {"]

    def init():
        global stack, level
        stack[level] = 0

    def succ():
        global stack, level, vec
        if stack[level] < vec[level]:
           stack[level] +=1
           return True
        else:
           return False

    def valid():
        return True

    def sol():
        global N, level
        return N == level

    def printf():
        global stack, level, ret
        out = "("
        for i in range(1, level + 1):
            out += str(stack[i]) + ","
        out = out[:-1]
        out += ")"
        ret.append(out)

    def bk():
        global level

        level = 1
        init()

        while not level == 0:
            hs = True
            iv = False
            while hs is True and iv is False:
                  hs = succ()
                  if hs is True:
                     iv = valid()

            if hs is True:
                if sol() is True:
                   printf()
                else:
                   level += 1
                   init()
            else:
                level -= 1

    bk()
    ret.append("}")
    return ''.join(str(i) for i in ret)

@app.route('/projects/queens/<int:N>')

def queens( N ):

    global Q, mat, stack

    Q = N

    mat = []

    stack = [0] * (Q + 1)

    for i in range(0, Q + 1):

        arr = []

        for j in range(0, Q + 1):

            arr.append(0)

        mat.append(arr)

    for i in range(0, Q + 1):

        mat[0][i] = i

    for j in range(0, Q + 1):

        mat[j][0] = j

    def succ():
        global level, stack, Q
        if stack[level] < Q:
           stack[level] += 1
           return True
        return False

    def init():

        global stack, level
        stack[level] = 0

    def valid():
        global stack, level
        for i in range(1, level):
            if stack[i] == stack[level] or abs(stack[i]-stack[level]) == abs(i - level):
                return False
        return True

    def sol():
        global level, Q
        return level == Q

    def printf():
        global stack, Q, mat
        for i in range(1, Q + 1):
            mat[i][stack[i]] = '<div style="background-color: yellow">1</div>'

    def bk():
        global level

        level = 1
        init()

        while not level == 0:

            hs = True
            iv = False

            while hs is True and iv is False:
                    hs = succ()
                    if hs is True:
                       iv = valid()
            if hs is True:
                if sol() is True:
                   printf()
                   break
                else:
                   level += 1
                   init()
            else:
                level -= 1




    bk()

    out = "<h1 style='font-size: 90px; background-color: yellow; color: mediumseagreen'>N Queens Puzzle</h1><table style='font-size: 100px;width: 100%; background-color: mediumseagreen;color: cyan'>"

    for i in range(0, Q + 1):

        out += "<tr>"

        out += ''.join('<td>' + str(j) + '</td>' for j in mat[i])

        out += "</tr>"

    out += "</table><style>tr, td {border: 3px solid cyan;text-align: center}p {font-size: 18px; color: green}</style>"

    out += "<p>Created with PASSION by <a href='http://adrianstatescu.ch'>Adrian Statescu</a></p>"

    return out

@app.route('/projects/quicksort')

def sort():

    return render_template('form.html')

@app.route('/projects/quicksort/inaction', methods = ['POST','GET'])

def inaction():

    if request.method == 'POST':

        user = request.form['numbers']

        return redirect(url_for('success',arr = user))

    else:

        user = request.args.get('numbers')

        return redirect(url_for('success',arr = user))

    return user

# Bubble Sort Method in Action. O(n^2) Complexity.
def bubblesort( arr ):

    finished = False

    swapped = False

    size = len(arr)

    while not finished:

            swapped = False

            for i in range(0, size - 1):

              if arr[i] > arr[i+1]:

                 arr[i], arr[i+1] = arr[i+1], arr[i]

                 swapped = True

            if swapped is True:

                size -= 1

            else:

                finished = True
    return arr

@app.route('/success/<arr>')

def success(arr):

   vec = arr.split(",")

   vec = list( map( int, vec ))

   mergesort( vec )

   return '<span>Sorted Array:</span><h1>%s</h1> <style> span,h1{ font-size: 100px; background-color: yellow; color: mediumseagreen} </style>' % ' '.join(str(i) for i in vec)

#Combo Sort in Action
def combosort( vec ):

    shrinkFactor = 1.3

    swapped = True

    size = len(vec)

    gap = size

    while gap > 1 or swapped is True:

        if gap > 1:

           gap = int(gap // shrinkFactor)

        swapped = False

        for i in range(0, size - gap):

            if vec[i] > vec[i+gap]:

                vec[i], vec[i+gap] = vec[i+gap], vec[i]

                swapped = True



#Quick Sort Method in Action using Divide Et Impera. Best Complexity
def quicksort( arr ):

    _quicksort(0, len( arr ) - 1, arr)

def _swap(i, j, vec):
    vec[i], vec[j] = vec[j], vec[i]

def _quicksort(lo, hi, vec):

    i = lo
    j = hi

    pivot = vec[(lo + hi) >> 1]

    while(i <= j):
        while vec[i] < pivot:
            i += 1
        while vec[j] > pivot:
            j -= 1
        if i <= j:
            _swap(i,j, vec)
            i += 1
            j -= 1
    if lo < j:
       _quicksort(lo, j, vec)
    if i < hi:
       _quicksort(i, hi, vec)

def merge(left, m, right, vec):

    i = left
    j = m + 1
    aux = []

    while i <= m and j <= right:

          if vec[i] < vec[j]:
             aux.append(vec[i])
             i += 1
          else:
             aux.append(vec[j])
             j += 1

    while i <= m:
          aux.append(vec[i])
          i += 1
    while j <= right:
          aux.append(vec[j])
          j += 1
    k = 0
    for i in range(left, right+1):
        vec[i] = aux[k];
        k += 1

def divideEtImpera(left, right, vec):

    if left < right:
            m = (left + right) >> 1
            divideEtImpera(left, m, vec)
            divideEtImpera(m + 1, right, vec)
            merge(left, m, right, vec)

def mergesort(vec):
    divideEtImpera(0, len(vec) - 1, vec)


class MyContainer:

    def __init__(self, data):

        self.data = data

        self.len = len(data)

        self.index = self.len

    def __iter__(self):

        return self

    def __next__(self):

        if self.index == 0:

            raise StopIteration

        self.index -= 1

        return self.data[ self.index ]


@app.route('/projects/iterator/<username>')

def myiterator(username):

    ob = MyContainer(username)

    l = [x for x in ob]

    out = "<span style='position: relative; left: 20%;font-size: 200px; background-color: yellow; color: mediumseagreen; font-weight: bold; font-family: verdana; padding: 10px; margin: 10px; text-align: center'>"
    out += ''.join(str(x) for x in l)
    out += "</span><h1>Iterator for looping over a sequence backwards</h1>"

    footer = "<p>Created with Passion by <a href='http://thinkphp.github.io'>Adrian Statescu</a></p>"

    SourceCode = """
    <h1 style='color: #000; background-color: yellow'>
    # Source Code </br>
    class Reverse: </br>

    def __init__(self, data): </br>

        self.data = data </br>

        self.len = len(data) </br>

        self.index = self.len </br>

    def __iter__(self): </br>

        return self </br>

    def __next__(self): </br>

        if self.index == 0: </br>

            raise StopIteration </br>

        self.index -= 1 </br>

        return self.data[ self.index ] </br>

        # Usage
        ob = Reverse("spam") </br>
        for c in ob: </br>
            print(c) </br>
    </h1>
    """

    return out + SourceCode + footer

class Primes:

    def __init__(self, n):

        self.n = n;

        self.data = self.agreggator()

        self.len = len(self.data)

        self.index = -1

    def agreggator(self):

        count = 1

        i = 2

        list = []

        while count <= self.n:

            if self.isPrime(i) is True:

                list.append(i)

                count += 1

            i += 1

        return list

    def __iter__(self):

        return self

    def __next__(self):

        if self.index == self.len - 1:

            raise StopIteration

        self.index += 1

        return self.data[ self.index ]

    def isPrime(self, n):

        i = 2

        prime = True

        while i * i <= n and prime is True:

              prime = n % i != 0
              i += 1

        return prime


@app.route('/projects/primes/<int:n>')

def iterator_primes( n ):

    ob = Primes(n)

    list = [x for x in ob]

    out = "<h1 style='background-color: yellow; font-size: 100px'>"

    out += ', '.join(str(x) for x in list)

    out += "</h1>"

    return out

def reverse(arr):
    i = 0
    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i +=1
        j -=1
    return arr

@app.route('/projects/mountain/<int:n>')

def mount( n ):

    arr = []

    while n:
        x = n % 10
        arr.append(x)
        n //= 10

    arr = reverse(arr)

    i = 0

    n = len(arr)

    while i < n - 1  and arr[i] < arr[i+1]:

        i += 1

    if i == 0 or i == n - 1:
        out = "<h1 style='background-color: lightgreen; font-size: 40px'>Not Aspect of Mountain</h1>" + ' '.join(str(i) for i in arr)
    else:
        aspect = True
        for j in range(i, n - 1):
            if arr[j] < arr[j+1]:
                aspect = False
                break

        if aspect is True:
            out = "<h1 style='background-color: lightgreen; font-size: 40px'>Aspect of Mountain</h1>" + '<h1>' +' '.join(str(i) for i in arr) + '</h1>'
        else:
            out = "<h1 style='background-color: lightgreen; font-size: 40px'>Not Aspect of Mountain</h1>" + '<h1>' +' '.join(str(i) for i in arr) + '</h1>'
    return out


@app.route('/projects/checkorder/<int:n>')

def checkTheOrderArr( n ):

    arr = []

    while n:
        x = n % 10
        arr.append(x)
        n //= 10

    arr = reverse(arr)

    i = 1

    n = len(arr)

    while i < n and arr[i] == arr[0]:
          i += 1

    if i == n:
        out = "<h1>Constant Sequence</h1>" + '<h1>' +' '.join(str(i) for i in arr) + '</h1>'
    else:
        if arr[i-1] < arr[i]:
            Asc = True
            for j in range(i, n - 1):
                if arr[j] > arr[j+1]:
                    Asc = False
                    break
            if Asc is True:
                out = "<h1>Ascending Order</h1>" + '<h1>' +' '.join(str(i) for i in arr) + '</h1>'
            else:
                out = "<h1>Unordered Sequence</h1>" + '<h1>' +' '.join(str(i) for i in arr) + '</h1>'
        elif arr[i-1] > arr[i]:
            Desc = True
            for j in range(i, n - 1):
                if arr[j] < arr[j+1]:
                    Desc = False
                    break
            if Desc is True:
                out = "<h1>Descending Order</h1>" + '<h1 style="background-color: yellow">' +' '.join(str(i) for i in arr) + '</h1>'
            else:
                out = "<h1>Unordered Sequence</h1>" + '<h1 style="background-color: lightgreen">' +' '.join(str(i) for i in arr) + '</h1>'

    return out

def countingsort(arr, n):

    b = [0] * (n + 1)

    c = [0] * (n + 1)

    for i in range(n):
        c[i] = arr[i]

    for i in range(n):
        for j in range(i):
            if c[j] < c[i]:
                b[i] += 1
            else:
                b[j] += 1
    for i in range(n):
        arr[b[i]] = c[i]

@app.route('/projects/countingsort/<int:n>')

def countingsorting( n ):

    arr = [9,8,7,6,-5,4,3,2,1,0,-1]

    input =  ' '.join(str(i) for i in arr)

    countingsort(arr, len(arr))

    output = ' '.join(str(i) for i in arr)

    return '<h2>Counting Sort</h2><h1 style="background-color: lightgreen; font-size: 40px">' + input + '</h1>' + '<br/>' + '<h1 style="background-color: yellow; font-size: 40px">'  + output + '</h1>'

def insertionsort( arr, n ):

    for i in range(1, n):
        aux = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= aux:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = aux

@app.route('/projects/insertsort/<int:n>')

def insertsorting(  n ):

    arr = [9,8,7,6,-5,4,3,2,1,0,-1]

    input =  ' '.join(str(i) for i in arr)

    insertionsort(arr, len(arr))

    output = ' '.join(str(i) for i in arr)

    code = "<pre style='font-size: 50px'>"

    code += """

def insertionsort( arr, n ):

    for i in range(1, n):
        aux = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= aux:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = aux

    """
    code += "</pre>"

    return '<h2>Insert Sort</h2><h1 style="background-color: lightgreen; font-size: 40px">' + input + '</h1>' + '<br/>' + '<h1 style="background-color: yellow; font-size: 40px">'  + output + '</h1>' + code


@app.route('/projects/depressionForm/<int:n>')

def depressionFormRelief( n ):

    arr = []

    while n:
        x = n % 10
        arr.append(x)
        n //= 10

    arr = reverse(arr)

    i = 0

    n = len(arr)

    while i < n - 1 and arr[ i ] > arr[ i + 1 ]:

          i += 1

    if i == 0 or i == n - 1:

       out = "<h1 style='background-color: lightgreen; font-size: 40px'>Not Aspect of Depression</h1>" + '<h1>' +' '.join(str(i) for i in arr) + '</h1>'

    else:

       while i < n - 1 and arr[i] < arr[i+1]:

             i += 1

       if i == n - 1:

         out = "<h1 style='background-color: lightgreen; font-size: 40px'>Aspect of Depression Relief</h1>" + '<h1>' +' '.join(str(i) for i in arr) + '</h1>'

       else:

         out = "<h1 style='background-color: lightgreen; font-size: 40px'>Not Aspect of Depression</h1>" + '<h1>' +' '.join(str(i) for i in arr) + '</h1>'

    return out

@app.route('/projects/freq/<int:n>')

def freq( n ):

    arr = []

    while n:
        x = n % 10
        arr.append(x)
        n //= 10

    arr = reverse(arr)

    size = len(arr)

    vec_str = " ". join(str(i) for i in arr)

    sort( arr )

    k = 0

    vec = [0] * ( size + 1 )

    frequency = [0] * ( size + 1 )

    vec[k] = arr[k]

    frequency[k] = 1

    for i in range(size-1):

        if arr[i] == arr[i+1]:

            frequency[k] += 1

        else:

            k += 1

            vec[k] = arr[i+1]

            frequency[k] = 1

    out = "<h1 style='background-color: yellow'>" + vec_str + "</h1>" + "<br/>"

    for i in range(k+1):

        if frequency[i] == 1:

            out += "Elementul %d apare o singura data" % (vec[i])

        else:

            out += "Elementul %d apare de %d ori" % (vec[i], frequency[i])

        out += "<br>"

    return out

def sort( arr ):

    n = len( arr )

    for i in range(1, n):

        aux = arr[i]
        j = i - 1

        while j >= 0 and arr[j] >= aux:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = aux

def _shellsort(arr, n):

    dists = [7,5,3,1]

    for d in dists:

        dist = d

        for i in range(dist, n):

            aux = arr[i]

            j = i - dist

            while j >= 0 and arr[j] >= aux:

                arr[j + dist] = arr[j]

                j -= dist

            arr[j + dist] = aux

@app.route('/projects/shellsort/<int:n>')

def shellsort( n ):

    arr = [9,8,7,6,-5,4,3,2,1,0,-1]

    input =  ' '.join(str(i) for i in arr)

    _shellsort(arr, len(arr))

    output = ' '.join(str(i) for i in arr)

    return '<h2>Shell Sort</h2><h1 style="background-color: lightgreen; font-size: 40px">' + input + '</h1>' + '<br/>' + '<h1 style="background-color: yellow; font-size: 40px">'  + output + '</h1>'


def _jumpsearch(vec, k):

    # define an array sorted order
    arr = vec

    key = k

    n = len( arr )

    jump = int( math.sqrt(n) )

    lo = 0

    hi = jump

    input = ' '.join(str(i) for i in arr)

    while hi < n and arr[hi] <= key:

          lo = hi

          hi += jump

          if hi > n:
             hi = n

    found = False

    for index in range(lo, hi):

        if arr[index] == key:

            found = True

            output = "Element %d is found at index %d" % (key, index)

            break

    if found is False:

            output = "The element %d Not Found" % (key)

    return "<h1 style='background-color: yellow'>" + input + "</h1><br/>" + "<h1 style='background-color: lightblue'>" + output + "</h1>"

@app.route('/projects/jumpsearch/<int:n>')

def jumpsearch(n):

    arr = [50, 60, 70, 80, 101, 200, 300]

    tests = [50, 60, 70, 81, 11, 200, 300, 1002]

    result = "<h2 style='font-size: 50px; background-color: green'>Jump Search Algorithm</h2>"

    for test in tests:

        result += _jumpsearch(arr, test)

        result += "<br/>"

    return "<h1>" + result + "</h1>"

def up( child ):

    parent = child // 2

    while parent != 0:

          if Heap[parent] >= Heap[child]:

             Heap[parent], Heap[child] = Heap[child], Heap[parent]

             child = parent

             parent = child // 2
          else:
              break

def down( parent ):

    while 2 * parent <= size:

          child = 2 * parent

          if 2 * parent + 1 <= size and Heap[2 * parent + 1] < Heap[2 * parent]:

              child += 1

          if Heap[parent] >= Heap[child]:

             Heap[parent], Heap[child] = Heap[child], Heap[parent]

             parent = child
          else:
             break

def insertHeap( elem ):

    global size

    size += 1

    Heap[ size ] = elem

    up( size )

@app.route('/projects/heapsort/<int:n>')

def heapsort(n):

    global Heap, size

    header = "<h1 style='background-color: yellow; font-size: 50px; text-align: center'>Heap Sort</h1><h2>Time and Space Complexity:</h2><ul><li>Worst case time: N LOG(N)</li><li>Average case time: N LOG(N)</li><li>Best case time: N LOG(N)</li></ul>"

    size = 0

    arr = [91,81,71,61,0,-5,4,3,21,1]

    input = " ".join(str(i) for i in arr)

    n = len(arr)

    Heap = [ 0 ] * (n + 1)

    for elem in arr:

        insertHeap( elem )

    out = []

    for i in arr:

        min = Heap[1]

        out.append(min)

        Heap[1] = Heap[size]

        size -= 1

        down(1)

    return header + "<h1 > Input: " + input + "</h1 > " + "<br/ > " + "<h1 >Output: " + " ".join(str(i) for i in out) + "</h1 > "

#
# Binary Search Tree - Data Structure
#
# Methods:
# - insert
# - search
# - delete
# - traversals (inorder, preorder, postorder)
#
# Time complexity Big O:
#      worst case O(log N)
#      average case O(log N)
#      best case O(log N)
#

class Node:

    def __init__(self, key):

        self.left = None

        self.right = None

        self.data = key

def insertBST(root, key):

    if root is None:

        root = Node(key)

    elif root.data < key:

        root.right = insertBST(root.right, key)

    elif root.data > key:

        root.left = insertBST(root.left, key)

    return root

def inorder(root):

    if root is not None:
        inorder(root.left)
        out.append(root.data)
        inorder(root.right)

def search(root, key):

    if root is None:
        return False
    elif root.data < key:
        return search(root.right, key)
    elif root.data > key:
        return search(root.left, key)
    else:
        return True

def mostlyLeftMin(root, key):
    if root.left is not None:
        root = root.left
    return root

def delete(root, key):

    if root is None:
        return root
    elif root.data < key:
        root.right = delete(root.right, key)
    elif root.data > key:
        root.left = delete(root.left, key)
    else:
        if root.left is None and root.right is None:
            root = None
        elif root.left is None:
             temp = root.right
             root = None
             return temp
        elif root.right is None:
             temp = root.left
             root = temp
             return temp
        elif root.left is not None and root.right is not None:
            temp = mostlyLeftMin(root.right)
            root.data = temp.data
            root.right = delete(root.right, temp.data)
    return root

@app.route('/projects/bst/<int:n>')

def bst( n ):

    global out

    header = "<h1 style='color: yellow; background: blue; font-size: 100px'> Binary Search Tree </h1>"

    out = []

    root = Node(8)

    arr = [ 10, 4, 3, -3, 7, 5, 14 ]

    for element in arr:

        insertBST(root, element)

    inorder(root)

    key = 7

    result = str(search(root, key))

    header +=  "<div style='color: blue; font-size: 50px'>Inorder: " + " ".join(str(i) for i in out) + "<br> Search: %d " % key + result + "<br>"

    out = []

    delkey = 7

    delete(root, delkey)

    inorder(root)

    header +="Deleted: %d" % delkey +"<br> Inorder: " + " ".join(str(i) for i in out) + "</div>"

    return header

class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head is None:
            self.head = Node2(value)
        else:
            c = Node2(value)
            c.next = self.head
            self.head = c

    def getFirst(self):

        return self.head.data

    def removeNode(self, key):

        if self.head.data == key:
            ptr = self.head
            self.head = self.head.next
            del ptr
        else:
            c = self.head
            while c.next.data != key:
                  c = c.next
            ptr = c.next
            c.next = ptr.next
            del ptr

    def display(self):
        c = self.head
        out = []
        while c is not None:
            out.append(c.data)
            c = c.next
        return out

    def reverse(self):

        out = []
        next = None
        prev = None
        curr = self.head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        self.head = prev

        c = self.head

        while c is not None:
            out.append(c.data)
            c = c.next

        return out

@app.route('/projects/linkedlist/<int:n>')

def linkedlist(n):

    header =  "<div style='font-size: 40px'><h1 style='color: yellow; background-color: blue; font-size: 50px'>Singly Linked List Data Structure</h1>"

    obj = SinglyLinkedList()

    for i in range(10):

        value = random.randrange(100)

        obj.add(value)

    out = obj.display()

    out2 = obj.reverse()

    node = obj.getFirst()

    delete = "<br/>Remove: " + str( node ) + "<br/>"

    obj.removeNode(node)

    out3 = obj.display()

    return header + "<span>List: </span>" +" ".join(str(i) for i in out) + "<br/><span>Reverse</span> " + " ".join(str(i) for i in out2) + delete + " ".join(str(i) for i in out3) + '</div>'

@app.route('/projects/lis/<int:n>')

def lis(n):

    # Input
    vec = [1, 7, 23, 8, 1, 33, 4, 10, 57, 81]

    # Time Complexity O(n^2) Dynamic Programming

    n = len(vec)

    # define an Array of lenghts
    L = [0] * (len(vec) + 1)

    L[n - 1] = 1

    for i in range(n - 1, -1, -1):

        max = 0

        for j in range(i + 1, n):

            if vec[ i ] < vec[j] and L[ j ] > max:

                   max = L[ j ]

        L[i] = 1 + max

    maxL = L[ 0 ]

    pos = 0

    for i in range(1, n):

        if L[i] > max:

            maxL = L[i]

            pos = i

    out = [vec[pos]]

    j = pos + 1

    while j < n:

        if vec[j] > vec[pos] and maxL-1 == L[j]:

           out.append(vec[j])

           maxL -= 1

        j+= 1

    return " ".join(str(i) for i in out)

@app.route('/projects/babyloniansqrt/<int:n>')

def babylon(n):

    x = n
    y = 1

    e = 0.000001
    while (x - y) > e:
        x = (x + y) / 2
        y = n / x

    result = "sqrt(%d) = %f" % (n,x)
    code = "<pre style='font-size: 50px'>"
    code += """
    Babylonian Square Root Algorithm

    x = n
    y = 1.0
    e = 0.000001
    while (x - y) > e:
        x = (x + y) / 2
        y = n / x

    @created by Adrian Statescu

    """
    code += "</pre>"
    return "<h1 style='background:yellow; font-size: 140px'>" + result + "</h1>" + code

def searchbin(lo, hi, arr, search):
    if lo > hi:
        return -1
    m = (lo + hi) >> 1
    if search > arr[m]:
        return searchbin(m+1, hi, arr, search)
    elif  search < arr[m]:
        return searchbin(lo, m-1, arr, search)
    else:
        return m

def searchbin2(lo, hi, arr, search):
    while lo <= hi:
        m = (lo+hi)>>1
        if search > arr[m]:
            lo = m + 1
        elif search < arr[m]:
            hi = m - 1
        else:
            return m
    return -1
@app.route('/projects/binarysearch/<int:n>')

def binarysearch(n):

    arr = [ 10,33,44,55,66,77,88,99,100 ]

    r = searchbin2(0, len(arr)-1,arr, n)

    if r == -1:

       result = "<span style='font-size: 100px; background-color: yellow'>Not Found!</span>"
    else:
       result = "<span style='font-size: 100px; background-color: yellow'>position: %d</span>"%r

    code = "<pre style='font-size: 50px'>"
    code += """
    Binary Search

    arr = [ 10,33,44,55,66,77,88,99,100 ]

    def searchbin(lo, hi, arr, search):
        if lo > hi:
            return -1
        m = (lo + hi) >> 1
        if search > arr[m]:
           return searchbin(m+1, hi, arr, search)
        elif  search < arr[m]:
           return searchbin(lo, m-1, arr, search)
        else:
           return m

    def searchbin2(lo, hi, arr, search):
        while lo <= hi:
           m = (lo+hi)>>1
           if search > arr[m]:
            lo = m + 1
           elif search < arr[m]:
            hi = m - 1
           else:
            return m
    return -1


    @created by Adrian Statescu
    """
    code += "</pre>"
    return result + code

def _hanoi(n, a, b, c):

    if n == 1:
        hanoiSol.append([a,b])
    else:
        _hanoi(n-1,a,c,b)
        hanoiSol.append([a,b])
        _hanoi(n-1,c,b,a)

@app.route('/projects/hanoi/<int:n>')

def hanoi(n):
    global hanoiSol
    hanoiSol = []
    _hanoi(n, 'a', 'b', 'c')
    out = ""
    for x,y in hanoiSol:
        out += "(" + str(x) + "," + str(y)  + ")"

    code = "<pre style='font-size: 50px'>"
    code += """
    Towers of Hanoi

    def _hanoi(n, a, b, c):
      if n == 1:
         print(a, b)
      else:
        _hanoi(n-1, a, c, b)
        print(a, b)
        _hanoi(n-1, c, b, a)

    @created by Adrian Statescu
    """
    code += "</pre>"
    return "<h1 style='background:yellow; font-size: 140px'>" + out + "</h1>" + code


@app.route('/projects/longestconsecutive/<int:n>')

def longestConsecutiveSubsequence(n):


    input = "000123456780000011111111012345000000"

    n = len(input)

    i = 0
    iCurr = 0
    iMax = 0
    lMax = 1

    while i <= n:

        if i - iCurr > lMax:
            lMax = i - iCurr
            iMax = iCurr

        iCurr = i
        while i < n - 1 and int(input[i]) + 1 == int(input[i+1]):
            i+=1
        i+=1

    output = "<h2>pos = %d<h2/><h3> length = %d</h3><h2 style='font-size: 80px'>Subsequence: "%(iMax, lMax)
    for i in range(iMax, iMax + lMax):
        output += str(input[i]) + " "
    output += "</h2>"

    code = "<pre style='font-size: 40px'>"
    code += """
    Longest Consecutive Subsequence

    input = "000123456780000011111111012345000000"

    n = len(input)

    i = 0
    iCurr = 0
    iMax = 0
    lMax = 1

    while i <= n:

        if i - iCurr > lMax:
            lMax = i - iCurr
            iMax = iCurr

        iCurr = i
        while i < n - 1 and int(input[i]) + 1 == int(input[i+1]):
            i+=1
        i+=1

    for i in range(iMax, iMax + lMax):

        output += str(input[i]) + " "


    @created by Adrian Statescu
    """
    code += "</pre>"
    return "<h1 style='background:yellow; font-size: 100px'>"+input+"</h1>" + output + code

@app.route('/projects/bubblesort/<int:n>')

def bubblesort(n):

    arr = [9,8,7,6,5,4,3,2,1,0]

    size = len(arr)

    finished = False

    while finished is not True:
        swapped = False
        for i in range(0, size-1):
            if arr[i] > arr[i+1]:
                xor = arr[i]^arr[i+1]
                arr[i] = xor^arr[i]
                arr[i+1] = xor ^ arr[i]
                swapped = True
        if swapped is True:
            size -= 1
        else:
            finished = True

    out = " ".join(str(x) for x in arr)

    code = "<pre style='font-size: 50px'>"
    code += """

    Bubble Sort Method

    def func(n):

        arr = [9,8,7,6,5,4,3,2,1,0]

        size = len(arr)

        finished = False

        while finished is not True:

          swapped = False

          for i in range(0, size-1):

            if arr[i] > arr[i+1]:

                xor = arr[i]^arr[i+1]
                arr[i] = xor^arr[i]
                arr[i+1] = xor ^ arr[i]
                swapped = True

        if swapped is True:

            size -= 1

        else:

            finished = True

    @created by Adrian Statescu
    """
    code += "</pre>"
    return "<h1 style='background:yellow; font-size: 140px'>" + out + "</h1>" + code

@app.route('/projects/selectionbymin/<int:n>')

def selectionbymin(n):

    arr = [9,8,7,6,5,4,3,1,-1,0]

    size = len(arr)

    for i in range(0, size-1):
        min = arr[i]
        ind = i
        for j in range(i+1, size):
            if arr[j] < min:
                ind =j
                min = arr[j]
        arr[ind] = arr[i]
        arr[i] = min

    out = " ".join(str(x) for x in arr)

    code = "<pre style='font-size: 50px'>"
    code += """
    Selection By Min Method

    arr = [9,8,7,6,5,4,3,1,-1,0]

    for i in range(0, size-1):
        min = arr[i]
        ind = i
        for j in range(i+1, size):
            if arr[j] < min:
                ind =j
                min = arr[j]
        arr[ind] = arr[i]
        arr[i] = min


    @created by Adrian Statescu
    """
    code += "</pre>"
    return "<h1 style='background:yellow; font-size: 140px'>" + out + "</h1>" + code

def _merge(lo, m, hi, arr):

    i = lo
    j = m + 1
    aux = []
    while i <= m and j <= hi:
        if arr[i] < arr[j]:
            aux.append(arr[i])
            i+=1
        else:
            aux.append(arr[j])
            j+=1
    while i <= m:
        aux.append(arr[i])
        i+=1
    while j <= hi:
        aux.append(arr[j])
        j+=1
    k=0
    for i in range(lo, hi+1):
        arr[i] = aux[k]
        k+=1

def _mergesort(lo, hi, arr):

    if lo < hi:
        m = (lo + hi) >> 1
        _mergesort(lo, m, arr)
        _mergesort(m+1, hi, arr)
        _merge(lo, m, hi, arr)

@app.route('/projects/mergesort/<int:n>')

def mergesort(n):

    arr = [0,8,7,6,5,4,3,2,12]

    _mergesort(0, len(arr)-1, arr)

    out = " ".join(str(x) for x in arr)

    code = "<pre style='font-size: 50px'>"
    code += """
    Merge Sort Method

    def _merge(lo, m, hi, arr):

        i = lo
        j = m + 1
        aux = []

        while i <= m and j <= hi:

          if arr[i] < arr[j]:

            aux.append(arr[i])
            i+=1

          else:

            aux.append(arr[j])
            j+=1

        while i <= m:

          aux.append(arr[i])
          i+=1

        while j <= hi:

          aux.append(arr[j])
          j+=1

       k=0
       for i in range(lo, hi+1):
          arr[i] = aux[k]
          k+=1

       def _mergesort(lo, hi, arr):

        if lo < hi:
           m = (lo + hi) >> 1
           _mergesort(lo, m, arr)
           _mergesort(m+1, hi, arr)
           _merge(lo, m, hi, arr)

    @created by Adrian Statescu
    """
    code += "</pre>"
    return "<h1 style='background:yellow; font-size: 140px'>" + out + "</h1>" + code

@app.route('/projects/knapsack/<int:n>')

def knapsack(n):

    capacity = 41

    matrix = [(1, 12.34, 123.99),(2, 23.45, 600.54),(3, 12.78, 90.67), (4, 9.34, 45.32)]

    input = "Capacity = <mark>%d </mark><br/>" % capacity

    for k in range(0, len(matrix)):

       input += str(matrix[k][0]) + " "+ str(matrix[k][1]) + " " + str(matrix[k][2]) + "<br/>"


    matrix = sorted(matrix, key=lambda object: object[1]/object[2])

    i = 0

    while capacity > 0:

        if capacity > matrix[i][1]:
            capacity -= matrix[i][1]
            i+=1
        else:
            capacity = -capacity

    output = ""

    for k in range(0, i):

        output += str(matrix[k][0]) + " "+ str(matrix[k][1]) + " " + str(matrix[k][2]) + " complete <br/>"

    if capacity < 0:
        output += str(matrix[i][0]) + " "+ str(matrix[i][1]) + " " + str(matrix[i][2]) + " "+ str(capacity) + "fractional <br/>"


    code = "<pre style='font-size: 50px'>"
    code += """
    Knapsack Problem

    Given a set of items, each with a weight and a value,
    determine a subset of items to include in a collection so that the total weight
    is less than or equal to a given limit and the  total value is as large as possible.

    class Object:
       def __init__(self, w, v, index):
          self.weight = float(w)
          self.value = float(v)
          self.index = int(index)
       def __repr__(self):
          return repr((self.index, self.weight, self.value))
       arr = []

       filepath = 'knapsack.in'
       with open(filepath) as fp:
            lines = fp.readlines()
            content = [x.strip() for x in lines]
            capacity = float(content[0])
            content.pop(0)
        i = 0
        for item in content:
        ob = item.split(" ")
        arr.append(Object(ob[0], ob[1], i))
        i+=1
        arr = sorted(arr, key = lambda x: x.weight/x.value)

        i = 0
        while capacity > 0:
          if capacity > arr[i].weight:
             capacity -= arr[i].weight
             i+=1
          else:
          capacity = -capacity

        for j in range(0, i):

            print("Object:%d. weight=%f value=%f completed"%(arr[j].index, arr[j].weight, arr[j].value))

        if capacity < 0:

            print("Object:%d. weight=%f value=%f %f fractional"%(arr[i].index, arr[i].weight, arr[i].value, capacity))

    @created by Adrian Statescu
    """
    code += "</pre>"

    return "<div style='background-color: lightgreen;font-size:50px'>" + input + "</div><div style='background-color: yellow;font-size:50px'>" + output + "</div>" + code


def plus(arr, n):

    return list(map(lambda x: x + 1, arr))


@app.route('/projects/colormap/<int:n>')

def mapColor(n):

    # we have 7 countries to color
    n = 7
    matrix = [[0,1,1,1,0,0,1],
              [1,0,1,1,0,0,0],
              [1,1,0,1,1,0,1],
              [1,1,1,0,1,0,1],
              [0,0,1,1,0,1,1],
              [0,0,0,0,1,0,1],
              [1,0,1,1,1,1,0]]

    Input = "<div style='background-color: lightgreen; font-size: 60px'>"

    for line in matrix:

        Input += " ".join(str(x) for x in line)

        Input += "<br/>"

    Input += "</div>"


    mapColors = []

    mapColors = [0] * (n)

    color = -1

    ok = True

    mapColors[0] = 0

    for i in range(1, n):

        ok = False

        color = -1

        while ok is not True:

              color += 1

              ok = True

              for j in range(0, i):

                  if 1 == matrix[j][i] and mapColors[j] == color:

                      ok = False
        mapColors[i] = color

    mapColors = plus(mapColors, 1)

    output = ""

    output += " ".join(str(element) for element in mapColors)

    code = "<pre style='font-size: 45px; padding: 10px; margin: 1px'>"
    code += """

Graph Coloring Problem based on Greedy Design

def plus(arr, n):

    return list(map(lambda x: x + 1, arr))

def func():
    # we have 7 countries to color
    n = 7
    matrix = [[0,1,1,1,0,0,1],
              [1,0,1,1,0,0,0],
              [1,1,0,1,1,0,1],
              [1,1,1,0,1,0,1],
              [0,0,1,1,0,1,1],
              [0,0,0,0,1,0,1],
              [1,0,1,1,1,1,0]]

    mapColors = []

    mapColors = [0] * (n)

    color = -1

    ok = True

    mapColors[0] = 0

    for i in range(1, n):

        ok = False

        color = -1

        while ok is not True:

              color += 1

              ok = True

              for j in range(0, i):

                  if 1 == matrix[j][i] and mapColors[j] == color:

                      ok = False
        mapColors[i] = color

    mapColors = plus(mapColors, 1)

    print(mapColors)

func()


    """
    code += "<pre>"

    return Input + "<div style='background-color: lightblue; font-size: 60px'>" + output + "</div>" + code



def coloring(i, j, color):

    global theMatrix

    if i >= 0 and j >= 0 and i < lines and j < cols and 1 == theMatrix[i][j]:


        theMatrix[i][j] = color

        coloring(i, j + 1, color)
        coloring(i, j - 1, color)
        coloring(i + 1, j, color)
        coloring(i - 1, j, color)

@app.route('/projects/picturecolor/<int:n>')

def photoColoring(n):

    global theMatrix, lines, cols

    theMatrix =[[4,6],[1,1,0,1,1,0],[1,1,0,0,0,1],[0,0,0,1,1,1],[1,1,0,0,1,0]]

    lines= int(theMatrix[0][0])

    cols = int(theMatrix[0][1])

    theMatrix.pop(0)

    Input = "<div style='background-color: lightgreen; font-size: 60px'>"

    for line in theMatrix:

        Input += " ".join(str(x) for x in line)

        Input += "<br/>"

    Input += "</div>"

    color = 2

    for i in range(0, lines):
        for j in range(0, cols):
            if theMatrix[i][j] == 1:
                coloring(i, j, color)
                color+= 1

    output = "<div style='background-color: yellow; font-size: 60px'>"

    for line in theMatrix:

        output += " ".join(str(x) for x in line)

        output += "<br/>"

    output += "</div>"

    code = "<pre style='font-size: 40px'>"
    code += """
    Photo Coloring Problem based on Backtracking

    def coloring(i, j, color):

        global matrix

        if i >= 0 and j >= 0 and i < n and j < m and 1 == matrix[i][j]:

        matrix[i][j] = color

        coloring(i, j + 1, color)
        coloring(i, j - 1, color)
        coloring(i + 1, j, color)
        coloring(i - 1, j, color)

    def func():

       global matrix, n, m

       filepath = "colorphoto.in"

       with open(filepath) as fp:

            lines = fp.readlines()

            content = [x.strip() for x in lines]

            lineCol = content[0].split(" ")

            n = int(lineCol[0])

            m = int(lineCol[1])

            content.pop(0)

            matrix = []

        for element in content:

           line = element.split(" ")

           line = [int(x) for x in line]

            matrix.append(line)

        for i in range(0, n):

            for j in range(0, m):

                print(matrix[i][j], end = " ")

            print(end = "")

        global color

        color = 2

        for i in range(0, n):

           for j in range(0, m):

           if matrix[i][j] == 1:

              coloring(i, j, color)

              color+=1

        print("")

        for i in range(0, n):

            for j in range(0, m):

            print(matrix[i][j], end = " ")

        print(end = "")

        func()

    @Created by Adrian Statescu
    """
    code += "</pre>"
    return Input + output + code

def module(n):
    if n < 0:
        return -n
    else:
        return n

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def computeArea(A,B,C):
    area = A.x*(B.y-C.y) + B.x *(C.y - A.y) + C.x*(A.y - B.y)
    area = module(area)/2
    return area

@app.route('/projects/areaoftriangle/<int:n>')

def areaoftriangle(n):

    A = Point(2,2)
    B = Point(2,8)
    C = Point(13,2)
    X = Point(-1,-1)
    Y = Point(1,1)
    Z = Point(3,3)
    area = computeArea(A,B,C)
    area2 = computeArea(X,Y,Z)

    output = "<div style='background-color: yellow; font-size: 60px'>Area of Triangle formed by points A, B and C = " + str(area) + "</div>"

    code = "<pre style='font-size: 41px'>"
    code += """
    Area of a Triangle

    As per area of triangle method, if three points
    P(x1,y1), P(x2,y2), R(x3, y3) are collinear,
    the area of the triangle formed by all three points
    P(x1,y1) Q(x2,y2) R(x3,y3) will be zero

    A = Point(2,2)
    B = Point(2,8)
    C = Point(13,2)
    X = Point(-1,-1)
    Y = Point(1,1)
    Z = Point(3,3)
    area = computeArea(A,B,C)
    area2 = computeArea(X,Y,Z)


def module(n):
    if n < 0:
        return -n
    else:
        return n

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def computeArea(A,B,C):
    area = A.x*(B.y-C.y) + B.x *(C.y - A.y) + C.x*(A.y - B.y)
    area = module(area)/2
    return area
    """
    code += "</pre"

    return output + code


@app.route('/projects/collinearity/<int:n>')

def collinearity(n):

    A = Point(2,2)
    B = Point(2,8)
    C = Point(13,2)
    X = Point(-1,-1)
    Y = Point(1,1)
    Z = Point(3,3)
    area = computeArea(A,B,C)
    area2 = computeArea(X,Y,Z)

    if area == 0.0:
       output = "<div style='background-color: yellow; font-size: 60px'>The points A,B,C are collinears</div>"
    else:
       output = "<div style='background-color: yellow; font-size: 60px'>The points A,B,Care not collinears</div>"

    if area2 == 0.0:
       output2 = "<div style='background-color: yellow; font-size: 60px'>The points X,Y,Z are collinears</div>"
    else:
       output2 = "<div style='background-color: yellow; font-size: 60px'>The points X,Y,Z are not collinears</div>"

    code = "<pre style='font-size: 41px'>"
    code += """
    Area of a Triangle

    As per area of triangle method, if three points
    P(x1,y1), P(x2,y2), R(x3, y3) are collinear,
    the area of the triangle formed by all three points
    P(x1,y1) Q(x2,y2) R(x3,y3) will be zero

    A = Point(2,2)
    B = Point(2,8)
    C = Point(13,2)
    X = Point(-1,-1)
    Y = Point(1,1)
    Z = Point(3,3)
    area = computeArea(A,B,C)
    area2 = computeArea(X,Y,Z)


def module(n):
    if n < 0:
        return -n
    else:
        return n

class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

def computeArea(A,B,C):
    area = A.x*(B.y-C.y) + B.x *(C.y - A.y) + C.x*(A.y - B.y)
    area = module(area)/2
    return area
    """
    code += "</pre"

    return output + output2 + code


def computeGradient(A, B):

    return (B.y - A.y) / (B.x - A.x)

@app.route('/projects/equationline/<int(signed=True):a>/<int(signed=True):b>/<int(signed=True):c>/<int(signed=True):d>')
def equationline(a,b,c,d):

    A = Point(a,b)
    B = Point(c,d)

    myPoints = "<div style='font-size:50px; background-color: yellow'>A(%d,%d) and B(%d,%d)</div>"%(a,b,c,d)
    slope = computeGradient(A,B)

    # y - y1 = m (x - x1)
    eq = myPoints + "<div style='background-color: lightblue; font-size: 70px;padding: 10px'>y - y1 = m (x - x1)</div>"
    theEq = "y - %f = %f * (x - %f)"% (A.y, slope, A.x)

    # y = mx - mx1 + y1
    # y = m x + y1 - m x1
    z = A.y - slope * A.x

    theEqSimplify = "y = %f x + %f" % (slope,z)
    code = "<pre style='font-size: 45px'>"
    code += """
#
# General Equation Line: ax + by + c = 0
# y - y1 = m (x - x1) with slope
# y = m x + c
# a = y1-y2
# b = x2 - x1
# c = x2y1 - x1y2
#
class Point():
    def __init__(self, x, y, name):
        self.name = name
        self.x = x
        self.y = y
    def __repr__(self):
        return self.name + '(' + str(self.x) + "," + str(self.y) + ')'

def computeSlope(x1, y1, x2, y2):
    return (y2-y1)/(x2-x1)

def func():

    A = Point(0,2,"A")
    B = Point(-1,4,"B")

    slope = computeSlope(A.x, A.y, B.x, B.y)

    print(slope)
    print(A)
    print(B)

    c = - slope * A.x + A.y

    print("y = %.2f * x + %.2f"%(slope,c))

    print("y - %.2f = %.2f x - %.2f %.2f "% (B.y, slope, slope, A.x))
func()
    """
    code += "</pre>"
    return eq + "<div style='background-color: lightgreen; font-size: 90px'>" + theEq + "</div><div style='background-color: lightblue;font-size: 100px'>" + theEqSimplify + "</div>" + code
