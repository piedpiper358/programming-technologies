


import sys
import re

def extr_name(filename):
  """
  Вход: nameYYYY.html, Выход: список начинается с года, продолжается имя-ранг в алфавитном порядке.
  '2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' и т.д.
  """
  i = 0
  names = [filename[4:8]]
  top10 = [[], []]
  with open(filename, 'r') as file:
    for line in file:
      result = re.search("<tr align=\"right\"><td>([0-9]+)</td><td>([A-Z][a-z]+)</td><td>([A-Z][a-z]+)</td>", line)
      if result:
        names.append(result.group(2) + " " + result.group(1))
        names.append(result.group(3) + " " + result.group(1))
        if i < 10:
          top10[0].append(result.group(2))
          top10[1].append(result.group(3))
        i += 1
  return sorted(names), top10


def main():
  args = sys.argv[1:]

  if not args:
    print('use: [--file] file [file ...]')
    sys.exit(1)
  for arg in args:
    names, top10 = extr_name(arg)
    print(names)
    print(top10)
# для каждого переданного аргументом имени файла, вывести имена extr_name
# напечатать ТОП-10 муж и жен имен из всех переданных файлов



if __name__ == '__main__':
  main()

