package phungleson.topcoder.srm591;

import java.util.ArrayList;
import java.util.List;

/**
 * http://community.topcoder.com/stat?c=problem_statement&pm=12619
 * 
 * @author son
 */
public class PyramidSequences {

	public static class Pair {
		public Pair(int n, int m) {
			this.n = n;
			this.m = m;
		}

		int n;

		int m;
	}

	public long distinctPairs(int nMax, int mMax) {
		int nValue;
		int nPreviousValue = 0;
		int nInc = 1;
		int mValue;
		int mPreviousValue = 0;
		int mInc = 1;
		List<Pair> pairs = new ArrayList<>();

		while (true) {
			nValue = nPreviousValue + nInc;
			if (nValue == nMax) {
				nInc = -1;
			}
			if (nValue == 1) {
				nInc = +1;
			}

			mValue = mPreviousValue + mInc;
			if (mValue == mMax) {
				mInc = -1;
			}
			if (mValue == 1) {
				mInc = +1;
			}

			boolean exists = false;

			// for (Pair pair : pairs) {
			// if (pair.n == nValue && pair.m == mValue) {
			// exists = true;
			// break;
			// }
			// }

			// if (!exists) {
			// pairs.add(new Pair(nValue, mValue));
			// }

			if ((nValue == nMax && mValue == 1) ||
				(nValue == 1 && mValue == mMax) ||
				(nValue == nMax && mValue == mMax)) {
				break;
			}
			nPreviousValue = nValue;
			mPreviousValue = mValue;
		}

		return pairs.size();
	}
}
