class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      word_mapping={}

      for word in strs:
        sorted_word=''.join(sorted(word))

        if sorted_word not in word_mapping:
            word_mapping[sorted_word]=[]

        word_mapping[sorted_word].append(word)


      return list(word_mapping.values())





        