import 'package:flet/flet.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:my_pda_scanner/my_pda_scanner_mixin.dart';
import 'package:my_pda_scanner/my_pda_scanner_util.dart';
import 'dart:io';

class PdaListener extends StatefulWidget {
  Control? parent;
  late Control control;
  String text = "";

  PdaListener({
    super.key,
    required this.parent,
    required this.control,
  });

  @override
  _PdaListener createState() => _PdaListener();
}

class _PdaListener extends State<PdaListener>
    with MyPdaScannerMixin<PdaListener> {
  String data_code = "NULL";

  @override
  Widget build(BuildContext context) {
    var pda_code = widget.control.attrString("pda_code");
    var pda_action = widget.control.attrString("pda_action");
    var data_tag = widget.control.attrString("data_tag");
    MyPdaScannerUtil pdaScannerUtil = MyPdaScannerUtil();
    pdaScannerUtil.sendMessageToAndroid(pda_action!, data_tag!);
    TextEditingController _controller = TextEditingController.fromValue(
        TextEditingValue(text: "扫描到数据:$data_code"));
    Widget pda_control = TextField(controller: _controller);
    return constrainedControl(
        context, pda_control, widget.parent, widget.control);
  }

  @override
  Future<void> myPdaScannerCodeHandle(String code) async {
    /// 编写你的逻辑
    setState(() {
      data_code = code;
      widget.text = code;
    });
  }
}
