1

   Abaqus 2024                                  Date 13-Jul-2025   Time 18:02:56
   For use by TRUSTEES OF COLUMBIA UNIVERSITY IN THE CITY OF NEW YORK under license from Dassault Systemes or its subsidiary.

                                                                                 
 faisal_Apply controlled displacement in this step                               
 STEP    1     INCREMENT     1     STEP TIME    0.00    


                        S T E P       1     C O U P L E D - T E M P E R A T U R E - D I S P L A C E M E N T   A N A L Y S I S


          faisal_Apply controlled displacement in this step                               

     AUTOMATIC TIME CONTROL WITH -
          A SUGGESTED INITIAL TIME INCREMENT OF                 60.0    
          AND A TOTAL TIME PERIOD OF                           3.480E+04
          THE MINIMUM TIME INCREMENT ALLOWED IS                1.000E-06
          THE MAXIMUM TIME INCREMENT ALLOWED IS                3.480E+04

          CREEP AND SWELLING EFFECTS ARE OMITTED IN THIS STEP

     THE SIZE OF THE TIME INCREMENT IS CONTROLLED BY -
          THE TEMPERATURE CHANGE PER INCREMENT NOT EXCEEDING            10.0    
          THE RATE DEPENDENCY WILL BE CONSIDERED IN THIS STEP

          CREEP AND SWELLING EFFECTS WILL BE IGNORED.

 CONVERGENCE TOLERANCE PARAMETERS FOR FORCE    
     CRITERION FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR DISP.    CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE FORCE                               1.000E-02
     AVERAGE FORCE     IS TIME AVERAGE FORCE    
     ALTERNATE CRIT. FOR RESIDUAL FORCE     FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO FORCE     RELATIVE TO TIME AVRG. FORCE         1.000E-05
     CRITERION FOR RESIDUAL FORCE     WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR DISP.    CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL FORCE     FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO FORCE     REL. TO TIME AVRG. MAX. FORCE        1.000E-05
     CRITERION FOR ZERO DISP.    RELATIVE TO CHARACTERISTIC LENGTH     1.000E-08

 CONVERGENCE TOLERANCE PARAMETERS FOR HEAT FLUX
     CRITERION FOR RESIDUAL HEAT FLUX FOR A NONLINEAR PROBLEM          5.000E-03
     CRITERION FOR TEMP.    CORRECTION IN A NONLINEAR PROBLEM          1.000E-02
     INITIAL VALUE OF TIME AVERAGE HEAT FLUX                           1.000E-02
     AVERAGE HEAT FLUX IS TIME AVERAGE HEAT FLUX
     ALTERNATE CRIT. FOR RESIDUAL HEAT FLUX FOR A NONLINEAR PROBLEM    2.000E-02
     CRITERION FOR ZERO HEAT FLUX RELATIVE TO TIME AVRG. HEAT FLUX     1.000E-05
     CRITERION FOR RESIDUAL HEAT FLUX WHEN THERE IS ZERO FLUX          1.000E-05
     CRITERION FOR TEMP.    CORRECTION WHEN THERE IS ZERO FLUX         1.000E-03
     CRITERION FOR RESIDUAL HEAT FLUX FOR A LINEAR INCREMENT           1.000E-08
     FIELD CONVERSION RATIO                                             1.00    
     CRITERION FOR ZERO HEAT FLUX REL. TO TIME AVRG. MAX. HEAT FLUX    1.000E-05

     VOLUMETRIC STRAIN COMPATIBILITY TOLERANCE FOR HYBRID SOLIDS       1.000E-05
     AXIAL STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS             1.000E-05
     TRANS. SHEAR STRAIN COMPATIBILITY TOLERANCE FOR HYBRID BEAMS      1.000E-05
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P>P0          5.000E-03
     SOFT CONTACT CONSTRAINT COMPATIBILITY TOLERANCE FOR P=0.0         0.100    
     CONTACT FORCE ERROR TOLERANCE FOR CONVERT SDI=YES                 1.00    
     DISPLACEMENT COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS           1.000E-05
     ROTATION COMPATIBILITY TOLERANCE FOR DCOUP ELEMENTS               1.000E-05

 EQUILIBRIUM WILL BE CHECKED FOR SEVERE DISCONTINUITY ITERATIONS

 TIME INCREMENTATION CONTROL PARAMETERS:
     FIRST EQUILIBRIUM ITERATION FOR CONSECUTIVE DIVERGENCE CHECK              4
     EQUILIBRIUM ITERATION AT WHICH LOG. CONVERGENCE RATE CHECK BEGINS         8
     EQUILIBRIUM ITERATION AFTER WHICH ALTERNATE RESIDUAL IS USED              9
     MAXIMUM EQUILIBRIUM ITERATIONS ALLOWED                                   16
     EQUILIBRIUM ITERATION COUNT FOR CUT-BACK IN NEXT INCREMENT               10
     MAXIMUM EQUILIB. ITERS IN TWO INCREMENTS FOR TIME INCREMENT INCREASE      4
     MAXIMUM ITERATIONS FOR SEVERE DISCONTINUITIES                            50
     MAXIMUM ATTEMPTS ALLOWED IN AN INCREMENT                                  5
     MAXIMUM DISCON. ITERS IN TWO INCREMENTS FOR TIME INCREMENT INCREASE      50
     MAXIMUM CONTACT AUGMENTATIONS FOR *SURFACE BEHAVIOR,AUGMENTED LAGRANGE   50
     CONSECUTIVE INCS MEETING TIME INTEG. TOL. FOR TIME INC. INCREASE          3
     CUT-BACK FACTOR AFTER DIVERGENCE                                 0.2500    
     CUT-BACK FACTOR FOR TOO SLOW CONVERGENCE                         0.5000    
     CUT-BACK FACTOR AFTER TOO MANY EQUILIBRIUM ITERATIONS            0.7500    
     CUT-BACK FACTOR AFTER TOO MANY SEVERE DISCONTINUITY ITERATIONS   0.2500    
     CUT-BACK FACTOR AFTER PROBLEMS IN ELEMENT ASSEMBLY               0.2500    
     INCREASE FACTOR AFTER TWO INCREMENTS THAT CONVERGE QUICKLY        1.500    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED                       1.500    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED (DYNAMICS)            1.250    
     MAX. TIME INCREMENT INCREASE FACTOR ALLOWED (DIFFUSION)           2.000    
     MINIMUM TIME INCREMENT RATIO FOR EXTRAPOLATION TO OCCUR          0.1000    
     CUT-BACK FACTOR WHEN TIME INTEGRATION ACCURACY TOL. EXCEEDED     0.8500    
     MAX. RATIO OF TIME INTEG. MEASURE TO TOL. FOR TIME INC. INCREASE 0.7500    
     INCREASE FACTOR FOR TIME INCREMENT WHEN POSSIBLE                 0.8000    
     MIN. TIME INC. INCREASE FACTOR IN LINEAR TRANSIENT PROBLEMS      0.9500    
     MAX. RATIO OF TIME INCREMENT TO STABILITY LIMIT                   1.000    
     FRACTION OF STABILITY LIMIT FOR NEW TIME INCREMENT               0.9500    
     TIME INCREMENT INCREASE FACTOR BEFORE A TIME POINT                1.000    
     GLOBAL STABILIZATION CONTROL IS NOT USED

          PRINT OF INCREMENT NUMBER, TIME, ETC., EVERY    1  INCREMENTS

     THE MAXIMUM NUMBER OF INCREMENTS IN THIS STEP IS                 1000000

          UNSYMMETRIC MATRIX STORAGE AND SOLUTION WILL BE USED

     LINEAR EXTRAPOLATION WILL BE USED

     CHARACTERISTIC ELEMENT LENGTH     0.333    

     DETAILS REGARDING ACTUAL SOLUTION WAVEFRONT REQUESTED

     DETAILED OUTPUT OF DIAGNOSTICS TO DATABASE REQUESTED

     PRINT OF INCREMENT NUMBER, TIME, ETC., TO THE MESSAGE FILE EVERY     1  INCREMENTS

     COLLECTING MODEL CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS

     COLLECTING STEP CONSTRAINT INFORMATION FOR OVERCONSTRAINT CHECKS


  INCREMENT     1 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT   60.0    
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  8ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       53.1       TIME AVG. FORCE        53.1    
 LARGEST SCALED RESIDUAL FORCE     -4.832E-13   AT NODE         27   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE     -4.832E-13
 LARGEST INCREMENT OF DISP.          2.10       AT NODE          1   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.         2.10       AT NODE          1   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  3.889E-08   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.          420.       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.         420.       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED   60.0    ,  FRACTION OF STEP COMPLETED  1.724E-03
 STEP TIME COMPLETED        60.0    ,  TOTAL TIME COMPLETED         60.0    


  INCREMENT     2 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT   60.0    
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  0ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       56.7       TIME AVG. FORCE        54.9    
 LARGEST SCALED RESIDUAL FORCE      6.537E-13   AT NODE         26   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE      6.537E-13
 LARGEST INCREMENT OF DISP.         0.136       AT NODE         60   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.        -2.00       AT NODE          1   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.852E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.          20.0       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.        -400.       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED   60.0    ,  FRACTION OF STEP COMPLETED  3.448E-03
 STEP TIME COMPLETED        120.    ,  TOTAL TIME COMPLETED         120.    


  INCREMENT     3 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT   60.0    
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  0ms

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       59.3       TIME AVG. FORCE        56.4    
 LARGEST SCALED RESIDUAL FORCE     -1.990E-13   AT NODE         23   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE     -1.990E-13
 LARGEST INCREMENT OF DISP.         0.137       AT NODE         60   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.        9.870E-04   AT NODE          9   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.852E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.          20.0       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.       -1.296E-44   AT NODE         43   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    
          TIME INCREMENT MAY NOW INCREASE TO     120.    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED   60.0    ,  FRACTION OF STEP COMPLETED  5.172E-03
 STEP TIME COMPLETED        180.    ,  TOTAL TIME COMPLETED         180.    


  INCREMENT     4 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT   120.    
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  2ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       64.5       TIME AVG. FORCE        58.4    
 LARGEST SCALED RESIDUAL FORCE     -1.705E-13   AT NODE         42   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE     -1.705E-13
 LARGEST INCREMENT OF DISP.         0.274       AT NODE         60   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.        1.087E-03   AT NODE          5   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.852E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.          40.0       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.       -1.296E-44   AT NODE         43   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    
          TIME INCREMENT MAY NOW INCREASE TO     240.    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED   120.    ,  FRACTION OF STEP COMPLETED  8.621E-03
 STEP TIME COMPLETED        300.    ,  TOTAL TIME COMPLETED         300.    


  INCREMENT     5 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT   240.    
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  1ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       74.8       TIME AVG. FORCE        61.7    
 LARGEST SCALED RESIDUAL FORCE      3.695E-13   AT NODE         23   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE      3.695E-13
 LARGEST INCREMENT OF DISP.         0.546       AT NODE         60   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.       -2.961E-03   AT NODE         53   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.852E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.          80.0       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.       -1.296E-44   AT NODE         39   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    
          TIME INCREMENT MAY NOW INCREASE TO     480.    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED   240.    ,  FRACTION OF STEP COMPLETED  1.552E-02
 STEP TIME COMPLETED        540.    ,  TOTAL TIME COMPLETED         540.    


  INCREMENT     6 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT   480.    
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  1ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       95.4       TIME AVG. FORCE        67.3    
 LARGEST SCALED RESIDUAL FORCE     -5.684E-13   AT NODE         38   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE     -5.684E-13
 LARGEST INCREMENT OF DISP.          1.09       AT NODE         60   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.        2.208E-03   AT NODE          5   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.852E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.          160.       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.       -1.296E-44   AT NODE         23   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    
          TIME INCREMENT MAY NOW INCREASE TO     960.    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED   480.    ,  FRACTION OF STEP COMPLETED  2.931E-02
 STEP TIME COMPLETED       1.020E+03,  TOTAL TIME COMPLETED        1.020E+03


  INCREMENT     7 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT   960.    
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  1ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       137.       TIME AVG. FORCE        77.2    
 LARGEST SCALED RESIDUAL FORCE      6.821E-13   AT NODE         43   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE      6.821E-13
 LARGEST INCREMENT OF DISP.          2.19       AT NODE         60   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.       -2.242E-03   AT NODE         13   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.852E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.          320.       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.       -1.296E-44   AT NODE         38   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    
          TIME INCREMENT MAY NOW INCREASE TO    1.920E+03

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED   960.    ,  FRACTION OF STEP COMPLETED  5.690E-02
 STEP TIME COMPLETED       1.980E+03,  TOTAL TIME COMPLETED        1.980E+03


  INCREMENT     8 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  1.920E+03
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  1ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       219.       TIME AVG. FORCE        94.9    
 LARGEST SCALED RESIDUAL FORCE     -9.095E-13   AT NODE         43   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE     -9.095E-13
 LARGEST INCREMENT OF DISP.          4.36       AT NODE         60   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.       -8.766E-03   AT NODE          4   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.852E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.          640.       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.       -1.296E-44   AT NODE         39   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    
          TIME INCREMENT MAY NOW INCREASE TO    3.840E+03

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  1.920E+03,  FRACTION OF STEP COMPLETED  0.112    
 STEP TIME COMPLETED       3.900E+03,  TOTAL TIME COMPLETED        3.900E+03


  INCREMENT     9 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  3.840E+03
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  1ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       384.       TIME AVG. FORCE        127.    
 LARGEST SCALED RESIDUAL FORCE     -3.638E-12   AT NODE         26   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE     -3.638E-12
 LARGEST INCREMENT OF DISP.          8.71       AT NODE         60   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.       -1.298E-02   AT NODE         36   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.852E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.         1.280E+03   AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.       -1.296E-44   AT NODE         38   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    
          TIME INCREMENT MAY NOW INCREASE TO    7.680E+03

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  3.840E+03,  FRACTION OF STEP COMPLETED  0.222    
 STEP TIME COMPLETED       7.740E+03,  TOTAL TIME COMPLETED        7.740E+03


  INCREMENT    10 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  7.680E+03
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  1ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       645.       TIME AVG. FORCE        179.    
 LARGEST SCALED RESIDUAL FORCE      3.837E-12   AT NODE         27   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE      3.837E-12
 LARGEST INCREMENT OF DISP.          16.8       AT NODE         60   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.        -2.70       AT NODE          1   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.461E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.         2.020E+03   AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.        -540.       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    
          TIME INCREMENT MAY NOW INCREASE TO    1.536E+04

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  7.680E+03,  FRACTION OF STEP COMPLETED  0.443    
 STEP TIME COMPLETED       1.542E+04,  TOTAL TIME COMPLETED        1.542E+04


  INCREMENT    11 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  1.536E+04
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  1ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       224.       TIME AVG. FORCE        183.    
 LARGEST SCALED RESIDUAL FORCE      1.160E-11   AT NODE         27   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE      1.160E-11
 LARGEST INCREMENT OF DISP.          35.9       AT NODE         57   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.        -36.5       AT NODE          1   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.179E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.        -3.260E+03   AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.       -7.300E+03   AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  1.536E+04,  FRACTION OF STEP COMPLETED  0.884    
 STEP TIME COMPLETED       3.078E+04,  TOTAL TIME COMPLETED        3.078E+04


  INCREMENT    12 STARTS. ATTEMPT NUMBER  1, TIME INCREMENT  4.020E+03
 
	UNSYMMETRIC NEW DIRECT SPARSE SOLVER RUNNING ON
 	1 HOST x 1 MPI RANK PER HOST x 1 THREAD PER RANK
        NUMBER OF EQUATIONS:  256
        NUMBER OF RHS:        1
        NUMBER OF FLOPS:      2.263e+06
        SOLVER ELAPSED TIME:  1ms
 

 ***WARNING: SOLVER PROBLEM. NUMERICAL SINGULARITY WHEN PROCESSING NODE 
             FAISAL_INSTANCE.34 D.O.F. 2 RATIO = 100.E+12     .

               CONVERGENCE CHECKS FOR EQUILIBRIUM ITERATION     1


 AVERAGE FORCE                       51.6       TIME AVG. FORCE        172.    
 LARGEST SCALED RESIDUAL FORCE     -2.482E-12   AT NODE         38   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
  CORRESPONDING RESIDUAL FORCE     -2.482E-12
 LARGEST INCREMENT OF DISP.          9.93       AT NODE         57   DOF  2
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO DISP.        -2.43       AT NODE          1   DOF  1
   INSTANCE: FAISAL_INSTANCE                                                                 
          THE FORCE     EQUILIBRIUM RESPONSE WAS LINEAR IN THIS INCREMENT

 AVERAGE HEAT FLUX                  1.852E-09   TIME AVG. HEAT FLUX   1.000E-02
 ALL HEAT FLUX RESIDUALS ARE ZERO
 LARGEST INCREMENT OF TEMP.        -1.340E+03   AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
 LARGEST CORRECTION TO TEMP.        -487.       AT NODE          1   DOF 11
   INSTANCE: FAISAL_INSTANCE                                                                 
          THERE IS ZERO HEAT FLUX EVERYWHERE
 

 ***WARNING: THERE IS ZERO HEAT FLUX EVERYWHERE IN THE MODEL BASED ON THE 
             DEFAULT CRITERION. PLEASE CHECK THE VALUE OF THE AVERAGE HEAT FLUX 
             DURING THE CURRENT ITERATION TO VERIFY THAT THE HEAT FLUX IS SMALL 
             ENOUGH TO BE TREATED AS ZERO. IF NOT, PLEASE USE THE SOLUTION 
             CONTROLS TO RESET THE CRITERION FOR ZERO HEAT FLUX.

 MAXIMUM NON-PRESCRIBED INCREMENT IN TEMPERATURE IS    0.00    

 ITERATION SUMMARY FOR THE INCREMENT:   1 TOTAL ITERATIONS, OF WHICH
   0 ARE SEVERE DISCONTINUITY ITERATIONS AND  1 ARE EQUILIBRIUM ITERATIONS.

 TIME INCREMENT COMPLETED  4.020E+03,  FRACTION OF STEP COMPLETED   1.00    
 STEP TIME COMPLETED       3.480E+04,  TOTAL TIME COMPLETED        3.480E+04


          THE ANALYSIS HAS BEEN COMPLETED



     ANALYSIS SUMMARY:
     TOTAL OF         12  INCREMENTS
                       0  CUTBACKS IN AUTOMATIC INCREMENTATION
                      12  ITERATIONS INCLUDING CONTACT ITERATIONS IF PRESENT
                      12  PASSES THROUGH THE EQUATION SOLVER OF WHICH 
                      10  INVOLVE MATRIX DECOMPOSITION, INCLUDING
                       0  DECOMPOSITION(S) OF THE MASS MATRIX
                       1  REORDERING OF EQUATIONS TO MINIMIZE WAVEFRONT
                       0  ADDITIONAL RESIDUAL EVALUATIONS FOR LINE SEARCHES
                       0  ADDITIONAL OPERATOR EVALUATIONS FOR LINE SEARCHES
                       1  WARNING MESSAGES DURING USER INPUT PROCESSING
                      22  WARNING MESSAGES DURING ANALYSIS
                      10  ANALYSIS WARNINGS ARE NUMERICAL PROBLEM MESSAGES
                       0  ANALYSIS WARNINGS ARE NEGATIVE EIGENVALUE MESSAGES
                       0  ERROR MESSAGES



     JOB TIME SUMMARY
       USER TIME (SEC)      =      0.0    
       SYSTEM TIME (SEC)    =     0.30    
       TOTAL CPU TIME (SEC) =     0.30    
       WALLCLOCK TIME (SEC) =            0
       MEMORY PEAK (GB)     =            0
