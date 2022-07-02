; 7. Scheme

; 7.1
(define (deep-map fn lst)
	(cond ((null? lst) lst)
		((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
		(else (cons (fn (car lst)) (deep-map fn (cdr lst)))))
)


;; Test
; (deep-map (lambda (x) (* x x)) '(1 2 3))
; expects (1 4 9)
; (deep-map (lambda (x) (* x x)) '(1 ((4) 5) 9))
; expects (1 ((16) 25) 81)