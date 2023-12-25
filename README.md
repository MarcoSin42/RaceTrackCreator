** Gaining insight on how to make good tracks **

20/12/23 - Gaining insight on how to make a good track

Currently, I'm working to find what makes a good track.  For our purposes, a good track is any track that's good enough for F1.  We'll first gather and synthesize some data.  We'll need some image representation of F1 tracks.  Fortunately, someone has done the work and [vectorized F1 tracks](https://github.com/f1laps/f1-track-vectors).

Next, we need some way to characterize each track numerically.  Since the curvature of the track, rather than the absolute distance of any segment of a track is what makes a track interesting.  We'll use the histogram of curvature to characterize each track.  Histograms of curvature are described [here](https://lmb.informatik.uni-freiburg.de/Publications/2014/FB14/gcpr2014_curvature.pdf)

Our next step is to visualize this somehow.


https://www.dgp.toronto.edu/~egarfink/Edy_Technical_report.pdf
