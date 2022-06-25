; 7. Mull It Over

;; (a)
;; multiply x by y (without using the * operator).
;; (mulxy 3 4) -> 12           ; 12 = 3 + 3 + 3 + 3
;; (mulxy (- 3) (- 4)) -> 12   ; 12 = - ( -3 + -3 + -3 + -3 )
(define (mulxy x y)
  (cond ((< y 0) (- (mulxy x (- y))))
    ((= y 0) 0)
    (else (+ x (mulxy x (- y 1))))))



;; (b)
;; Multiply together a list of numbers.
;; (mul '(2 3 4 2)) -> 48
(define (mul s) (reduce mulxy s))

;; Evaluate an expression with only calls to * and numbers.
;; (mul-expr '(* (* 1 2) (* 3 (* 4 1 1) 2))) -> 48
(define (mul-expr e)
  (if (number? e) e
      (mul (map mul-expr (cdr e)))))



; (c)
;; Convert all calls to * to calls to mul in expression e.
;; (eval (*-to-mul '(* 1 (+ 2 3) (+ 4 5 (* 6 1))))) -> 75
(define (*-to-mul e)
  (if (not (list? e)) e
    (let ((op (car e)) (rest (cdr e)))
      (if (equal? op '*)
          (list 'mul (cons 'list (map *-to-mul rest)))
          (cons op rest)))))



; 8. Live Stream

;; Scale all elements of a stream by k.
(define (scale s k) (cons-stream (* (car s) k) (scale (cdr-stream s) k)))

;; A stream of 1 -2 4 -8 16 -32 64 -128 256 -512 ...
(define twos (cons-stream 1 (scale twos -2)))

;; Return a stream of all elements in s larger than all previous elements.
;; (up twos) -> a stream of 1 4 16 64 256 ...
(define (up s)
  (define (rest t)
    (if (> (car t) (car s))
      (up t)
      (rest (cdr-stream t))))
  (cons-stream (car s) (rest s)))



; 9. Macro Lens

;; A macro that creates a procedure from a partial call expression missing the last operand.
;; (define add-two (partial (+ 1 1))) ->  (lambda (y) (+ 1 1 y))
;; (add-two 3) -> 5 by evaluating (+ 1 1 3)
;;
;; (define eq-5 (partial (equal? (+ 2 3)))) ->  (lambda (y) (equal? (+ 2 3) y))
;; (eq-5 (+ 3 2)) -> #t by evaluating (equal? (+ 2 3) 5)
;;
;; ((partial (append '(1 2))) '(3 4)) -> (1 2 3 4)
(define-macro (partial call)
  `(lambda (y) ,(append call (list 'y))))