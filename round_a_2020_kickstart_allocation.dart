import 'dart:io';

void main() {
  String testCases = stdin.readLineSync();
  int t = int.parse(testCases);

  for (int i = 0; i < t; i++) {
    _solveCase(i + 1);
  }
}

void _solveCase(int cas) {
  String line = stdin.readLineSync();
  List<int> nb = _readIntegers(line);
  final int n = nb[0];
  int b = nb[1];

  line = stdin.readLineSync();
  List<int> costs = _readIntegers(line)..sort();

  int number = 0;
  for (int i = 0; i < n; i++) {
    if (b >= costs[i]) {
      number++;
      b -= costs[i];
    } else {
      break;
    }
  }

  print('Case #$cas: $number');
}

List<int> _readIntegers(String line) {
  List<String> line2 = line.split(' ')
    ..removeWhere((value) => value.trim().isEmpty);
  return line2.map((val) => int.parse(val)).toList();
}
