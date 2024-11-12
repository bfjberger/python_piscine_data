import sys
import time

def ft_tqdm(lst: range) -> None:
    total_item = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst):
        progress = (i + 1) * 100 / total_item
        bar_length = 81  # Length of the progress bar
        filled_length = int(bar_length * progress // 100)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        # Calculate elapsed time and speed
        time_elapse = time.time() - start_time
        speed = (i + 1) / time_elapse if time_elapse > 0 else 0

        # Format elapsed time and remaining time
        elapsed_formatted = time.strftime("%M:%S", time.gmtime(time_elapse))
        remaining_time = (total_item - (i + 1)) / speed if speed > 0 else 0
        remaining_formatted = time.strftime("%M:%S", time.gmtime(remaining_time))

        # Only display output after a certain progress level (e.g., > 10%)
        if progress > 10:
            # Construct the output string without extra characters
            output = (f"\r{int(progress)}%|{bar}| {i + 1}/{total_item} "
                    f"[{elapsed_formatted}<{remaining_formatted}, {speed:.2f}it/s]   ")
            # Write the output to stdout
            sys.stdout.write(output)
            sys.stdout.flush()  # Flush to ensure it's printed immediately

        time.sleep(0.1)  # Simulate some work being done
        yield item

    print()  # Print a new line once the progress is done

# Example usage
# for item in ft_tqdm(range(10)):
#     time.sleep(0.1)  # Simulating work being done
# print()  # Final print to ensure a new line after completion