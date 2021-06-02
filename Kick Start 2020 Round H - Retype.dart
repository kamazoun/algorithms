import 'dart:io';

void main() {
  int t = getInt()[0];

  for (int i = 0; i < t; i++) {
    _solveCase(i + 1);
  }
}

void _solveCase(int cas) {
  final nks = getInt();
  final int n = nks[0];
  final int k = nks[1];
  final int s = nks[2];
  
  print('Case #$cas: ${min(n+k, n+2*k-2*s)}');
}

int min(int a, int b){
return a < b ? a : b;
}

List<int> _readIntegers(String line) {
  List<String> line2 = line.split(' ')
    ..removeWhere((value) => value.trim().isEmpty);
  return line2.map((val) => int.parse(val)).toList();
}

List<int> getInt(){
return _readIntegers(stdin.readLineSync());
}
