import numpy as np
import plotly.graph_objects as go

def calculate_exit_point(entry_point, incident_vector, thickness, normal, n1, n2):
    normal = np.array(normal)
    # Normalize vectors
    incident_vector = np.array(incident_vector)
    incident_vector = incident_vector / np.linalg.norm(incident_vector)
    
    entry_point = np.array(entry_point)
    
    mu = n1 / n2
    
    # Calculate dot products
    n_dot_i = np.dot(normal, incident_vector)
    
    # Calculate the transmitted vector using the equations provided
    term_under_sqrt = 1 - mu**2 * (1 - n_dot_i**2)
    
    if term_under_sqrt < 0:
        # Total internal reflection occurs
        print("Total internal reflection occurs.")
        return None, None
    
    n_dot_t = -np.sqrt(term_under_sqrt)
    t_parallel = mu * (incident_vector - n_dot_i * normal)
    t_perpendicular = n_dot_t * normal

    transmitted_vector = t_parallel + t_perpendicular

    # Calculate the exit point
    # Move from the entry point along the refracted vector by the thickness of the glass
    exit_point = entry_point + transmitted_vector * (thickness / (-np.dot(transmitted_vector, normal)))

    return exit_point, transmitted_vector

def visualize_reflection(entry_point, incident_vector, thickness, exit_point, normal, marker_size):

    unit_incident_vecotr = np.array(incident_vector) / np.linalg.norm(incident_vector)
    
    # Prepare the data for Plotly
    x_data_incident = [entry_point[0] - unit_incident_vecotr[0], entry_point[0]]
    y_data_incident = [entry_point[1] - unit_incident_vecotr[1], entry_point[1]]
    z_data_incident = [entry_point[2] - unit_incident_vecotr[2], entry_point[2]]

    x_data_refracted = [entry_point[0], exit_point[0]] if exit_point is not None else []
    y_data_refracted = [entry_point[1], exit_point[1]] if exit_point is not None else []
    z_data_refracted = [entry_point[2], exit_point[2]] if exit_point is not None else []


    # Data for the light path if there were no glass
    normal = np.array(normal)
    no_glass_exit_point = entry_point +  unit_incident_vecotr * thickness / (-np.dot(unit_incident_vecotr, normal))
    x_data_no_glass = [entry_point[0], no_glass_exit_point[0]]
    y_data_no_glass = [entry_point[1], no_glass_exit_point[1]]
    z_data_no_glass = [entry_point[2], no_glass_exit_point[2]]
    
    fig = go.Figure()
    
    # Incoming light
    fig.add_trace(go.Scatter3d(
        x=x_data_incident,
        y=y_data_incident,
        z=z_data_incident,
        mode='lines+markers',
        line=dict(color='red', width=5),
        marker=dict(size=marker_size),
        name='Incoming Light'
    ))
    
    # Refracted light
    if exit_point is not None:
        fig.add_trace(go.Scatter3d(
            x=x_data_refracted,
            y=y_data_refracted,
            z=z_data_refracted,
            mode='lines+markers',
            line=dict(color='blue', width=5),
            marker=dict(size=marker_size),
            name='Refracted Light'
        ))

    
    # Path if no glass
    fig.add_trace(go.Scatter3d(
        x=x_data_no_glass,
        y=y_data_no_glass,
        z=z_data_no_glass,
        mode='lines',
        line=dict(color='black', width=2, dash='dash'),
        name='Path without Glass'
    ))

    # Entry and Exit points
    fig.add_trace(go.Scatter3d(
        x=[entry_point[0]],
        y=[entry_point[1]],
        z=[entry_point[2]],
        mode='markers',
        marker=dict(size=marker_size, color='green'),
        name='Entry Point'
    ))
    
    if exit_point is not None:
        fig.add_trace(go.Scatter3d(
            x=[exit_point[0]],
            y=[exit_point[1]],
            z=[exit_point[2]],
            mode='markers',
            marker=dict(size=marker_size, color='blue'),
            name='Exit Point'
        ))
    
    # Labels and layout
    fig.update_layout(
        scene=dict(
            xaxis_title='X Axis',
            yaxis_title='Y Axis',
            zaxis_title='Z Axis', 
        ),
        title='Refraction of Light Through Glass',
        showlegend=True
    )
    
    fig.show()
    print("Snell Law demonstrates a deviation of X", exit_point[0] - no_glass_exit_point[0], "mm")
    print("Snell Law demonstrates a deviation of y", exit_point[1] - no_glass_exit_point[1], "mm")


# Parameters
entry_point = (0, 0, 0)  # Example entry point on the top surface
incident_vector = (-1, 0,-1)  # Incident light vector
normal = (0,0,1)
thickness = 6.66  # Thickness of the glass in mm
n1 = 1
n2 = 1.47


# Calculate the exit point
exit_point, transmitted_vector = calculate_exit_point(entry_point, incident_vector, thickness, normal, n1, n2)

if exit_point is not None:
    print("Exit Point:", exit_point)
    print("Transmitted Vector:", transmitted_vector)

visualize_reflection(entry_point, incident_vector, thickness, exit_point, normal, 3)