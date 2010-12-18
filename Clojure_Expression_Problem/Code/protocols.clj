(ns protocols)

;;; These can be in separate namespaces
(defrecord Circle [radius])
(defrecord Rectangle [height width])
(defrecord Square [side])

;;; Grouping
(defprotocol Measurable
  (area [obj]))

;;; Implementations
(extend-protocol Measurable
  Circle
  (area [this] (* Math/PI (* (:radius this) (:radius this))))

  Rectangle
  (area [this] (* (:height this) (:width this)))

  Square
  (area [this] (* (:side this) (:side this))))
