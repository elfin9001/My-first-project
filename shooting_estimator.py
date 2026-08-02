def estimate_shooting_days(scene_pages, pages_per_day=5.0):
    """
    Estimates the number of shooting days required based on the script's page count.
    A standard industry assumption is shooting about 5 pages per day.
    """
    total_pages = sum(scene_pages)
    estimated_days = total_pages / pages_per_day
    
    # Round up to the nearest whole day
    if estimated_days > int(estimated_days):
        total_days = int(estimated_days) + 1
    else:
        total_days = int(estimated_days)
        
    return total_pages, total_days

if __name__ == "__main__":
    # Example: Page counts for each scene in the script
    script_scenes = [2.5, 1.0, 4.0, 3.5, 0.5, 6.0]
    
    print("--- Shooting Schedule Estimator ---")
    print(f"Number of scenes to shoot: {len(script_scenes)}")
    
    total_p, days = estimate_shooting_days(script_scenes)
    
    print(f"Total script pages: {total_p}")
    print(f"Estimated shooting days needed: {days} day(s)")
