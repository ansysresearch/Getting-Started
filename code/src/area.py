""""
utils.py
-------------
An example for explaining multiple concepts including unittests, documentation and running parallel jobs.

"""
import numpy as np
from joblib import Parallel, delayed

__all__ = ["compute_triangle_area",
           "compute_mesh_area",
           "compute_mesh_area_parallel"]


def compute_triangle_area(vertices):
    """
    function to compute area of triangle from the coordinate of its vertices.

    It is based on the identity
    .. math::
    area = 1/2 AB \times AC

    where :math:`A, B` and :math:`C` are three vertices of the triangle.

    Args:
        vertices: (np.ndarray) numpy array of vertices of size 3x2 or 3x3

    Returns: (float) area

    """
    v01 = vertices[0] - vertices[1]
    v02 = vertices[0] - vertices[2]
    cross_prod = np.cross(v01, v02)
    area = 0.5 * np.linalg.norm(cross_prod)
    return area


def compute_mesh_area(mesh):
    """
    compute surface area of a mesh by summing the surface area of all faces
    Args:
        mesh: (trimesh.Trimesh) input mesh object

    Returns: (float) area

    """
    vertices = mesh.vertices
    faces = mesh.faces
    areas = [compute_triangle_area(vertices[face]) for face in faces]
    mesh_surface_area = sum(areas)
    return mesh_surface_area


def compute_mesh_area_parallel(mesh, n_jobs=2):
    """
    compute surface area of a mesh by summing the surface area of all faces.
    this function divides the computation between `n_jobs` workers (cores)
    to speedup the computation.

    Args:
        mesh: (trimesh.Trimesh) input mesh object
        n_jobs: (int) number of parallel workers

    Returns: (float) area

    """
    vertices = mesh.vertices

    # we define an auxiliary function that will be passed to each worker.
    def func(dummy_faces):
        return [compute_triangle_area(vertices[face]) for face in dummy_faces]

    faces = mesh.faces
    faces_split = np.array_split(faces, n_jobs)
    areas = Parallel(n_jobs=n_jobs)(delayed(func)(f) for f in faces_split)
    mesh_surface_area = np.array(areas).sum()
    return mesh_surface_area


def compute_mesh_area_numpy(mesh):
    """
    compute surface area of a mesh by summing the surface area of all faces
    here instead of looping over all faces, we use numpy slicing and compute it in one go.
    Args:
        mesh: (trimesh.Trimesh) input mesh object

    Returns: (float) area

    """
    pass


def compute_mesh_area_smart(mesh):
    """
    compute surface area of a mesh by summing the surface area of all faces
    turns out that trimesh library actually has a fast implementation for this ALREADY.
    Args:
        mesh: (trimesh.Trimesh) input mesh object

    Returns: (float) area

    """
    mesh_surface_area = mesh.area
    return mesh_surface_area

