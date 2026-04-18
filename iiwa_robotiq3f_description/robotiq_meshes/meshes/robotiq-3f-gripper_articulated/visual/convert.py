import trimesh, glob
for f in glob.glob('*.dae'):
    mesh = trimesh.load(f, force='mesh')
    out = f.replace('.dae', '.obj')
    mesh.export(out)
    print(f'Converted {f} -> {out}')
