def lru_page_replacement(pages, num_frames):
    frames = []
    page_faults = 0

    for page in pages:
        if page in frames:
            frames.remove(page)
            frames.append(page)
        else:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
            page_faults += 1
        print(f"Page: {page}, Frames: {frames}")

    return page_faults


# Example
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
num_frames = 4
faults = lru_page_replacement(pages, num_frames)
print(f"Total Page Faults (LRU): {faults}")
