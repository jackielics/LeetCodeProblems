/*
 * @lc app=leetcode.cn id=11 lang=c
 *
 * [11] 盛最多水的容器
 */

// @lc code=start
int maxArea(int* height, int heightSize){
	// area = 0
	// for i in range(len(height)):
	// 	for j in range(i+1, len(height)):
	// 		area = max(area, min(height[i], height[j]) * (j-i))
	// return area\
	// 将上面代码转成C语言
	int area = 0;
	for (int i = 0; i < heightSize; i++) {
		for (int j = i + 1; j < heightSize; j++) {
			area = area > (height[i] < height[j] ? height[i] : height[j]) * (j - i) ? area : (height[i] < height[j] ? height[i] : height[j]) * (j - i);
		}
	}
	return area;
}
// @lc code=end

