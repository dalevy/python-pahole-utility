
#!/usr/bin/python

import sys
import subprocess as subp
import getopt

DEFAULT_DEBUG_IMAGE_LOCATION = "/usr/lib/debug/boot/"
_default_loc = DEFAULT_DEBUG_IMAGE_LOCATION #convenience

#The list of modules to output for each kernel image. Modify this to output more or less modules
_module_list = [
        "cred",
        "dentry",
        "dentry_operations",
        "fdtable",
        "file",
        "fs_struct",
        "files_struct",
        "lock_class",
        "lockdep_subclass_key",
        "lock_class_key",
        "lockdep_map",
        "kernel_cap_struct",
        "mm_struct",
        "path",
        "qstr",
        "raw_spinlock",
        "spinlock",
        "task_io_accounting",
        "task_struct",
        "task_rss_stat",
        "timekeeper",
        "timespec",
        "vm_area_struct",
        ]

#reads a debug kernel image and outputs the required structs
def output_module(mod_name,kernel_name):
     p = subp.Popen(["pahole", "-C",mod_name,_default_loc+kernel_name], stdout=subp.PIPE)
     (output, err) = p.communicate()
     return output

def usage():
    print "usage: debug [-i kernel_image]"
    sys.exit(-1)

def main(argv):

    kernel_image =""

     #command line parsing
    try:
        opts, args = getopt.getopt(argv, "i:", ["image"])
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt == "-i":
            kernel_image = arg
        else:
            usage()

    print "Reading kernel image: ", kernel_image

    #module search and output
    for kernel_module in _module_list:
        result = output_module(kernel_module,kernel_image)
        print "Writing results for....", kernel_module
        with open(kernel_module+".txt","w") as out_file:
            out_file.write(result)


if __name__ =='__main__':
    argc = len(sys.argv)
    main(sys.argv[1:])
