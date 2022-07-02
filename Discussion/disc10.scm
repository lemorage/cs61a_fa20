; Questions

; 3.1 What Would Scheme Display?
#|
scm> (define a (+ 1 2))
a
scm> a
3
scm> (define b (- (+ (* 3 3) 2) 1)) ; 10
b
scm> (= (modulo b a) (quotient 5 3)) 
#t
|#


; 4.1 What Would Scheme Display?
#|
scm> (if (or #t (/ 1 0)) 1 (/ 1 0)) ; Short-circuits
1
scm> ((if (< 4 3) + -) 4 100)
-96
|#

; 4.1 Write a function that returns the factorial of a number.
(define (factorial x)
    (if (<= x 1) x (* x (factorial (- x 1))))
)

; 4.2 Write a function that returns the nth Fibonacci number.
(define (fib n)
    (if (<= n 1) n (+ (fib (- n 2)) (fib (- n 1))))
)
#|
scm> (fib 0)
0
scm> (fib 1)
1
scm> (fib 10)
55
|#



; 5.1 Write a function which takes two lists and concatenates them.
(define (my-append a b)
    (if (null? a) b (cons (car a) (my-append (cdr a) b)))
)
#|
scm> (my-append '(1 2 3) '(2 3 4))
(1 2 3 2 3 4)
|#

; 5.2 Short Questions

; Describe the difference between the following two Scheme expressions
;Expression A:
(define x (+ 1 2 3)) 
; Assignment: x is bound to 6

;Expression B:
(define (x) (+ 1 2 3))
; Define a function called x, takes zero argument and returns 6

; Write an expression that selects the value 3 from the list below.
(define s '(5 4 (1 2) 3 7))
(car (cdr (cdr (cdr s))))

; 5.3 Write a Scheme function that, duplicates every element in the list
(define (duplicate lst)
    (if (null? lst) nil (cons (car lst) (cons (car lst) (duplicate (cdr lst)))))
)

; 5.4  Write a Scheme function that, inserts the element into the list at that index.
(define (insert element lst index)
    (if (= index 0)
        (cons element lst)
        (cons (car lst) (insert element (cdr lst) (- index 1))))
)