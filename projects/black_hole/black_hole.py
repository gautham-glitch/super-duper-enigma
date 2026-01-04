import numpy as np
import plotly.graph_objects as go

# Constants
G, M, c = 6.67430e-11, 1e27, 3e8
dt, steps = 0.1, 120
bh = np.array([5e10, 5e10, 0])
R_s = 2 * G * M / c**2

# Accretion disk: multiple rings
n_rings, particles_per_ring = 5, 40
radii = np.linspace(3e10, 6e10, n_rings)
disk_pos, disk_vel = [], []

for r in radii:
    θ = np.linspace(0, 2*np.pi, particles_per_ring, endpoint=False)
    pos = np.column_stack((r*np.cos(θ), r*np.sin(θ), np.zeros(particles_per_ring))) + bh
    r_vec = pos - bh
    v = np.sqrt(G * M / r)
    tangent = np.column_stack((-r_vec[:,1], r_vec[:,0], np.zeros(particles_per_ring)))
    tangent /= np.linalg.norm(tangent, axis=1)[:,None]
    vel = tangent * v
    disk_pos.append(pos)
    disk_vel.append(vel)

disk_pos = np.vstack(disk_pos)
disk_vel = np.vstack(disk_vel)

# Jets
n_jet = 6
pos_j = np.tile(bh, (n_jet,1))
vel_j = np.zeros((n_jet,3))
vel_j[:n_jet//2,2] = c*0.8
vel_j[n_jet//2:,2] = -c*0.8

# Combine
pos = np.vstack((disk_pos, pos_j))
vel = np.vstack((disk_vel, vel_j))

# Simulation
frames = []
for _ in range(steps):
    r_vec = pos - bh
    r_mag = np.linalg.norm(r_vec, axis=1) + 1e-3
    f_mag = G*M / r_mag**2
    f_dir = -r_vec / r_mag[:,None]
    vel += f_mag[:,None] * f_dir * dt
    speed = np.linalg.norm(vel, axis=1)
    vel[speed > c] *= (c / speed[speed > c])[:,None]
    pos += vel * dt
    frames.append(go.Frame(data=[go.Scatter3d(
        x=pos[:,0], y=pos[:,1], z=pos[:,2],
        mode='markers', marker=dict(size=2, color='blue'))]))

# Plot
fig = go.Figure(
    data=[go.Scatter3d(x=pos[:,0], y=pos[:,1], z=pos[:,2],
                       mode='markers', marker=dict(size=2, color='blue')),
          go.Scatter3d(x=[bh[0]], y=[bh[1]], z=[bh[2]],
                       mode='markers', marker=dict(size=10, color='black'))],
    frames=frames,
    layout=go.Layout(
        title='Accretion Disk + Relativistic Jets',
        scene=dict(xaxis=dict(range=[0,1e11]), yaxis=dict(range=[0,1e11]), zaxis=dict(range=[-1e10,1e10])),
        updatemenus=[dict(type='buttons', showactive=False,
                          buttons=[dict(label='Play', method='animate',
                                        args=[None, {
                                            "frame": {"duration": 100, "redraw": True},
                                            "fromcurrent": True,
                                            "transition": {"duration": 0},
                                            "loop": True
                                        }]),
                                   dict(label='Pause', method='animate',
                                        args=[[None], {"frame": {"duration": 0}, "mode": "immediate"}])])]
    )
)

fig.show()