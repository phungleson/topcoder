package phungleson.topcoder.srm591

import phungleson.topcoder.srm591.TheTree

describe TheTree {
	describe "#maximumDiameter" {
		def tests {
		    |  counts 														|  maximumDiameter  	|
		    |  	#[3]   														|		2				|
		    |  	#[2, 2]   													|		4				|
		    |  	#[4, 1, 2, 4]   											|		5				|
		    |	#[4, 2, 1, 3, 2, 5, 7, 2, 4, 5, 2, 3, 1, 13, 6]				|		21				|
		    |	#[1]														|		1				|
		    |	#[1, 1, 1, 1, 1]											|		5				|
		    |	#[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
		    		1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
		    		1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]				|		50				|
		    |	#[324, 200]													|		4				|
		    |	#[253, 1, 663, 237, 218, 1, 1, 1, 1, 738, 977, 1, 295,
		    		1, 1, 839, 1, 1, 195, 908, 43, 44, 1, 1, 548, 1, 888,
		    		811, 434, 97, 888, 1, 181, 67, 621, 238, 1, 199, 1,
		    		182, 495, 28, 120, 1, 1]								|		46				|
		    |	#[269, 462, 1, 419, 306, 475, 941, 276, 630, 457, 730,
		    		139, 36, 964, 786, 49, 426, 86, 678, 635, 175, 511,
		    		301, 272, 897, 63, 181, 411, 561, 172, 58, 463, 629,
		    		332, 89, 885, 206, 791, 236, 372, 387, 22, 686, 278, 26]|		84				|
		    |	#[1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2]							|		16				|
		    |	#[2, 5, 1, 2, 10, 1]										|		8				|
  		}
 
		fact tests.forEach[subject.maximumDiameter(counts) => maximumDiameter]
	}
}