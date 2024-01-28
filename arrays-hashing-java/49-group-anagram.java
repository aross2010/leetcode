import java.util.*;

class main {

    public static void main(String[] args) {

        List<List<String>> list = groupAnagrams(new String[]{"eat", "tea", "tan", "ate", "nat", "bat"});

    }

    public static List<List<String>> groupAnagrams(String[] strings) {
        Map<String, List<String>> map = new HashMap<>();

        for (int i = 0; i < strings.length; i++) {
            char[] str = strings[i].toCharArray();
            Arrays.sort(str);
            String sortedStr = new String(str);

            if (map.containsKey(sortedStr)) {
                map.get(sortedStr).add(strings[i]);
            } else {
                map.put(sortedStr, new ArrayList<>());
            }
        }

        return new ArrayList<>(map.values());

        
        
      

        
    }
    
}
