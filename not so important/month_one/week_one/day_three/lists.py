def main():
    
    print(make_tags("i", "hello"))

def make_tags(tag, word):
    
  return f"<{tag}>{word}</{tag}>"

main()