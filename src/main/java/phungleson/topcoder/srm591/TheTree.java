package phungleson.topcoder.srm591;

public class TheTree {
	public int maximumDiameter(int[] counts) {
		if (counts == null || counts.length == 0) {
			return 0;
		}

		int maximumDiameter = counts.length;
		int diameter = 0;
		for (int index = 0; index < counts.length; index++) {
			int count = counts[index];

			if (count == 1) {
				diameter += counts.length - index;
				if (diameter > maximumDiameter) {
					maximumDiameter = diameter;
				}
				diameter = 0;
			} else {
				diameter += 2;
			}
		}

		if (diameter > maximumDiameter) {
			maximumDiameter = diameter;
		}

		return maximumDiameter;
	}
}
