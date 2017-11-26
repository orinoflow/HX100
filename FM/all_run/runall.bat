cd ../rmbuffer
    rmbuffer.py dxj
    rmbuffer.py lyt

cd ../topfomat
    topfomat.py dxj allport nc
    topfomat.py lyt allport nc

    topfomat.py lyt loopcells nc
    topfomat.py dxj loopcells nc

cd ../setcutpoints
    cutpointsgen.py

cd ../topfomat
    tclgen.py
    fmenvgen.py

cd ../all_run
    pause
