import os
import sys
import argparse
import glob


def symlink(source, link_name):
    def symlink_ms(source, link_name):
            #os.system("""runas /user:administrator "mklink {link} {target}" """.format(
            os.system("mklink {link} {target}".format(
                link = link_name,
                target = source))

    os_symlink = getattr(os, "symlink", None)
    if callable(os_symlink):
        os_symlink(source, link_name)
    else:
        symlink_ms(source, link_name)

def link_files(source, dest):
    print 'linkin...' + source  + ' to ' + dest
    symlink(source, dest)


def main():
  parser = argparse.ArgumentParser()
  #parser.add_argument('overwrite')
  args = parser.parse_args()

  home = os.getenv('HOME', os.getenv('USERPROFILE'))
  print "home is: " + home
  
  dotfiles_root = os.path.abspath('.')

  print "dotfiles_root is: " + dotfiles_root 
  
  files = glob.glob(os.path.join(dotfiles_root, '*/*.symlink')) 

  overwrite_all = False
  backup_all = False
  skip_all = False

  for source in files:
    file_base = os.path.basename(source.replace('.symlink', ''))
    dest = os.path.join(home, '.' + file_base)  
    print dest
    if os.path.islink(dest) and os.path.realpath(dest) == source:
       print 'already in place: ' + dest
       continue

    if os.path.exists(dest):
       print 'files exists: ' + dest
       link_files(source, dest)
    else:
       link_files(source, dest)

if __name__ == "__main__":
  main()
