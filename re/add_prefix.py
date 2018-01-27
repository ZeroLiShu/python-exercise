#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import re

with open('test.txt.bak', 'w') as fp_w:
	lines_w = []
	with open('test.txt', 'r+') as fp_r:
		lines_r = fp_r.readlines()
		global_fn = re.compile(r'^void(.+)protobuf_(.+)')
		pb_class = re.compile(r'^class pve : public ::google::protobuf::Message {')
		include_end = re.compile(r'(.+)protoc_insertion_point(.+)')
		for line_r in lines_r:
			ret_global_fn = re.match(global_fn, line_r)
			ret_pb_class = re.match(pb_class, line_r)
			ret_include_end = re.match(include_end, line_r)
			new_line = line_r
			if (ret_global_fn):
				print(ret_global_fn.group())
				new_line = r'PTNNECFGDLL_PUBLIC_API ' + new_line 
			if (ret_pb_class):
				print(ret_pb_class.group())
				new_line = r'class PTNNECFGDLL_PUBLIC_API pve : public ::google::protobuf::Message {' + '\n';
			lines_w.append(new_line)
			if (ret_include_end):
				print(ret_include_end.group())
				lines_w.append(r'#include "ptnnecfgdll.h"' + '\n')
		fp_r.close()
	fp_w.writelines(lines_w)
	fp_w.close()