import 'package:flet/flet.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:my_pda_scanner/my_pda_scanner_mixin.dart';
import 'package:my_pda_scanner/my_pda_scanner_util.dart';

class PdaListener extends StatefulWidget {
  final Control? parent;
  final Control control;
  final FletControlBackend backend;

  const PdaListener(
      {super.key, this.parent, required this.control, required this.backend});
  @override
  _PdaListener createState() => _PdaListener();
}

class _PdaListener extends State<PdaListener> {
  String _pda_code = "";
  bool _start_listener = false;
  late TextEditingController _controller;
  MyPdaScannerUtil pdaScannerUtil = MyPdaScannerUtil();

  @override
  Widget build(BuildContext context) {
    var pda_code = widget.control.attrString("pda_code");
    _controller = TextEditingController();
    if (_pda_code != "") {
      pda_code = _pda_code;
      _controller.text = _pda_code;
    }
    var hint_text = widget.control.attrString("hint_text");

    var pda_action = widget.control.attrString("pda_action");
    var qr_data_tag = widget.control.attrString("qr_data_tag");
    var image_data_tag = widget.control.attrString("image_data_tag");
    var ocr_data_tag = widget.control.attrString("ocr_data_tag");
    var qr_data = widget.control.attrString("qr_data");
    var image_data = widget.control.attrString("image_data");
    var ocr_data = widget.control.attrString("ocr_data");

    Map<String, String> data_map = {
      "qr_data_tag": qr_data_tag!,
      "image_data_tag": image_data_tag!,
      "ocr_data_tag": ocr_data_tag!,
    };
    pdaScannerUtil.sendMessageToAndroid(data_map);
    bool onChange = widget.control.attrBool("onChange", false)!;
    bool start_listener = widget.control.attrBool("start_listener")!;
    final ValueChanged<String>? _on_changed;
    if (start_listener) {
      setState(() {
        _start_listener = true;
      });
    } else {
      setState(() {
        _start_listener = false;
      });
    }

    Widget pda_control = TextField(
        controller: _controller,
        decoration: InputDecoration(
          border: InputBorder.none, //无边框
          hintText: hint_text, //提示文本
        ),
        onChanged: (String value) {
          debugPrint(value);
          _pda_code = value;
          widget.backend
              .updateControlState(widget.control.id, {"pda_code": value});
          if (onChange) {
            widget.backend
                .triggerControlEvent(widget.control.id, "change", value);
          }
        });

    return constrainedControl(
        context, pda_control, widget.parent, widget.control);
  }

  @override
  Future<void> myPdaScannerCodeHandle(dynamic code) async {
    // 编写你的逻辑
    if (_start_listener) {
      String qr_data = code['qr_data'];
      String image_data = code['image_data'];
      String ocr_data = code['ocr_data'];

      setState(() {
        _pda_code = qr_data;
      });
      widget.backend.updateControlState(widget.control.id, {
        "pda_code": qr_data,
        "qr_data": qr_data,
        "image_data": image_data,
        "ocr_data": ocr_data,
      });
      widget.backend.triggerControlEvent(widget.control.id, "listener", code);
    }
  }
}
