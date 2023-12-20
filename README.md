**Intro**
As it says on the tin, we generate race tracks procedurally.

**Problem Statement/Inspiration**
For my game design class, we had to design our own game (shocker).  We decided to make a Mario Kart clone game.  However, we were given the additonal constraint for our game that our game must be procedurally generated.  This meant that we had to find a way to generate random closed-loop tracks.  We had various different ideas, but eventually settled on using close-looped bezier curves as the data structure of choice.  My initial idea was to borrow from topology and use the fact that any smooth closed-loop (which every race track as far as I know satisfies) is topologically a circle.  I.e. any closed loop can be stretched and deformed such that you can make a circle and vice versa.  However, this is easier said than done, furthermore, any deformation will not necessarily create an interesting track.

**A naive attempt**

We start with an initial closed-loop bezier curve.  We find the centroid of bezier curve, **C**.  For each point, p_i, on the bezier-curve {p_1,p_2,...,p_n}, move them randomly along the direction of the vector p_i - C.  Where we restrict the direction to be strictly greater than zero so as to not have the track self-intersect.

Whilst this did create a 'random' track, it more often than not looked like fairly similar to the original track and did not give much variety.  Furthermore, this did not allow for chicanes or hairpins.  Overall the tracks were somewhat uninteresting.  

