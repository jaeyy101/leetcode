/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  const n = haystack.length;
  const m = needle.length;
  const LPS = computeLPS(needle);

  let i = 0;
  let j = 0;
  while (i < haystack.length) {
    if (haystack[i] == needle[j]) {
      i++;
      j++;
    }

    if (j === m) {
      return i - j;
    } else if (i < n && haystack[i] != needle[j]) {
      if (j != 0) {
        j = LPS[j - 1];
      } else {
        i++;
      }
    }
  }
  return -1;
};

/**
 *
 * @param {string} needle
 */
var computeLPS = (needle) => {
  const m = needle.length;

  let needle_len = 0;
  let i = 1;

  const LPS = Array(m).fill(0);
  while (i < m) {
    if (needle[i] == needle[needle_len]) {
      needle_len++;
      LPS[i] = needle_len;
      i++;
    } else {
      if (needle_len != 0) {
        needle_len = LPS[needle_len - 1];
      } else {
        i++;
      }
    }
  }

  return LPS;
};

console.log(strStr("sabababaab", "abaab"));
