# #!/usr/bin/env python
# from slugify import slugify
# import argparse
# import os
# import sys
#
# def main(args):
#
#     parser = argparse.ArgumentParser(
#     description='A tool slugifies file names for web use.')
#
#     parser.add_argument(
#         'path',
#         help='Path to directory to be renamed')
#
#     parser.add_argument(
#         '-r',
#         '--recurse',
#         default=False,
#         action='store_true',
#         help='Set if you want to recurse to children directory')
#
#     parser.add_argument(
#         '-d',
#         '--dry-run',
#         default=False,
#         action='store_true',
#         help='Does not commit changes, only shows the outcome')
#
#     parser.add_argument(
#         '-v',
#         '--verbose',
#         action='store_true',
#         help='Adds print out per item to be changed.'
#     )
#
#     namespace = parser.parse_args(args)
#
#     files = get_contents(namespace.path, namespace.recurse)
#
#     renamed = slugify_names(files)
#
#     renamed_count = rename_files(files, renamed, namespace.dry_run, namespace.verbose)
#
#     if namespace.dry_run:
#         print '\n{} file(s) would be renamed'.format(renamed_count)
#     else:
#         print '\n{} file(s) renamed'.format(renamed_count)
#
# def get_contents(path, recurse):
#     file_names = []
#     for item in os.listdir(path):
#         if os.path.isfile(os.path.join(path, item)):
#             file_names.append(os.path.join(path, item))
#         else:
#             if recurse:
#                 file_names += get_contents(os.path.join(path, item), recurse)
#
#     return file_names
#
# def slugify_names(path_list):
#     renamed = []
#     for path in path_list:
#         path_split = path.split('/')
#         filename = path_split[-1].split('.')
#         filename[0] = slugify(filename[0])
#         filename = '.'.join(filename)
#         renamed.append('/'.join(path_split[:-1] + [filename.lower()]))
#
#     return renamed
#
# def rename_files(files, renamed, dry, verbose):
#     renamed_count = 0
#
#     for i in range(len(files)):
#         if files[i] != renamed[i]:
#             renamed_count += 1
#
#             if verbose:
#                 print '\noriginal name: \t', files[i]
#                 print 'new name: \t', renamed[i]
#
#             if dry:
#                 continue
#
#             os.rename(files[i], renamed[i])
#
#     return renamed_count
#
# if __name__ == "__main__":
#    main(sys.argv[1:])
