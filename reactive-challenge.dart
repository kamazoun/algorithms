import 'package:rxdart/rxdart.dart';
import 'dart:async';

Stream<List<int?>> samplem(List<Stream<int?>> sensors, Duration interval) {
  final List<Stream<int?>> safeSensors = sensors.map((sensor) {
    return sensor.transform(StreamTransformer<int?, int?>.fromHandlers(
      handleError: (error, stackTrace, sink) {
        sink.add(null);  // Add null instead of the error
      }
    ));
  }).toList();

  final Stream<List<int?>> allStreams = CombineLatestStream.list(safeSensors);
  return allStreams;
}

main() {
  final sensor1 = Stream<int>.fromIterable([1, 2, 3]).cast<int?>();
  final controller = StreamController<int>();

  controller.add(4);
  controller.add(5);
  controller.addError('AN ERROR');  // This error will be replaced by null
  controller.close();

  final sensorStreams = [sensor1, controller.stream.cast<int?>()];
  final snapshots = samplem(sensorStreams, Duration(seconds: 1));

  snapshots.listen(print);
}