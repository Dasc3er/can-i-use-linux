import os

build_path = "build"
os.makedirs(build_path, exist_ok=True)

base_template = ""
with open("base.html") as f:
    base_template = f.read()

index_contents = """
<div class="px-4 pt-5 my-5 text-center border-bottom">
    <h1 class="display-4 fw-bold text-body-emphasis">Can I Use Linux? - Demo</h1>
    <div class="col-lg-6 mx-auto">
        <p class="lead mb-4">
            Yes, most likely.
        </p>
        <p class="lead mb-4">
            In general, most devices are supported by recent Linux releases.
        </p>
        <p class="lead mb-4">
            In some rare cases, some peculiar features may not fully be supported (e.g. fingerprint sensors, ...).
            As all devices are different, we aim to provide a simple search utility to track if your specific device
            is well supported by Linux in all its capabilities and related version information for your usage.</p>
        <div class="alert alert-warning" role="alert">
            This site is currently experimental - it has been created as a demo and contains limited information.
            Due to this, there is no search utility and all records are listed below.
        </div>
    </div>
</div>

<div class="album py-5 bg-body-tertiary">
    <div class="container">
        <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
            <div class="col">
                <div class="card shadow-sm"> <svg aria-label="Placeholder: Thumbnail"
                        class="bd-placeholder-img card-img-top" height="225" preserveAspectRatio="xMidYMid slice"
                        role="img" width="100%" xmlns="http://www.w3.org/2000/svg">
                        <title>Placeholder</title>
                        <rect width="100%" height="100%" fill="#55595c"></rect><text x="50%" y="50%" fill="#eceeef"
                            dy=".3em">Thumbnail</text>
                    </svg>
                    <div class="card-body">
                        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                            additional content. This content is a little bit longer.</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="btn-group"> <button type="button"
                                    class="btn btn-sm btn-outline-secondary">View</button></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card shadow-sm"> <svg aria-label="Placeholder: Thumbnail"
                        class="bd-placeholder-img card-img-top" height="225" preserveAspectRatio="xMidYMid slice"
                        role="img" width="100%" xmlns="http://www.w3.org/2000/svg">
                        <title>Placeholder</title>
                        <rect width="100%" height="100%" fill="#55595c"></rect><text x="50%" y="50%" fill="#eceeef"
                            dy=".3em">Thumbnail</text>
                    </svg>
                    <div class="card-body">
                        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                            additional content. This content is a little bit longer.</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="btn-group"> <button type="button"
                                    class="btn btn-sm btn-outline-secondary">View</button></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col">
                <div class="card shadow-sm"> <svg aria-label="Placeholder: Thumbnail"
                        class="bd-placeholder-img card-img-top" height="225" preserveAspectRatio="xMidYMid slice"
                        role="img" width="100%" xmlns="http://www.w3.org/2000/svg">
                        <title>Placeholder</title>
                        <rect width="100%" height="100%" fill="#55595c"></rect><text x="50%" y="50%" fill="#eceeef"
                            dy=".3em">Thumbnail</text>
                    </svg>
                    <div class="card-body">
                        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to
                            additional content. This content is a little bit longer.</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <div class="btn-group"> <button type="button"
                                    class="btn btn-sm btn-outline-secondary">View</button></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

"""
with open(os.path.join(build_path, "index.html"), "w+") as f:
    content = base_template.replace("[body]", index_contents).replace("[title]", "Home")
    f.write(content)