# 🧊 Wireframe-3D

A real-time 3D wireframe rendering engine with 6-DOF camera controls and near-plane perspective clipping, designed for the NumWorks calculator and written in MicroPython.

---

## ⌨️ Inputs & Controls

Toggle between navigation modes using the **OK** / **EXE** button:

- **OK / EXE** : Switch between **Translation Mode** (moving camera through 3D space) and **Look / Orientation Mode** (rotating camera angle).

### Translation Mode (Default)
- **Up / Down Arrows** : Move forward / backward along the camera facing vector.
- **Left / Right Arrows** : Strafe left / right.
- **CLEAR (Key 17) / Square (Key 23)** : Move along the vertical Z-axis (elevate / descend).

### Look / Orientation Mode
- **Left / Right Arrows** : Yaw (horizontal rotation).
- **Up / Down Arrows** : Pitch (vertical look, clamped between -90° and +90° to avoid gimbal artifacts).

---

## 🚀 Features

- **Full 6-DOF Camera** : Complete basis vectors computation (forward, right, up) with inverse matrix transformation.
- **Near-Plane Clipping** : Analytical edge clipping against the camera near-plane, preventing geometry behind the viewpoint from creating inverted projection glitches.
- **Perspective Projection** : Realistic field-of-view (FOV 60°) with dynamic focal length mapping to screen space.
- **Fast Line Rasterizer** : Bresenham-optimized integer drawing algorithm designed for calculator hardware limits.
- **Centroid Transformation** : Real-time matrix rotations applied directly around geometric centers.

---

## 🕰️ Project Evolution & History

Previous versions and progressive iterations are preserved in the [`history/`](history/) folder:

1. **`visu_3d.py`** *(Created March 12, 2024)* : Initial 3D engine prototype rendering basic 3D geometry in fixed perspective.
2. **`visu_3d_mouv.py`** *(Created March 12, 2024)* : Added vertex transformations and time speed control (`e^x` and `ln`), featuring a rotating 3D cube and multi-vertex forms.
3. **`visu_3d_cam.py`** *(Created January 27, 2025)* : Introduced free-fly camera movement and user-controlled 3-axis exploration with dual-mode navigation (`Shift`).
4. **`wireframe_3d.py`** *(Created June 25, 2025)* : Full architectural overhaul (**visu_3d_refonte**) featuring true 6-DOF camera matrices, near-plane frustum clipping, multi-mesh scene support, and optimized rendering.

---

## ℹ️ Technical Details

- **Target Resolution** : 320 × 222 pixels (native NumWorks display).
- **Libraries** : MicroPython standard modules `kandinsky` (rasterization) and `ion` (real-time key states).
- **Platform** : Runs directly on hardware NumWorks calculators (N0110/N0120) and browser emulators.

---

## 🛠️ Details

The project has been created the June 25 of 2025.
