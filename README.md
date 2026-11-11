# 🧊 Wireframe-3D

A real-time 3D wireframe rendering engine with 6-DOF camera controls and perspective clipping, designed for the NumWorks calculator and written in MicroPython.

## ⌨️ Inputs

Toggle between navigation modes using the **OK** button:

- **OK / EXE** : Switch between **Translation** (moving through 3D space) and **Look / Orientation** (rotating camera).

### Translation Mode (Default)
- **Up / Down Arrows** : Move forward / backward
- **Left / Right Arrows** : Move left / right (strafe)
- **Key 17 (CLEAR) / Key 23 (→)** : Elevate up / descend down

### Look Mode
- **Left / Right Arrows** : Yaw (horizontal look)
- **Up / Down Arrows** : Pitch (vertical look, clamped between -90° and +90°)

## 🚀 Features

- **Full 6-DOF Camera** : Basis vectors calculation (Yaw, Pitch, Roll) and inverse projection.
- **Near-Plane Clipping** : Edge clipping prevents geometry projection behind the camera lens.
- **Perspective Projection** : Dynamic projection based on a 60° field of view and focal length.
- **Fast Line Rasterizer** : Custom Bresenham-style line rendering tailored for calculator hardware.
- **Centroid Rotations** : Real-time matrix transformation around geometric centers.

## ℹ️ Technical Details

- **Target Resolution** : 320 × 222 pixels (native NumWorks screen).
- **Libraries** : Powered by `kandinsky` (screen drawing) and `ion` (keyboard inputs).
- **Platform** : Runs directly on physical NumWorks calculators or within web simulators.

It was coded on a Numworks calculator in Micropython.

The project has been created the August 27 of 2024.
