import maya.cmds as cmds

def convertSelectedNParticleToCurves():
    """
    1. Finds the selected nParticle transform, then infers the nParticle shape within it.
    2. Uses the existing Maya timeline range (playbackOptions).
    3. Samples particle positions at each frame and creates curves.
    4. If 'position' returns 6 floats, we slice to the first 3.

    Usage:
      - Select the nParticle transform in the viewport or Outliner.
      - Run this function.
    """

    # --- Step 1: Identify the Selected Particle Shape ---
    sel = cmds.ls(selection=True, transforms=True)
    if not sel:
        cmds.error("No transform is selected. Select an nParticle transform and run again.")
        return

    # We expect the user to have selected the transform that has an nParticle shape child
    transform = sel[0]

    # Now, find any child shape of type "nParticle"
    shapes = cmds.listRelatives(transform, shapes=True, type="nParticle", fullPath=True) or []
    if not shapes:
        cmds.error("Selected transform '{}' does not have an nParticle shape.".format(transform))
        return

    # We’ll just use the first shape found
    particleShape = shapes[0]
    print("Selected transform: '{}' => using nParticle shape: '{}'".format(transform, particleShape))

    # --- Step 2: Get Timeline Range ---
    startFrame = int(cmds.playbackOptions(q=True, minTime=True))
    endFrame   = int(cmds.playbackOptions(q=True, maxTime=True))
    print("Timeline range is {} to {}.".format(startFrame, endFrame))

    # --- Prepare a dictionary to store positions: { particleID: [(x,y,z), ...] } ---
    positions_dict = {}

    # --- Step 3: Frame-by-Frame Sampling ---
    for frame in range(startFrame, endFrame + 1):
        cmds.currentTime(frame, update=True)
        try:
            currentCount = cmds.getAttr("{}.count".format(particleShape))
        except:
            # If shape name is invalid or something else is up
            print("Frame {} => ERROR: Could not query count for '{}'".format(frame, particleShape))
            continue

        if not currentCount:
            # No particles at this frame
            continue

        for pid in range(currentCount):
            try:
                posData = cmds.getParticleAttr("{}.pt[{}]".format(particleShape, pid), at='position')
            except:
                # Possibly the particle died or doesn't exist yet
                continue

            if not posData:
                continue

            # If posData is [[x,y,z, ...]], unwrap
            if isinstance(posData[0], (list, tuple)):
                posData = posData[0]

            # If 6 floats (xyz + 3 zeros), slice to the first 3
            if len(posData) == 6:
                posData = posData[:3]

            # We only accept if we now have exactly 3 floats
            if len(posData) != 3:
                continue

            # Store
            if pid not in positions_dict:
                positions_dict[pid] = []
            positions_dict[pid].append(tuple(posData))

    # --- Step 4: Create Curves for Each Particle ---
    created_count = 0
    for pid, pos_list in positions_dict.items():
        # Only build if we have > 1 frame of data
        if len(pos_list) > 1:
            crv = cmds.curve(p=pos_list, d=1, name="particlePath_{}_CRV".format(pid))
            created_count += 1
        else:
            pass  # A single-frame particle yields no curve

    print("\nDone! Created {} curves.".format(created_count))

# -----------------------------------------------------------------
# Run the function on the currently selected nParticle transform
# -----------------------------------------------------------------
convertSelectedNParticleToCurves()
