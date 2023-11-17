vertex(0..5).
edge(0, 2).
edge(0, 1).
edge(1, 2).
edge(1, 4).
edge(3, 2).
edge(3, 5).
edge(4, 5).

{scarecrow(X)} :- vertex(X).

secured(V1, V2) :- edge(V1, V2), scarecrow(V2).
secured(V2, V1) :- edge(V2, V1), scarecrow(V2).

:- edge(V1, V2), not secured(V1, V2).

#minimize { 1, V : scarecrow(V) }.

#show scarecrow/1.