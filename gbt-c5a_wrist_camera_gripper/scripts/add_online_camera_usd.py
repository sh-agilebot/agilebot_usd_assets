#!/usr/bin/env python3

from pathlib import Path
import sys


DEFAULT_STAGE_PATH = Path("urdf/gbt-c5a_wrist_camera_gripper/gbt-c5a_wrist_camera_gripper.usd")
DEFAULT_STAGE_NAME = "gbt-c5a_wrist_camera_gripper.usd"
DEFAULT_CAMERA_PRIM_CANDIDATES = (
    "/GBT_C5A_wrist_camera_gripper/camera_mount_link/camera_link",
    "/World/GBT_C5A_wrist_camera_gripper/camera_mount_link/camera_link",
)
DEFAULT_CAMERA_RELATIVE_PATH = "/Isaac/Sensors/Orbbec/Gemini2/orbbec_gemini2_v1.0.usd"
DEFAULT_LOCAL_ASSET_ROOT = Path("/home/gbt/isaac_assets/Assets/Isaac/5.1")
LEGACY_CAMERA_URLS = {
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/"
    "Assets/Isaac/5.1/Isaac/Sensors/Orbbec/Gemini%202/orbbec_gemini2_V1.0.usd",
    "https://omniverse-content-production.s3-us-west-2.amazonaws.com/"
    "Assets/Isaac/5.1/Isaac/Sensors/Orbbec/Gemini2/orbbec_gemini2_v1.0.usd",
}


def import_usd_modules():
    from pxr import Sdf, Usd, UsdGeom

    return Sdf, Usd, UsdGeom


def ensure_prim(stage, prim_path: str):
    _, _, UsdGeom = import_usd_modules()
    prim = stage.GetPrimAtPath(prim_path)
    if prim.IsValid():
        return prim
    return UsdGeom.Xform.Define(stage, prim_path).GetPrim()


def resolve_camera_prim_path(stage) -> str:
    for prim_path in DEFAULT_CAMERA_PRIM_CANDIDATES:
        if stage.GetPrimAtPath(prim_path).IsValid():
            return prim_path

    matches = [str(prim.GetPath()) for prim in stage.Traverse() if prim.GetName() == "camera_link"]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        for prim_path in matches:
            if prim_path.startswith("/GBT_C5A_wrist_camera_gripper/"):
                return prim_path
        return matches[0]

    return DEFAULT_CAMERA_PRIM_CANDIDATES[0]


def list_reference_assets(prim) -> tuple[list[str], object | None]:
    refs = prim.GetMetadata("references")
    if refs is None:
        return [], None
    return [ref.assetPath for ref in refs.prependedItems], refs


def remove_legacy_references(prim) -> None:
    Sdf, _, _ = import_usd_modules()
    assets, refs = list_reference_assets(prim)
    if refs is None:
        return
    for asset in assets:
        if asset in LEGACY_CAMERA_URLS:
            prim.GetReferences().RemoveReference(Sdf.Reference(asset))
            print(f"Removed legacy reference: {asset}")


def build_asset_path() -> str:
    local_asset = DEFAULT_LOCAL_ASSET_ROOT / DEFAULT_CAMERA_RELATIVE_PATH.lstrip("/")
    if local_asset.exists():
        return str(local_asset)
    raise RuntimeError(f"Local Isaac asset not found: {local_asset}")


def add_camera_reference(stage_path: Path) -> None:
    _, Usd, _ = import_usd_modules()
    asset_path = build_asset_path()
    stage = Usd.Stage.Open(str(stage_path))
    if stage is None:
        raise RuntimeError(f"Failed to open stage: {stage_path}")

    prim_path = resolve_camera_prim_path(stage)
    prim = ensure_prim(stage, prim_path)
    remove_legacy_references(prim)
    existing_assets, _ = list_reference_assets(prim)

    if asset_path in existing_assets:
        print(f"Reference already exists on {prim_path}")
        print(f"Asset path: {asset_path}")
        return

    prim.GetReferences().AddReference(asset_path)
    stage.Save()
    print(f"Added reference to {asset_path}")
    print(f"Target prim: {prim_path}")
    print(f"Saved stage: {stage_path}")


def find_existing_stage(repo_root: Path) -> Path:
    preferred = repo_root / DEFAULT_STAGE_PATH
    if preferred.exists():
        return preferred

    candidates = sorted(repo_root.rglob(DEFAULT_STAGE_NAME))
    if candidates:
        return candidates[0]

    raise FileNotFoundError(f"Could not find existing USD stage named {DEFAULT_STAGE_NAME}")


def run_with_simulation_app(stage_path: Path) -> int:
    try:
        import_usd_modules()
    except ModuleNotFoundError:
        from isaacsim import SimulationApp

        app = SimulationApp({"headless": True})
        try:
            add_camera_reference(stage_path)
        finally:
            app.close()
        return 0

    add_camera_reference(stage_path)
    return 0


def main() -> int:
    repo_root = Path(__file__).resolve().parent.parent
    stage_path = Path(sys.argv[1]) if len(sys.argv) > 1 else find_existing_stage(repo_root)
    if not stage_path.is_absolute():
        stage_path = (repo_root / stage_path).resolve()
    if not stage_path.exists():
        print(f"Stage file not found: {stage_path}", file=sys.stderr)
        return 1

    try:
        return run_with_simulation_app(stage_path)
    except Exception as exc:
        print(f"Failed to attach camera: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
