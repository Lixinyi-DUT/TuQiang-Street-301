
#lang racket

(provide (all-defined-out)) ;; so we can put tests in a second file

;; put your code below

(define (sequence low high stride)
   (if (> low high)
       null
       (cons low (sequence (+ low stride) high stride))))

(define (string-append-map xs suffix)
  (map (lambda (x) (string-append x suffix) ) xs))

(define (list-nth-mod xs n)
  (if (< n 0) (error "list-nth-mod: negative number")
      (if (null? xs)
          (error "list-nth-mod: empty list")
          (car (list-tail xs (remainder n (length xs)))))) )

(define (stream-for-n-steps s n)
  (if (= n 0) null
      (let ([p (s)])
      (cons (car p) (stream-for-n-steps (cdr p) (- n 1)) ))))

(define funny-number-stream
  (letrec ([f (lambda (x)
                (if (= (remainder x 5) 0)
                    (cons (- 0 x) (lambda () (f (+ x 1))))
                    (cons x (lambda ()(f (+ x 1))))))])
    (lambda () (f 1))))

(define dan-then-dog
  (letrec ([dan (lambda ()(cons "dan.jpg" dog))]
           [dog (lambda ()(cons "dog.jpg" dan))])
           dan))

(define (stream-add-zero s)
  (let ([p (s)])
  (lambda () (cons (cons 0 (car p)) (stream-add-zero (cdr p))) )))

(define (cycle-lists xs ys)
  (letrec ([f (lambda (n) (cons
                          (cons (list-nth-mod xs n) (list-nth-mod ys n))
                          (lambda () (f (+ n 1)))))])
    (lambda () (f 0))))


(define (vector-assoc v vec)
  (letrec ([len (vector-length vec)]
           [f (lambda (n) (if (= n (vector-length vec))
                              #f
                              (if (pair? (vector-ref vec n))
                                  (if (equal? (car (vector-ref vec n)) v)
                                      (vector-ref vec n)
                                      (f (+ n 1)))
                                      (f (+ n 1)))))])
           (f 0)))

(define (cached-assoc xs n)
  (letrec ([cache (make-vector n #f)]
           [pos 0])
    (lambda (v) (let ([ans (vector-assoc v cache)])
                               (if ans ans
                                   (let ([new-ans (assoc v xs)])
                                            (begin (vector-set! cache pos new-ans)
                                                   (set! pos (remainder (+ pos 1) n))
                                                   new-ans)))))))

(define-syntax while-less
  (syntax-rules (do)
               ([while-less e1 do e2]
                (letrec ([e e1]
                         [f (lambda() (if (< e2 e) (f) #t)) ])
                  (f)))))

