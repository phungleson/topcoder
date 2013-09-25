package phungleson.topcoder.srm591

describe PyramidSequences {
	describe "#distinctPairs" {
		def tests {
			|	a 	|	b	|	c	|
			|	1	|	2	|	3	|
  		}
 
		fact tests.forEach[subject.distinctPairs(a, b) => c]
	}
}