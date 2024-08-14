import 'package:flet/flet.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:my_pda_scanner/my_pda_scanner_mixin.dart';
import 'package:my_pda_scanner/my_pda_scanner_util.dart';

class PdaListener extends StatefulWidget {
  final Control? parent;
  final Control control;
  final List<Control> children;
  final bool parentDisabled;
  final bool? parentAdaptive;
  final FletControlBackend backend;

  const PdaListener(
      {super.key,
      this.parent,
      required this.control,
      required this.children,
      required this.parentDisabled,
      required this.parentAdaptive,
      required this.backend});

  @override
  _PdaListener createState() => _PdaListener();
}

class _PdaListener extends State<PdaListener>
    with MyPdaScannerMixin<PdaListener> {
  String _pda_code = "";
  late TextEditingController _controller;

  @override
  void initstate() {
    super.initState();
    _controller = TextEditingController();
  }

  @override
  Widget build(BuildContext context) {
    var pda_code = widget.control.attrs["pda_code"] ?? "";
    if (_pda_code != pda_code) {
      pda_code = _pda_code;
      _controller.text = _pda_code;
    }
    var pda_action = widget.control.attrString("pda_action");
    var data_tag = widget.control.attrString("data_tag");

    bool onChange = widget.control.attrBool("onChange", false)!;
    final ValueChanged<String>? _on_changed;

    MyPdaScannerUtil pdaScannerUtil = MyPdaScannerUtil();
    pdaScannerUtil.sendMessageToAndroid(pda_action!, data_tag!);

    Widget pda_control = TextFormField(
        controller: _controller,
        onChanged: (String value) {
          debugPrint(value);
          _pda_code = value;
          widget.backend
              .updateControlState(widget.control.id, {"value": value});
          if (onChange) {
            widget.backend
                .triggerControlEvent(widget.control.id, "change", value);
          }
        });

    return constrainedControl(
        context, pda_control, widget.parent, widget.control);
  }

  @override
  Future<void> myPdaScannerCodeHandle(String code) async {
    /// 编写你的逻辑
    setState(() {
      _pda_code = code;
    });
  }
}
