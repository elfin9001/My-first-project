def calculate_total_runtime(scenes):
    """
    Calculates the total runtime of the film based on the length of individual scenes.
    The length of the scenes must be provided in minutes.
    """
    total_minutes = sum(scenes)
    hours = int(total_minutes // 60)
    minutes = int(total_minutes % 60)
    return hours, minutes

if __name__ == "__main__":
    # Example: The length of scenes in minutes
    project_scenes = [12.5, 5.0, 8.5, 22.0, 3.5, 15.0]
    
    print("--- Runtime Calculator ---")
    print(f"Number of scenes: {len(project_scenes)}")
    
    h, m = calculate_total_runtime(project_scenes)
    print(f"Estimated total runtime: {h} hours and {m} minutes.")
