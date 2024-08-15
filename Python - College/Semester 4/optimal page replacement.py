def optimal_page_replacement(pages, num_frames):
    frames = []
    page_faults = 0

    for i in range(len(pages)):
        page = pages[i]
        if page not in frames:
            if len(frames) < num_frames:
                frames.append(page)
            else:
                future_uses = [
                    pages[i + 1 :].index(p) if p in pages[i + 1 :] else float("inf")
                    for p in frames
                ]
                to_replace = future_uses.index(max(future_uses))
                frames[to_replace] = page
            page_faults += 1
        print(f"Page: {page}, Frames: {frames}")

    return page_faults


# Example
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3]
num_frames = 4
faults = optimal_page_replacement(pages, num_frames)
print(f"Total Page Faults (Optimal): {faults}")
