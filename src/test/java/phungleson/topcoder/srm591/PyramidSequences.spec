package phungleson.topcoder.srm591

describe PyramidSequences {
	describe "#distinctPairs" {
		def tests {
			|	a 	|	b			|	c			|
			|	3	|	4			|	6l			|
			|	3	|	5			|	5l			|
			|	43	|	76			|	895l		|
			|	2	|	1000000000	|	1000000000l	|
  		}
 
		fact tests.forEach[subject.distinctPairs(a, b) => c]
	}
}