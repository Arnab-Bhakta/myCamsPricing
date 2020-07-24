import pickle
import os

price = 774.70


def renderer():
    print("html rendering started ......")
    with open("index1.txt", "r") as index1:
        s = index1.read()
        # print(s)
    s += """
        <tr>
            <td>Date</td>
            <td>Price</td>
            <td>Price Change</td>
        </tr>
    """
    with open("scrapped.pickle", "rb") as navs:
        navs = pickle.load(navs)
        for nav in navs:
            s = s + f"""
            <tr>
                <td>{nav["date"]}</td>
                <td>{ round(nav["nav"]*price,2)}</td>
                <td>{round(nav["change"]*price,2)}</td>
            </tr>
            """
    # print(s)

    with open("index2.txt", "r") as index2:
        s += (index2.read())
    # print(s)
    with open(os.path.join("public", "index.html"), "w") as out:
        out.write(s)
    print("html rendering done ..........")
    print()


if __name__ == "__main__":
    renderer()
