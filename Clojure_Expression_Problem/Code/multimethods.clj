(ns multimethods)

;;; These can be in separate namespaces
(defrecord Circle [radius])
(defrecord Rectangle [height width])
(defrecord Square [side])

(defn get-type
  "Determine the type of the object"
  [obj]
  (condp = (class obj)
      multimethods.Circle ::circle
      multimethods.Rectangle ::rectangle
      multimethods.Square ::square
      ::unknown))

;;; Define the generic function which dispatches on the "dispatch-fn" function
(defmulti get-area get-type)

;;; Implementations

(defmethod get-area ::circle [c]
  (* Math/PI (* (:radius c) (:radius c))))

(defmethod get-area ::rectangle [r]
  (* (:height r) (:width r)))

(defmethod get-area ::square [s]
  (* (:side s) (:side s)))

;;;

(defn qsort [coll]
  "Sort a collection using QuickSort"
  (if-let [coll (seq coll)]
    (let [[pivot & tail] coll]
      (concat (qsort (filter #(< % pivot) tail))
              [pivot]
              (qsort (filter #(>= % pivot) tail))))
    []))
