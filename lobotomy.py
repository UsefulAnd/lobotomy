from blessings import Terminal
from framework.commands.cmd import Run
import sys

if __name__ == '__main__':

    # Setup
    # terminal colors
    #
    t = Terminal()

    print (t.green("""

                  :                   :                  :
                 t#,                 t#,                t#,
            i   ;##W.   .           ;##W.              ;##W.
           LE  :#L:WE   Ef.        :#L:WE  GEEEEEEEL  :#L:WE             ..       : f.     ;WE.
          L#E .KG  ,#D  E#Wi      .KG  ,#D ,;;L#K;;. .KG  ,#D           ,W,     .Et E#,   i#G
         G#W. EE    ;#f E#K#D:    EE    ;#f   t#E    EE    ;#f         t##,    ,W#t E#t  f#f
        D#K. f#.     t#iE#t,E#f. f#.     t#i  t#E   f#.     t#i       L###,   j###t E#t G#i
       E#K.  :#G     GK E#WEE##Wt:#G     GK   t#E   :#G     GK      .E#j##,  G#fE#t E#jEW,
     .E#E.    ;#L   LW. E##Ei;;;;.;#L   LW.   t#E    ;#L   LW.     ;WW; ##,:K#i E#t E##E.
    .K#E       t#f f#:  E#DWWt     t#f f#:    t#E     t#f f#:     j#E.  ##f#W,  E#t E#G
   .K#D         f#D#;   E#t f#K;    f#D#;     t#E      f#D#;    .D#L    ###K:   E#t E#t
  .W#G           G#t    E#Dfff##E,   G#t      t#E       G#t    :K#t     ##D.    E#t E#t
 :W##########Wt   t     jLLLLLLLLL;   t        fE        t     ...      #G      ..  EE.
 :,,,,,,,,,,,,,.                                :                       j           t

    """))

    try:

        # Setup command
        # loop
        #
        run = Run()
        run.prompt = t.green("(lobotomy) ")
        run.ruler = t.green("-")
        run.cmdloop()

    except KeyboardInterrupt:
        sys.exit(0)