#! /usr/bin/python
# -*- coding: utf-8 -*-
import os
import re

def scan_pb_header_file_add_macro(pb_header_file, macro_define, include_file):
	with open(pb_header_file + r'.bak', 'w') as fp_w:
		lines_w = []
		with open(pb_header_file, 'r+') as fp_r:
			lines_r = fp_r.readlines()
			global_fn = re.compile(r'^void(.+)protobuf_(.+)')
			pb_class = re.compile(r'^class(.+)pve(.+):(.+)public(.+)')
			include_end = re.compile(r'(.+)protoc_insertion_point(.+)')
			for line_r in lines_r:
				ret_global_fn = re.match(global_fn, line_r)
				ret_pb_class = re.match(pb_class, line_r)
				ret_include_end = re.match(include_end, line_r)
				new_line = line_r
				if (ret_global_fn):
					print(ret_global_fn.group())
					new_line = macro_define + ' ' + new_line 
				if (ret_pb_class):
					print(ret_pb_class.group())
					new_line = r'class ' + macro_define + ' pve : public ::google::protobuf::Message {' + '\n';
				lines_w.append(new_line)
				if (ret_include_end):
					print(ret_include_end.group())
					lines_w.append(r'#include "' + include_file + '"' + '\n')
			fp_r.close()
		fp_w.writelines(lines_w)
		fp_w.close()

scan_pb_header_file_add_macro(r'test.txt', r'PTNNECFGDLL_PUBLIC_API', r'ptnnecfgdll.h')

os.remove('test.txt')
os.rename('test.txt.bak', 'test.txt')