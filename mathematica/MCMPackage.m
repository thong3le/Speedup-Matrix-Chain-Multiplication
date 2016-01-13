BeginPackage[ "MCMPackage`"]

NestedParenthesesToTriangulatedPolygon::usage = "The function build a triangulated polygon that is equivalent to the given nested parentheses."
NestedParenthesesToTriangulatedPolygonwithLabel::usage = "build partition with label"
MatrixChainMultOpt::usage = "Find optimal solution for matrix chain multiplication problem."

Begin[ "Private`" ]

NestedParenthesesToTriangulatedPolygonHelper[s_, label_] := 
 Module[{chars = Characters[s], pos, rawtokens, tokens = {}, n, i, 
   edges},
  pos = Flatten[Position[chars, "A"]];
  n = Length[pos] + 1;
  tokens = 
   ReadList[StringToStream[s], Word, TokenWords -> {"(", "A", ")"}];
  tokens = Select[tokens, # != "A" &];
  edges = Table[i <-> (i + 1), {i, n - 1}];
  (*AppendTo[edges, n\[UndirectedEdge]1];*)
  
  SplitParentheses[tokens_] := 
   Module[{index, k, t, t1, len = Length[tokens]},
    t = Part[tokens, Range[2, len - 1]];
    len = len - 2;
    For[k = 1, k <= len - 1, k++,
     	t1 = Take[t, k];
     	If[Length[Select[t1, # == "(" &]] ==  
       Length[Select[t1, # == ")" &]], Return[{t1, Drop[t, k]}];];
     ];
    Return[{{}, {}}];
    ];
  
  ProcessEdges[tokens_] := 
   Module[{e, v1, v2, t1, t2, t = SplitParentheses[tokens]},
    	t1 = t[[1]];
    	t2 = t[[2]];
    	v1 =  ToExpression[First[Select[t[[1]], # != "(" && # != ")" &]]];
    	v2 =  
     ToExpression[Last[Select[t[[1]], # != "(" && # != ")" &]]] + 1;	
    	AppendTo[edges, v1 <-> v2];
    	v1 =  ToExpression[First[Select[t[[2]], # != "(" && # != ")" &]]];
    	v2 =  
     ToExpression[Last[Select[t[[2]], # != "(" && # != ")" &]]] + 1;	
    	AppendTo[edges, v1 <-> v2];
    	If[Length[t1] > 1, ProcessEdges[t1];];
    	If[Length[t2] > 1, ProcessEdges[t2];];
    ];
  ProcessEdges[tokens];
  circleLayout[n_] := 
   Table[{Cos[-2 \[Pi]/n i - \[Pi]/2], 
     Sin[-2 \[Pi]/n i - \[Pi]/2]}, {i, n}];
  Graph[Range[n], DeleteDuplicates[edges], 
   VertexLabels -> Table[i -> label[[i]], {i, n}], 
   VertexCoordinates -> circleLayout[n]]
  ]

NestedParenthesesToTriangulatedPolygon[s_] := 
  NestedParenthesesToTriangulatedPolygonHelper[s, 
   Range[Length[Flatten[Position[Characters[s], "A"]]] + 1]];

NestedParenthesesToTriangulatedPolygonwithLabel[s_, label_] :=
NestedParenthesesToTriangulatedPolygonHelper[s, label];

MatrixChainMultOpt[p_] := 
 Module[{MAX = 10^15, n = Length[p] - 1, ans, i, j, t, np},
  M = ConstantArray[MAX, {n, n}];
  S = ConstantArray[{}, {n, n}];
  subproblem[i_, j_] := Module[{k, q},
    If[M[[i, j]] < MAX, Return[M[[i, j]]];];
    If[i == j, M[[i, j]] = 0,
     For[k = i, k <= j - 1, k++,
       q = 
        subproblem[i, k] + subproblem[k + 1, j] + 
         p[[i]]*p[[k + 1]]*p[[j + 1]];
       If[q < M[[i, j]], M[[i, j]] = q;];
       ];
     ];
    Return[M[[i, j]]];
    ];
  ans = subproblem[1, n];
  For[i = 1, i <= n - 1, i++,
   For[j = i + 1, j <= n, j++,
     For[t = i, t <= j - 1, t++,
       If[
         M[[i, j]] == 
          M[[i, t]] + M[[t + 1, j]] + p[[i]]*p[[t + 1]]*p[[j + 1]], 
         AppendTo[S[[i, j]], t]];
       ];
     ];
   ];
  
  f[i_, x_, y_] := x[[i]] <> # & /@ y;
  g[x_, y_] := Flatten[f[#, x, y] & /@ Range[Length[x]]];
  
  getoptimal[i_, j_] := Module[{res, res1, temp, opt, k},
    res = {""};
    If[i == j, Return[{"A" <> ToString[j]} ], 
     	res = # <> "(" & /@ res;
     	opt = S[[i, j]];
              res1 = {};
     	For[k = 1, k <= Length[opt], k++,
                  temp  = g[res, getoptimal[i, opt[[k]]]];
                  temp = g[temp, getoptimal[opt[[k]] + 1, j]];
      	   temp = # <> ")" & /@ temp;
      	   res1 = Join[res1, temp];
             ];
     Return[res1];
     ];
    ];
  (*Print[M//TableForm];
  Print[S//TableForm];*)
  Print[ans];
  np = getoptimal[1, n];
  Print[np];
  NestedParenthesesToTriangulatedPolygonHelper[#, p] & /@ np // TableForm
  ]

End[]

EndPackage[]