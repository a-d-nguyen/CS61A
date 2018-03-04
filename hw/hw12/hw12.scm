(define (find s predicate)
  (cond ((null? s) #f)
  	((predicate (car s))
  		(car s))
  	(else (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))
)

(define (has-cycle s)
	(define (analyze begin end)
		(cond
			((null? begin) #f)
			((null? end) #f)
			((eq? begin end) #t)
			(else (analyze begin (cdr-stream end))))
	)
	(analyze s (cdr-stream s))
)

(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
