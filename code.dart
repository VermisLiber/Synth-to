import 'package:nlp/nlp.dart';

void main() 
{
  String input = "The quick brwn fox jumped over the lazy dog.";
  List<String> tokens = NLProcessor.tokenize(input);
  List<String> tags = NLProcessor.tag(tokens);
  List<String> errors = checkForErrors(tokens, tags);
  if (errors.isNotEmpty) 
  {
    print("Potential errors found:");
    errors.forEach((error) => print(error));
  } 
  else
  {
    print("No errors found.");
  }
}
List<String> checkForErrors(List<String> tokens, List<String> tags) {
  List<String> errors = [];
  for (String token in tokens)
  {
    if (!checkSpelling(token)) 
    {
      errors.add("Misspelled word: $token");
    }
  }
  for (int i = 0; i < tags.length - 1; i++) 
  {
    String tag = tags[i];
    String nextTag = tags[i + 1];
    if (tag == "VB" && nextTag == "VBN") 
    {
      errors.add("Incorrect verb tense: ${tokens[i]} ${tokens[i + 1]}");
    }
    if (tag == "NN" && nextTag == "VBZ") {
      errors.add("Subject-verb agreement error: ${tokens[i]} ${tokens[i + 1]}");
    }
  }
  return errors;
}
bool checkSpelling(String word) 
{
  return true; 
}

