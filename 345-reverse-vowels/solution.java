class Solution {
    public String reverseVowels(String s) {
        Set<Character> vowels = new HashSet<>();
        for (char c : "aeiouAEIOU".toCharArray()) {
            vowels.add(c);
        }

        char[] cList = s.toCharArray();
        int left = 0;
        int right = cList.length - 1;

        while (left < right) {
            if (!vowels.contains(cList[left])) {
                left++;
                continue;
            }
            if (!vowels.contains(cList[right])) {
                right--;
                continue;
            }
            // Swap the vowels
            char temp = cList[left];
            cList[left] = cList[right];
            cList[right] = temp;

            left++;
            right--;
        }
        return new String(cList);
    }
}