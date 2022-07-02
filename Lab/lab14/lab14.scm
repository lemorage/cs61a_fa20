(define (split-at lst n)
  (cond 
    ((zero? n)
     (cons nil lst))
    ((> n (length lst))
     (cons lst nil))
    (else
     (cons (cons (car lst)
                 (car (split-at (cdr lst) (- n 1))))
           (cdr (split-at (cdr lst) (- n 1)))))))

(define (compose-all funcs)
  (lambda (number)
    (if (null? funcs)
        number
        ((compose-all (cdr funcs)) ((car funcs) number)))))
